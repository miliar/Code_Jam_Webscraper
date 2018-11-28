#include <bits/stdc++.h>

using namespace std;

mutex cerr_lock;
class LOG {
public:
    template<class T>
    LOG& operator<<(const T& value) {
        ss_ << value;
        return *this;
    }

    ~LOG() {
        lock_guard<mutex> lock(cerr_lock);
        cerr << ss_.str() << '\n';
        cerr.flush();
    }
private:
    stringstream ss_;
};

string f[3][15];

class TestImpl {
public:
    void Input() {
        cin >> n >> r >> p >> s; 
    }

    void Solve() {
        answer = "IMPOSSIBLE";
        bool done = false;
        for (int i = 0; i < 3; ++i) {
            const auto& a = f[i][n];
            int R = 0, S = 0, P = 0;
            for (int j = 0; j < a.size(); ++j) {
                if (a[j] == 'R') ++R;
                if (a[j] == 'P') ++P;
                if (a[j] == 'S') ++S;
            }

            if (R == r && S == s && P == p) {
                if (!done || a < answer) {
                    done = true;
                    answer = a;
                }
            }
        }
    }

    void Output() {
        cout << answer << endl;
    }

private:
    int n, r, p, s;
    string answer;
};

class Test {
public:
    void Input(int testNo) {
        testNo_ = testNo;
        impl_.reset(new TestImpl);
        impl_->Input();
        
        LOG() << "Test #" << testNo_ << " is inputted";
    }

    void Solve() {
        impl_->Solve(); 
        LOG() << "Test #" << testNo_ << " is solved";
    }

    void Output() {
        printf("Case #%d: ", testNo_);
        impl_->Output();
        LOG() << "Test #" << testNo_ << " is outputted";
    }

private:
    int testNo_;
    unique_ptr<TestImpl> impl_;
};

int looser[225];
const char* all = "SRP";

int main() {
    for (int i = 0; i < 3; ++i) f[i][0] = all[i];
    looser[int('S')] = 2;
    looser[int('R')] = 0;
    looser[int('P')] = 1;
    for (int level = 1; level < 15; ++level) {
        for (int i = 0; i < 3; ++i) {
            const auto& a = f[i][level - 1];
            const auto& b = f[looser[int(all[i])]][level - 1];
            f[i][level] = min(a + b, b + a);
        }
    }

    constexpr int N_THREADS = 4;
    vector<Test> tests;
    queue<int> not_solved;

    int T;
    scanf("%d\n", &T);
    tests.resize(T);
    for (int i = 0; i < T; ++i) {
        tests[i].Input(i + 1);
        not_solved.push(i);
    }
    
    mutex test_mutex;
    vector<thread> threads;
    for (int i = 0; i < N_THREADS; ++i) {
        threads.emplace_back(
                [&](){
                    bool done = false;
                    do {
                        int next_test = -1;
                        test_mutex.lock();
                        if (not_solved.empty()) {
                            done = true;
                        } else {
                            next_test = not_solved.front();
                            not_solved.pop();
                        }
                        test_mutex.unlock();
                        if (!done) {
                            tests[next_test].Solve();
                        }
                    } while (!done);
                });
    }

    for (auto& thread : threads) {
        thread.join();
    }

    for (auto& test : tests) {
        test.Output();
    }

    return 0;
}

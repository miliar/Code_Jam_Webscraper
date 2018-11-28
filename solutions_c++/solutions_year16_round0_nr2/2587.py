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

class TestImpl {
public:
    void Input() {
        cin >> s;
    }

    void Solve() {
        n = s.size();

        for (int q = 0; q < 2; ++q) {
            f[q].resize(n + 1);
            for (int i = 0; i <= n; ++i) {
                f[q][i].resize(n + 1);
                for (int j = 0; j <= n; ++j) {
                    f[q][i][j] = 1e9;
                    if (i == j) f[q][i][j] = 0;
                }
            }
        }

        for (int length = 1; length <= n; ++length) {
            for (int l = 0; l + length <= n; ++l) {
                int r = l + length;
                bool all0 = true, all1 = true;
                for (int i = l; i < r; ++i) {
                    if (s[i] == '+') all0 = false;
                    if (s[i] == '-') all1 = false;
                }

                if (all0) {
                    f[0][l][r] = 0;
                    f[1][l][r] = 1;
                    f[1][r][l] = 0;
                    f[0][r][l] = 1;
                    continue;
                }
                if (all1) {
                    f[0][l][r] = 1;
                    f[1][l][r] = 0;
                    f[1][r][l] = 1;
                    f[0][r][l] = 0;
                    continue;

                }

                for (int k = l + 1; k < r; ++k) {
                    for (int q = 0; q < 2; ++q) {
                        f[q][l][r] = min(f[q][l][r], f[1 - q][l][k] + 1 + f[q][r][k]);
                        f[q][r][l] = min(f[q][r][l], f[1 - q][r][k] + 1 + f[q][l][k]);

                        if (f[q][k][r] == 0) f[q][l][r] = min(f[q][l][r], f[q][l][k]);
                        if (f[q][k][l] == 0) f[q][r][k] = min(f[q][r][l], f[q][r][k]);
                    }
                }

                for (int times = 0; times < 5; ++times) {
                    for (int q = 0; q < 2; ++q) {
                        f[q][l][r] = min(f[q][l][r], 1 + f[1 - q][r][l]);
                        f[q][l][r] = min(f[q][l][r], f[q][r][l] + 2);
                        f[q][r][l] = min(f[q][r][l], 1 + f[1 - q][l][r]);
                        f[q][r][l] = min(f[q][r][l], f[q][l][r] + 2);
                    }
                }
            }
        }
    }

    void Output() {
        cout << f[1][0][n] << endl;
    }

private:
    int n;
    string s;
    vector<vector<int>> f[2];
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

protected:
    int testNo_;
    unique_ptr<TestImpl> impl_;
};

int main() {
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

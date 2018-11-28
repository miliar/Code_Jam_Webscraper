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

int count(int msk) {
    int res = 0;
    while (msk) {
        res += 1;
        msk &= (msk - 1);
    }
    return res;
}

class TestImpl {
public:
    void Input() {
        cin >> n;
        can.resize(n);
        for (int i = 0; i < n; ++i) {
            can[i].resize(n);
            for (int j = 0; j < n; ++j) {
                char c = getchar(); while (c != '0' && c != '1') c = getchar();
                can[i][j] = int(c - '0');
            }
        }
    }

    bool rec(int mans, int machines) {
        if (mans == clim - 1) {
            return true;
        }

        for (int man = 0; man < n; ++man)
            if (!(mans & (1 << man))) {
                bool cool = false;
                for (int machine = 0; machine < n; ++machine)
                    if (!(machines & (1 << machine)) && can[man][machine]) {
                        cool = true;
                        if (!rec(mans + (1 << man), machines + (1 << machine))) return false;
                    }
                if (!cool) return false;
            }

        return true;
    }

    bool tryit(int msk) {
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                can[i][j] = msk & (1 << (n * i + j));
            }
        }
        return rec(0, 0);
    }

    void Solve() {
        clim = 1 << n;
        int cmask = 0;
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j)
                if (can[i][j]) cmask += 1 << (n * i + j);

        int lim = 1 << (n * n);
        for (int msk = 0; msk < lim; ++msk) {
            if ((msk & cmask) != cmask) continue;
            int cand = count(msk ^ cmask);
            if (cand > ans) continue;
            
            if (tryit(msk)) ans = cand;
        }
    }

    void Output() {
        cout << ans << endl;
    }

private:
    int n;
    vector<vector<int>> can;
    int ans = 1e9;
    int clim;
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

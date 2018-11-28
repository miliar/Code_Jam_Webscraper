#include <bits/stdc++.h>

using namespace std;
typedef long double ld;

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
        cin >> n >> k;
        prob.resize(n);
        for (int i = 0; i < n; ++i) {
            ld x;
            cin >> x; 

            prob[i] = int(x * 100. + 1e-5);
        }
    }

    void tryit(const vector<int>& a, const vector<ld>& P, const vector<ld>& Q) {
        int count0 = 0, count1 = 0;
        for (int x : a) {
            if (x == 0) count0++;
            else if (x == 100) count1++;
        }

        if (count0 > k / 2 || count1 > k / 2) return;
        cool = true;

        vector<vector<ld>> f(k + 1);
        f[0].resize(1);
        f[0][0] = 0;
        for (int i = 1; i <= k; ++i) {
            f[i].resize(i + 1);
            for (int j = 0; j <= i; ++j) {
                if (j) {
                    f[i][j] += expl(f[i - 1][j - 1] + P[i - 1]);
                }
                if (j < i) {
                    f[i][j] += expl(f[i - 1][j] + Q[i - 1]);
                }
                f[i][j] = logl(f[i][j]);
            }
        }
        ans = max(ans, expl(f[k][k / 2]));
    }

    void Solve() {
        sort(begin(prob), end(prob));
        p.resize(n);
        q.resize(n);
        for (int i = 0; i < n; ++i) {
            if (prob[i] == 0) {
                p[i] = -(1e100);
                q[i] = 0;
            } else if (prob[i] == 100) {
                q[i] = -(1e100);
                p[i] = 0;
            } else {
                p[i] = logl(ld(prob[i])) - logl(ld(100));
                q[i] = logl(ld(100 - prob[i])) - logl(ld(100));
            }
        }

        for (int left = 0; left <= k; ++left) {
            int right = k - left;

            vector<int> a;
            vector<ld> ps, qs;
            for (int i = 0; i < left; ++i) {
                a.push_back(prob[i]);
                ps.push_back(p[i]);
                qs.push_back(q[i]);
            }
            for (int i = 0; i < right; ++i) {
                a.push_back(prob[n - 1 - i]);
                ps.push_back(p[n - 1 - i]);
                qs.push_back(q[n - 1 - i]);
            }

            tryit(a, ps, qs);
        }

        /*
        f[0][0][0] = 0;
        used[0][0][0] = true;
        for (int i = 1; i <= n; ++i) {
            used[i][0][0] = true;
            f[i][0][0] = 0;
            for (int chosen = 1; chosen <= i; ++chosen) {
                for (int yes = 0; yes <= chosen; ++yes) {
                    if (used[i - 1][chosen][yes]) {
                        used[i][chosen][yes] = true;
                        f[i][chosen][yes] = f[i - 1][chosen][yes];
                    }

                    if (yes && used[i - 1][chosen - 1][yes - 1] && prob[i] != 0) {
                        if (!used[i][chosen][yes] || f[i - 1][chosen - 1][yes - 1] + p[i] > f[i][chosen][yes]) {
                            used[i][chosen][yes] = true;
                            f[i][chosen][yes] = f[i - 1][chosen - 1][yes - 1] + p[i];
                        }
                    }

                    if (used[i - 1][chosen - 1][yes] && prob[i] != 100) {
                        if (!used[i][chosen][yes] || f[i - 1][chosen - 1][yes] + q[i] > f[i][chosen][yes]) {
                            used[i][chosen][yes] = true;
                            f[i][chosen][yes] = f[i - 1][chosen - 1][yes] + q[i];
                        }
                    }
                }
            }
        }
        */
    }

    void Output() {
        /*
        if (!used[n][k][k / 2]) {
            printf("0.00000000\n");
        } else {
            cout.precision(20); cout << fixed;
            cout << expl(f[n][k][k / 2]) << endl;
        }
        */
        cout.precision(20); cout << fixed;
        cout << ans << endl;
    }

private:
    ld ans = 0;
    bool cool = false;
    int n, k;
    //ld f[222][222][222];
    vector<ld> p, q;
    //bool used[222][222][222];
    vector<int> prob;
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

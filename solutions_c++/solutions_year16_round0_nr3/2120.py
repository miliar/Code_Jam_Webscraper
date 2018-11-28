#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

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
        cin >> n >> j;
    }

    void Solve() {
        vector<long long> powers[11];
        for (int i = 1; i < 11; ++i) {
            powers[i].push_back(1);
        }
        for (int i = 0; i < n; ++i) {
            for (long long c = 1; c <= 10; ++c) {
                powers[c].push_back(powers[c].back() * c);
            }
        }

        int lim = 1 << n;
        for (int msk = 0; msk < lim; ++msk) {
            if (!(msk & 1)) continue;
            if (!(msk & (1 << (n - 1)))) continue;

            bool cool = true;
            vector<ll> divisors;
            for (ll c = 2; c <= 10; ++c) {
                ll m = 0;
                for (int i = 0; i < n; ++i) {
                    if (msk & (1 << i)) m += powers[c][i];
                }

                int clim = min(10000ll, m - 1);
                cool = false;
                for (int d = 2; d <= clim; ++d) {
                    if (!(m % d)) {
                        divisors.push_back(d);
                        cool = true;
                        break;
                    }
                }

                if (!cool) break;
            }

            if (cool) {
                ans.emplace_back(msk, divisors);
                if (int(ans.size()) == j) break;
            }
        }
    }

    void Output() {
        if (ans.size() != size_t(j)) {
            cout << "Impossible" << endl;
        } else {
            cout << endl;
            for (int i = 0; i < j; ++i) {
                for (int q = n - 1; q >= 0; --q) {
                    cout << ((ans[i].first & (1 << q)) ? 1 : 0);
                }
                for (ll x : ans[i].second) {
                    cout << ' ' << x;
                }
                cout << endl;
            }
        }
    }

private:
    int n, j;
    vector<pair<int, vector<ll>>> ans;
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

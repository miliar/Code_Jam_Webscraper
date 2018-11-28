#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <tuple>
#include <numeric>
#include <functional>
using namespace std;

class TTestCase {
public:
    int N, M;
    typedef long long ll;
    static const ll MOD = ll(1e9) + 2013;
    long long f(long long diff, long long p) {
        return (ll(N)*diff - ll(diff) * (diff - 1) / 2) % MOD * p % MOD;
    }
    void runTest() {
        cin >> N >> M;
        typedef pair<int,int> pii;
        vector<pii> events;
        ll result = 0;
        for (int i = 0; i < M; ++i) {
            int o, e, p;
            cin >> o >> e >> p;
            events.push_back(pii(o, -p));
            events.push_back(pii(e, p));
            result += f(e - o, p);
            result %= MOD;
        }
        sort(events.begin(), events.end());
        map<int, ll, greater<int> > cl;
        for (auto ev = events.begin(); ev != events.end(); ++ev) {
            if (ev->second < 0) {
                cl[ev->first] -= ev->second;
            } else {
                for (ll rem = ev->second; rem != 0; ) {
                    ll df = min(rem, cl.begin()->second);
                    result -= f(ev->first - cl.begin()->first, df);
                    result %= MOD;
                    rem -= df;
                    cl.begin()->second -= df;
                    if (cl.begin()->second == 0)
                        cl.erase(cl.begin());
                }
            }
        }
        cout << (result + MOD) % MOD << endl;
    }
};

int main(void) {
    ios::sync_with_stdio(false);
    int T;
    cin >> T;
    for (int testNo = 1; testNo <= T; ++testNo) {
        cout << "Case #" << testNo << ": ";
        TTestCase().runTest();
    }
    return 0;
}

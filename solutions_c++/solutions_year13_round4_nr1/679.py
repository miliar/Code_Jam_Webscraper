#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>

using namespace std;

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define REP(i,n) FOR(i,0,n)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define INF 1000000000
#define X first
#define Y second
#define pb push_back

typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef vector<VI> VVI;

long long cost(long long n, long long d) {
    return (n + (n-d+1))*d/2;
}

const int mod = 1000002013;

int main () {
    freopen ("input.txt", "r", stdin);
    freopen ("output.txt", "w+", stdout);

    int t;
    cin >> t;
    REP (tt, t) {
        std::cout << "Case #" << tt+1 << ": ";
        long long res = 0;

        int n;
        cin >> n;
        int m;
        cin >> m;

        VI x(m);
        VI y(m);
        VI c(m);
        REP (i, m)
            cin >> x[i] >> y[i] >> c[i];

        bool ok = true;

        while (ok) {
            ok = false;
            for (size_t i=0; i<x.size(); ++i)
            {
                for (size_t j=i+1; j<x.size(); ++j) {
                    if (max(x[i], y[i]) < min(x[j], y[j])) continue;
                    if (min(x[i], y[i]) > max(x[j], y[j])) continue;
                    long long old_cost = cost(n, abs(x[i]-y[i])) + cost(n, abs(x[j]-y[j]));
                    long long new_cost = cost(n, abs(x[i]-y[j])) + cost(n, abs(y[i]-x[j]));
                    if (new_cost < old_cost) {
                        int cc = min(c[i], c[j]);
                        c[i] -= cc;
                        c[j] -= cc;
                        x.pb(x[i]); y.pb(y[j]); c.pb(cc);
                        x.pb(x[j]); y.pb(y[i]); c.pb(cc);
                        if (c[i] == 0) {
                            swap (c[i], c.back());
                            swap (x[i], x.back());
                            swap (y[i], y.back());
                            x.pop_back(); y.pop_back(); c.pop_back();
                        }
                        if (c[j] == 0) {
                            swap (c[j], c.back());
                            swap (x[j], x.back());
                            swap (y[j], y.back());
                            x.pop_back(); y.pop_back(); c.pop_back();
                        }

                        ok = true;
                        res += (old_cost - new_cost)%mod*cc%mod;
                        res %= mod;
                    }

                }

            }
            if (!ok)
                break;

        }

        cout << res << endl;
    }

    return 0;
}

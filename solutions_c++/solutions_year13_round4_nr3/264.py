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

int main () {
    freopen ("input.txt", "r", stdin);
    freopen ("output.txt", "w+", stdout);

    int t;
    cin >> t;
    REP (tt, t) {
        std::cout << "Case #" << tt+1 << ":";

        int n;
        cin >> n;
        VI a(n), b(n);
        REP (i, n)
            cin >> a[i];
        REP (i, n)
            cin >> b[i];

        VVI r(1<<n, VI(n, INF));

        r[0] = VI(n, 0);

        REP (i, 1<<n)
            if (r[i][0] < INF) {
                int x = 1;
                REP (j, n)
                    if (r[i][j])
                        x++;

                REP (j, n)
                    if (!r[i][j]) {
                        int v1 = 1;
                        int v2 = 1;
                        REP (k, j)
                            if (r[i][k])
                                v1 = max (v1, a[k]+1);
                        FOR (k, j+1, n)
                            if (r[i][k])
                                v2 = max (v2, b[k]+1);

                        if (v1 == a[j] && v2 == b[j]) {
                            VI v = r[i];
                            v[j] = x;
                            r[i | (1<<j)] = min (r[i | (1<<j)], v);
                        }
                    }
            }

        REP (i, n)
        {
            cout << " " << r[(1<<n)-1][i];
        }
        cout << endl;
    }

    return 0;
}

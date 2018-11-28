#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
#define VAR(a,b) __typeof(b) a=(b)
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define REP(i,n) FOR(i,0,n)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define SZ(c) (c).size()
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<PII> VPII;
typedef vector<VI> VVI;

int solve1( vector<long double> a, vector<long double> b) {
    int res = 0;
    SORT (a);
    SORT (b);
    REP (i, a.size()) {
        if (a[0] > b[0])
        {
            res ++;
            a.erase(a.begin());
            b.erase(b.begin());
        } else {
            b.pop_back();
            a.erase(a.begin());
        }
    }

    return res;
}

int solve2( vector<long double> a, vector<long double> b) {
    int res = 0;
    SORT (a);
    SORT (b);
    REP (i, a.size()) {
        if (a.back() > b.back())
        {
            res ++;
            a.pop_back();
            b.erase(b.begin());
        } else {
            b.pop_back();
            a.pop_back();
        }
    }

    return res;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w+", stdout);

    int tt;
    cin >> tt;
    REP (t, tt) {
        cout << "Case #" << (t+1) << ": ";

        int n;
        cin >> n;
        vector<long double> a(n), b(n);
        REP(i, n)
            cin >> a[i];
        REP(i, n)
            cin >> b[i];

        cout << solve1(a, b)<< " " << solve2(a, b) << endl;
    }

	return 0;
}

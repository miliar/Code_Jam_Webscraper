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

FILE* tmp;

int main()
{
	freopen_s(&tmp, "input.txt", "r", stdin);
	freopen_s(&tmp, "output.txt", "w+", stdout);

	int tt;
	cin >> tt;

	map<char, PII> M;
	M['v'] = PII(1, 0);
	M['^'] = PII(-1, 0);
	M['>'] = PII(0, 1);
	M['<'] = PII(0, -1);

	REP(t, tt) {
		cout << "Case #" << t + 1 << ": ";
		int n, m;
		cin >> n >> m; 
		vector<string> a(n);
		REP(i, n)
			cin >> a[i];

		vector<int> x(n), y(m);

		REP (i, n)
			REP (j, m)
				if (a[i][j] != '.') {
					x[i] ++;
					y[j] ++;
				}

		int res = 0;

		REP (i, n)
			REP(j, m) {
				if (a[i][j] == '.')
					continue;
				
				int xx = i;
				int yy = j;
				PII d = M[a[i][j]];
				xx += d.X;
				yy += d.Y;

				while (xx >= 0 && xx < n && yy >= 0 && yy < m) {
					if (a[xx][yy] != '.')
						goto next;
					xx += d.X;
					yy += d.Y;
				}

				if (x[i] > 1 || y[j] > 1)
					res++;
				else
					res = INF;

				next:;
			}

		if (res < INF)
			cout << res << endl;
		else
			cout << "IMPOSSIBLE" << endl;
	}

	return 0;
}

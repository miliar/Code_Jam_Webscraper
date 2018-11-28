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
	REP(t, tt) {
		cout << "Case #" << t + 1 << ":";
		int p;
		cin >> p;
		VI e(p), f(p);

		REP(i, p)
			cin >> e[i];
		REP(i, p)
			cin >> f[i];

		f[0] --;

		set<PII> s;
		FOR(i, 0, p) if (f[i])
			s.insert(PII(e[i], f[i]));

		VI res;

		while (!s.empty()) {
			int x = s.begin()->X;
			
			REP(m, 1 << res.size()) {
				int v = x;
				REP(i, res.size())
					if (m & (1 << i))
						v += res[i];

				auto it = s.lower_bound(PII(v, 0));
				//cout << v << endl;
				int y = it->Y-1;
				s.erase(it);
				if (y)
					s.insert(PII(v, y));
			}
			//cout << " x = " << x << endl;
			res.pb(x);
		}
		REP(i, res.size())
			cout << " " << res[i];
		cout << endl;
	}

	return 0;
}

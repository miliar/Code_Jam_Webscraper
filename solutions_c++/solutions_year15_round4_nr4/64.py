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
		cout << "Case #" << t + 1 << ": ";
		int r, c;
		cin >> r >> c;

		int res = 0;

		switch (r) {
		case 1:
			res = 1;
			break;
		case 2:
			if (c == 3)
				res = 2;
			else if (c == 6)
				res = 3;
			else
				res = 1;
			break;
		case 3: // 3, 2 or 2, 3
			if (c == 4)
				res = 3;
			else 
				res = 2;
			break;
		case 4: // 2, 3, 2 or 3 + combo or combo + 3
			if (c == 3)
				res = 3;
			else if (c == 6)
				res = 5;
			else
				res = 1;
			break;
		case 5: // 3, 2, 3 or 2, 3, combo or combo, 3, 2
			if (c == 3)
				res = 3;
			else if (c == 6)
				res = 5;
			else if (c == 4)
				res = 3;
			else
				res = 1;
			break;
		case 6: // 2,3,2,3 or 3,2,3,2 or combo, 3, combo or 3, combo, 3
			if (c == 3)
				res = 1 + 1 + 3 + 1;
			else if (c == 6)
				res = 1 + 1 + (6 + 3 + 3 + 3) + 2;
			else if (c == 4)
				res = 2 + 2;
			else
				res = 2;
			break;
		default:
			while (1);
		}

		cout << res << endl;
	}

	return 0;
}

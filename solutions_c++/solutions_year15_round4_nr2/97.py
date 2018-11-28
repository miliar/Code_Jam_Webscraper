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

typedef long double cfloat;

FILE* tmp;

cfloat eps = 1e-10;

int main()
{
	freopen_s(&tmp, "input.txt", "r", stdin);
	freopen_s(&tmp, "output.txt", "w+", stdout);

	int tt;
	cin >> tt;
	REP(t, tt) {
		cout << "Case #" << (t + 1) << ": ";

		int n;
		cfloat v, x;
		cin >> n >>v >> x;
		vector<pair<cfloat, cfloat>> a(n);
		REP(i, n)
			cin >> a[i].Y >> a[i].X;
		SORT(a);

		cfloat ti1 = v;
		{
			cfloat vv = 0;
			REP(i, n)
				vv += a[i].Y;
			ti1 /= vv;
		}

		cfloat ti2 = 1e10;

		REP(i, n)
			FOR(j, i+1, n)
			if (a[i].X == a[j].X) {
				a[i].Y += a[j].Y;
				a[j].Y = 0;
			}

		FORD(i, n - 1, 0) {
			if (a[i].Y == 0) {
				a.erase(a.begin() + i);
				n--;
			}
		}

		if (a[0].X == x) {
			while (a[n - 1].X != x) {
				a.pop_back();
				n--;
			}
		}

		if (a.back().X == x) {
			while (a[0].X != x) {
				a.erase(a.begin());
				n--;
			}
		}
		REP(i, 1000) {
			cfloat t = (ti1+ti2)/2;

			cfloat v1 = 0;
			cfloat t1 = 0;

			cfloat v2 = 0;
			cfloat t2 = 0;

			REP(i, n) {
				cfloat vv = min(v - v1, a[i].Y * t);
				v1 += vv;
				t1 += vv*a[i].X;
			}

			FORD(i, n - 1, 0) {
				cfloat vv = min(v - v2, a[i].Y * t);
				v2 += vv;
				t2 += vv*a[i].X;
			}

			//cout << t << " " << v1 << " " << t1 << " " << v2 << " " << t2 << endl;

			if (t1/v > x || t2/v < x)
				ti1 = t;
			else
				ti2 = t;

		}

		cfloat t = (ti1 + ti2) / 2;

		cfloat t2 = -1;

		if (n == 1) {
			if (a[0].X == x) {
				t2 = v / a[0].Y;
				cout << t2 << endl;
				continue;
			}
			else {
				t2 = 1e10;
				cout << "IMPOSSIBLE" << endl;
				continue;
			}
		}/*
		else {
			if (a[0].X == a[1].X) {
				if (a[0].X == x)
					t2 = v / (a[0].Y + a[1].Y);
				else
					t2 = 1e10;
			}
			else {
				if (a[0].X == x)
					t2 = v / a[0].Y;
				else if (a[1].X == x)
					t2 = v / a[1].Y;
				else if (a[0].X > x || a[1].X < x)
					t2 = 1e10;
				else {
					//v1 * a[0].X + (v - v1)* a[1].X = v * x;
					cfloat v1 = (v*x - v*a[1].X) / (a[0].X - a[1].X);
					cfloat v2 = v - v1;

					t2 = max(v1 / a[0].Y, v2 / a[1].Y);
				}
			}
		}*/
		
		cout.precision(20);
		if (t > 1e9)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << t << endl;
		/*if (t2 > 1e9)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << t2 << endl;
			*/
		

	}

	return 0;
}

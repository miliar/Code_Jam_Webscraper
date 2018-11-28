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

std::vector<int> s, m, ok;
VVI e;
int n, d;
int sum = 0;

void add(int i) {
	if (!ok[i]) ok[i] = 1;

	if (i && ok[m[i]] < 2)
		return;

	ok[i] = 2;
	sum ++;
	//cout << "add " << i << endl;

	for (auto x : e[i]) {
		if (ok[x])
			add(x);
	}
}
void remove(int i) {
	if (ok[i] < 2) {
		ok[i] = 0;
		return;
	}
	sum--;
	//cout << "remove " << i << endl;
	ok[i] = 0;

	for (auto x : e[i]) {
		remove(x);
	}
}


int main()
{
	freopen_s(&tmp, "input.txt", "r", stdin);
	freopen_s(&tmp, "output.txt", "w+", stdout);

	int tt;
	cin >> tt;
	REP(t, tt) {
		cout << "Case #" << (t + 1) << ": ";

		cin >> n >> d;

		long long s0, as, cs, rs;
		cin >> s0 >> as >> cs >> rs;
		long long m0, am, cm, rm;
		cin >> m0 >> am >> cm >> rm;


		s.resize(0);
		m.resize(0);
		
		REP(i, n) {
			s.pb(s0);
			m.pb(m0 % max(i, 1));

			s0 = (s0*as + cs) % rs;
			m0 = (m0*am + cm) % rm;

			//cout << i << " " << s.back() << " " << m.back() << endl;
		}

		VPII o;
		REP(i, n)
			o.pb(PII(s[i], i));

		SORT(o);
	
		e = VVI();
		e.resize(n);
		
		FOR(i, 1, n)
			e[m[i]].pb(i);

		sum = 0;

		int res = 0;

		ok = VI(n);

		int x = 0;
		REP(i, n) {
			add(o[i].Y);
			while (s[o[x].Y] + d < s[o[i].Y]) {
				remove(o[x].Y);
				x++;
			}

			res = max(res, sum);
		}

		std::cout << res << endl;
	}

	return 0;
}

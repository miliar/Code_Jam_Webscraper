#include <functional>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <numeric>
#include <cstring>
#include <cassert>
#include <cstdio>
#include <string>
#include <vector>
#include <bitset>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <list>
#include <set>
#include <map>
#include <complex>
using namespace std;

#define FOR(i, a, b) for(int i = a, __up = b; i < __up; ++i)
#define REP(n) FOR(i, 0, n)
#define CLR(a) memset(a, 0, sizeof a)

typedef complex<double> point;
typedef long long ll;

// S E N W
int dx[]={1,0,-1,0};
int dy[]={0,1,0,-1};

void solve() {
	double c, f, x, s;
	// 0
	cin >> c >> f >> x;
	s = f*(x-c)/c;
	if (s < 2 || x <= c) {
		cout << x/2.0;
	} else {
		s -= 2;
		int t = ceil(s/f);
		double ans = 0, cur = 2;
		REP(t) {
			ans += c/cur;
			cur += f;
		}
		ans += x/cur;
		printf("%.7f", ans);
	}

	puts("");

}
int main()
{
	int T;
	cin >> T;
	REP(T) {
		printf("Case #%d: ", i+1);
		solve();
	}

	return 0;
}

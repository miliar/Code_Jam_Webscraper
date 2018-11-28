#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <string.h>
#define rep(x,n) for(int x=0;x<n;++x)
#define rep1(i,s) for(int i = 0; i < (int)s.size(); ++i)
#define mem(a, b) memset(a, b, sizeof(a))

#define mp(x,y) make_pair(x,y)
#define getBit(code, i) (code & (1 << i))
#define setBit(code, i) (code | (1 << i))
#define xetBit(code, i) (code & ~(1 << i))
#define PI acos(-1.0)
#define oo (int)10e7
#define rd(x) scanf("%d", &x)
#define rdfile(x) freopen(x, "r", stdin)
#define wtfile(x) freopen(x, "w", stdout)
using namespace std;

#define negamod(x, mod) ((x + mod) % mod)

int main() {

	rdfile("in.txt");
	wtfile("out.txt");
	long long r, t;

	int cas;
	cin >> cas;

	rep(cc, cas) {

		cin >> r >> t;

		int res = 0;
		long long cur = 1;
		while (t > 0) {
			t -= (((cur + r) * (cur + r)) - ((cur - 1 + r) * (cur - 1 + r)));
			if (t >= 0)
				++res;
			cur += 2;
		}

		cout << "Case #" << cc + 1 << ": " << res << endl;
	}

	return 0;
}


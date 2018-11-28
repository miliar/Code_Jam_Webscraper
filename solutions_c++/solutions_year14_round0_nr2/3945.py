#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <vector>
#include <cstdlib>
#include <fstream>
#include <sstream>
#include <deque>
#include <cassert>

using namespace std;

#ifdef WIN32
	#define I64 "%I64d"
#else
	#define I64 "%lld"
#endif

typedef long long ll;
typedef long double ld;

#define F first
#define S second
#define mp make_pair
#define pb push_back
#define all(s) s.begin(), s.end()
#define sz(s) (int(s.size()))
#define fname "a"
#define ms(a,x) memset(a, x, sizeof(a))
#define forit(it,s) for(__typeof(s.begin()) it = s.begin(); it != s.end(); ++it)

double tc, tf, tx;
const ld eps = 1e-9;

inline bool eq(ld a, ld b)
{
	return abs(a - b) < eps;
}

inline bool less1(ld a, ld b)
{
	return a < b && !eq(a, b);
}

inline void solve()
{
	scanf("%lf%lf%lf", &tc, &tf, &tx);
	ld c = tc;
	ld f = tf;
	ld x = tx;
	ld s = 2;
	ld ans = 0;
	while(less1(c / s + x / (s + f), x / s))
	{		
		ans += c / s;
		s += f;
	}
	printf("%.15lf\n", double(ans + x / s));
}

int main()
{
	#ifdef LOCAL
	freopen(fname".in", "r", stdin);
	freopen(fname".out", "w", stdout);
	#endif

	int tt;
	scanf("%d", &tt);
	for (int t = 0; t < tt; ++t)
	{
		printf("Case #%d: ", t + 1);
		solve();
	}
	return 0;
}

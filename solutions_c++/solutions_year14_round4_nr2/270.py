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

#define F first
#define S second
#define mp make_pair
#define pb push_back
#define all(s) s.begin(), s.end()
#define sz(s) (int(s.size()))
#define fname "a"
#define ms(a,x) memset(a, x, sizeof(a))
#define forit(it,s) for(__typeof(s.begin()) it = s.begin(); it != s.end(); ++it)
#define MAXN 1001

int n;
int a[MAXN];
pair <int, int> b[MAXN];
int ok[MAXN];

inline void solve()
{
	scanf("%d", &n);
	for (int i = 0; i < n; ++i)
	{
		ok[i] = 0;
		scanf("%d", &a[i]);
		b[i] = mp(a[i], i);
	}
	sort(b, b + n);
	int ans = 0;
	for (int i = 0; i < n; ++i)
	{
		int pos = b[i].S;
		int s1 = 0;
		for (int j = 0; j < pos; ++j)
			s1 += !ok[j];
		int s2 = 0;
		for (int j = pos + 1; j < n; ++j)
			s2 += !ok[j];
		ans += min(s1, s2);
		ok[pos] = 1;
	}
	printf("%d\n", ans);
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

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
#define MAXN 20002

int n, x;
int a[MAXN];
multiset <int> s;

inline void solve()
{
	scanf("%d%d", &n, &x);
	s.clear();
	for (int i = 0; i < n; ++i)
	{
		scanf("%d", &a[i]);
		s.insert(a[i]);
	}
	sort(a, a + n);
	int ans = 0;
	for (int i = n - 1; i >= 0; --i)
	{
		if (s.find(a[i]) == s.end()) continue;
		++ans;
		s.erase(s.find(a[i]));
		int rem = x - a[i];
      set <int>::iterator it = s.upper_bound(rem);
      if (it == s.begin()) continue;
      --it;
      s.erase(it);
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

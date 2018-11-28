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

int n = 4;
int a[4];

inline void solve()
{
	int x;
	scanf("%d", &x);
	--x;
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < n; ++j)
			if (i <= x)
				scanf("%d", &a[j]);
			else
				scanf("%*d");
	
	int k = 0, ans = -1;
	scanf("%d", &x);
	--x;
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < n; ++j)
		{
			int t;
			scanf("%d", &t);
			if (i == x)
				for (int z = 0; z < n; ++z)
					if (a[z] == t)
					{
						++k;
						ans = t;
					}
		}

	if (k == 1)
	{
		printf("%d\n", ans);
		return;
	}
	puts(k ? "Bad magician!" : "Volunteer cheated!");
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

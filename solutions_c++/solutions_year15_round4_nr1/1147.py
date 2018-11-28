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

#define f first
#define s second
#define mp make_pair
#define pb push_back
#define all(s) s.begin(), s.end()
#define sz(s) (int(s.size()))
#define fname "a"
#define ms(a,x) memset(a, x, sizeof(a))
#define forit(it,s) for(__typeof(s.begin()) it = s.begin(); it != s.end(); ++it)
#define MAXN 202

int n, m;
char s[MAXN][MAXN];
int r[MAXN];
int c[MAXN];

inline void solve()
{
	scanf("%d%d", &n, &m);
	for (int i = 0; i < n; ++i)
		scanf("%s", s[i]);

	int ans = 0;

	memset(r, 0, sizeof(r));
	memset(c, 0, sizeof(c));

	for (int i = 0; i < n; ++i)
		for (int j = 0; j < m; ++j)
		{
			if (s[i][j] == '.') continue;
			if (s[i][j] == '^' && !c[j]) ++ans;
			if (s[i][j] == '<' && !r[i]) ++ans;
			++r[i];
			++c[j];
		}

	for (int i = 0; i < n; ++i)
		for (int j = 0; j < m; ++j)
		{
			if (s[i][j] == '.') continue;
			if (r[i] == 1 && c[j] == 1)
			{
				puts("IMPOSSIBLE");
				return;
			}
		}

	memset(r, 0, sizeof(r));
	memset(c, 0, sizeof(c));

	for (int i = n - 1; i >= 0; --i)
		for (int j = m - 1; j >= 0; --j)
		{
			if (s[i][j] == '.') continue;
			if (s[i][j] == 'v' && !c[j]) ++ans;
			if (s[i][j] == '>' && !r[i]) ++ans;
			++r[i];
			++c[j];
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

#include <bits/stdc++.h>

using namespace std;

#define REP(i, a, b) for (int i = (a), _end_ = (b); i < _end_; ++i)
#define debug(...) fprintf(stderr, __VA_ARGS__)
#define mp make_pair
#define x first
#define y second
#define pb push_back
#define SZ(x) (int((x).size()))
#define ALL(x) (x).begin(), (x).end()

template<typename T> inline bool chkmin(T &a, const T &b) { return a > b ? a = b, 1 : 0; }
template<typename T> inline bool chkmax(T &a, const T &b) { return a < b ? a = b, 1 : 0; }

typedef long long LL;

const int oo = 0x3f3f3f3f;

const int maxn = 20000;

int main()
{
#ifdef matthew99
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	char s[maxn + 5];
	int T;
	scanf("%d", &T);
	for (int cc = 1; cc <= T; ++cc)
	{
		printf("Case #%d: ", cc);
		scanf("%s", s);
		int n = strlen(s);
		int ans = 0;
		static char stk[maxn + 5];
		int tot = 0;
		REP(i, 0, n)
		{
			if (tot && stk[tot - 1] == s[i]) --tot;
			else stk[tot++] = s[i];
		}
		ans = (n * 10 - tot * 5) >> 1;
		printf("%d\n", ans);
	}
	return 0;
}

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

const int maxl = 50;

int main()
{
#ifdef matthew99
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T;
	scanf("%d", &T);
	for (int cc = 1; cc <= T; ++cc)
	{
		printf("Case #%d: ", cc);
		int n, L;
		scanf("%d%d", &n, &L);
		static char s[maxl + 5];
		bool failed = 0;
		REP(i, 0, n)
		{
			scanf("%s", s);
			bool ok = 0;
			REP(j, 0, L) if (s[j] == '0') { ok = 1; break; }
			if (!ok) failed = 1;
		}
		scanf("%s", s);
		if (failed) printf("IMPOSSIBLE\n");
		else
		{
			if (L == 1)
			{
				printf("? 0\n");
			}
			else
			{
				printf("10?");
				REP(i, 3, 130) printf("%d", i & 1);
				printf(" ");
				REP(i, 0, L - 1) printf("?");
				printf("\n");
			}
		}
	}
	return 0;
}

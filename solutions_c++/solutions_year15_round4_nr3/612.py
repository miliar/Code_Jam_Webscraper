#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <cctype>
#include <cassert>
#include <map>

#define REP(i, a, b) for (int i = (a), _end_ = (b); i < _end_; ++i)
#define debug(...) fprintf(stderr, __VA_ARGS__)
#define EXIT(...) printf(__VA_ARGS__), exit(0)
#define pb push_back
#define SZ(x) (int((x).size()))
#define ALL(x) (x).begin(), (x).end()
#define foreach(e,x) for (__typeof(x.begin()) e=x.begin();e!=x.end();++e)
#define FOR(i,a,b) for (int i=(a);i<=(b);++i)

using namespace std;

const int oo = 0x3f3f3f3f;

const int maxn = 20, max0 = 3000;

bool belong[max0 + 5][2];

map<string, int> id;
int idn = 0;

vector<int> all[maxn + 5];

int get_id(char *s)
{
	string tmp;
	for (int i = 0; s[i]; ++i) tmp += s[i];
	if (!id.count(tmp)) id[tmp] = idn++;
	return id[tmp];
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i)
	{
		debug("%d\n", i);
		printf("Case #%d: ", i);
		int n;
		static char s[1000000];
		scanf("%d\n", &n);
		id.clear();
		idn = 0;
		REP(i, 0, n)
		{
			gets(s);
			all[i].clear();
			static char s0[10000];
			int s0n = 0;
			for (int j = 0; s[j]; ++j)
			{
				if (s[j] == ' ')
				{
					s0[s0n] = 0;
					all[i].pb(get_id(s0));
					s0n = 0;
				}
				else s0[s0n++] = s[j];
			}
			s0[s0n] = 0;
			all[i].pb(get_id(s0));
			s0n = 0;
		}
		int ans = oo;
		REP(i, 0, 1 << (n - 2))
		{
			REP(j, 0, idn) belong[j][0] = belong[j][1] = 0;
			REP(j, 0, 2)
				for (auto it : all[j]) belong[it][j] = 1;
			REP(j, 2, n)
				for (auto it : all[j]) belong[it][i >> (j - 2) & 1] = 1;
			int tmp = 0;
			REP(i, 0, idn)
				if (belong[i][0] && belong[i][1]) ++tmp;
			ans = min(ans, tmp);
		}
		printf("%d\n", ans);
	}
	return 0;
}

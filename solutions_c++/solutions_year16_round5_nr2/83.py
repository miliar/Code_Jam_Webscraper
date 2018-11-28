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

const int try_cnt = 25000;

const int maxn = 110;
const int maxm = 5;
const int maxl = 20;

int fa[maxn + 5];

vector<int> adj[maxn + 5];

vector<int> rt;

int n, m;

char s[maxn + 5];

int sz[maxn + 5];

inline void get_nxt(char *a, int n, int *nxt)
{
	int i = 1, j = 0;
	while (i < n)
	{
		while (j && a[i] != a[j]) j = nxt[j];
		if (a[i] == a[j]) ++j;
		++i;
		nxt[i] = j;
	}
}

static char qs[maxm + 5][maxl + 5];
static int nxt[maxl + 5];
static int cnt[maxm + 5];

char cur[maxn + 5];

void pre_dfs(int x) { sz[x] = 1; for (auto y : adj[x]) pre_dfs(y), sz[x] += sz[y]; }

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
		debug("%d\n", cc);
		printf("Case #%d: ", cc);
		scanf("%d", &n);
		REP(i, 0, n) adj[i].clear();
		rt.clear();
		REP(i, 0, n)
		{
			scanf("%d", fa + i), --fa[i];
			if (~fa[i]) adj[fa[i]].pb(i);
			else rt.pb(i);
		}
		for (auto u : rt) pre_dfs(u);
		scanf("%s", s);
		scanf("%d", &m);
		REP(i, 0, m) scanf("%s", qs[i]), cnt[i] = 0;
		REP(_t, 0, try_cnt)
		{
			vector<int> now(rt);
			REP(i, 0, n)
			{
				int p = rand() % (n - i);
				int sum = 0;
				int x = -1;
				REP(j, 0, SZ(now))
				{
					sum += sz[now[j]];
					if (sum > p)
					{
						x = j;
						break;
					}
				}
				assert(~x);
				int tmp = now[x];
				swap(now[x], now[SZ(now) - 1]);
				now.pop_back();
				cur[i] = s[tmp];
				for (auto y : adj[tmp]) now.pb(y);
			}
			REP(i, 0, m)
			{
				int l = strlen(qs[i]);
				get_nxt(qs[i], l, nxt);
				int k = 0;
				REP(j, 0, n)
				{
					while (k && qs[i][k] != cur[j]) k = nxt[k]; 
					k += qs[i][k] == cur[j];
					if (k == l)
					{
						++cnt[i];
						break;
					}
				}
			}
		}
		REP(i, 0, m) printf("%f ", (double)cnt[i] / try_cnt);
		printf("\n");
	}
	return 0;
}

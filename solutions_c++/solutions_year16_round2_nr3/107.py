#include <bits/stdc++.h>
#define rep(i, a, b) for (int i = (a); i <= (b); ++i)
#define drep(i, a, b) for (int i = (a); i >= (b); --i)
#define REP(i, a, b) for (int i = (a); i < (b); ++i)
#define pb(x) push_back(x)
#define mp(x, y) (make_pair(x, y))
#define clr(x) memset(x, 0, sizeof(x))
#define xx first
#define yy second

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
const int inf = ~0U >> 1;
const ll INF = ~0ULL >> 1;
template <class T> inline void read(T &n)
{
    char c; int flag = 1;
    for (c = getchar(); !(c >= '0' && c <= '9' || c == '-'); c = getchar()); if (c == '-') flag = -1, n = 0; else n = c - '0';
    for (c = getchar(); c >= '0' && c <= '9'; c = getchar()) n = n * 10 + c - '0'; n *= flag;
}
//***************************

string s1[2000], s2[2000];
map<string, int> hl, hr;
int n, cl, cr, x[2000], y[2000], vis[3000], lk[3000], visx[3000], visy[3000];
vector<int> E[3000];

int dfs(int u)
{
	for (auto v:E[u])
		if (!vis[v])
		{
			vis[v] = true;
			if (!lk[v] || dfs(lk[v]))
			{
				lk[v] = u;
				return true;
			}
		}
	return false;
}

int work()
{
	int ans = 0;
	hl.clear(); hr.clear();
	cl = cr = 0;
	scanf("%d", &n);
	rep(i, 1, n) E[i].clear();
	rep(i, 1, n)
	{
		cin >> s1[i] >> s2[i];
		if (!hl[s1[i]]) hl[s1[i]] = ++cl;
		if (!hr[s2[i]]) hr[s2[i]] = ++cr;
		x[i] = hl[s1[i]]; y[i] = hr[s2[i]];
		E[x[i]].pb(y[i]);
	}
	clr(lk);
	rep(i, 1, cl)
	{
		clr(vis);
		ans += dfs(i);
	}
	return n - (cl + cr - ans);
}

int main(int argc, char *argv[])
{
	int cases;
	scanf("%d", &cases);
	rep(_, 1, cases)
		printf("Case #%d: %d\n", _, work());
	return 0;
}

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

int working[100], taken[100], valid, N, best;
char can[100][100];

void Dfs(int cur)
{
	if (cur == N + 1) return;
	rep(i, 1, N)
		if (!working[i])
		{
			int flag = false;
			rep(j, 1, N)
				if (can[i][j] && !taken[j])
				{
					flag = true;
					working[i] = true;
					taken[j] = true;
					Dfs(cur + 1);
					working[i] = false;
					taken[j] = false;
				}
			if (!flag) valid = false;
		}
}

void dfs(int x, int y, int cost)
{
	if (x == N + 1)
	{
		valid = true;
		Dfs(1);
		if (valid) best = min(best, cost);
		return;
	}
	if (y == N) dfs(x + 1, 1, cost);
	else dfs(x, y + 1, cost);
	if (!can[x][y])
	{
		can[x][y] = true;
		if (y == N) dfs(x + 1, 1, cost + 1);
		else dfs(x, y + 1, cost + 1);		
		can[x][y] = false;	
	}
}

int solve()
{
	scanf("%d", &N);
	rep(i, 1, N) 
	{
		scanf("%s", can[i] + 1);
		rep(j, 1, N) can[i][j] -= '0';
	}
	best = inf;
	dfs(1, 1, 0);
	return best;
}

int main(int argc, char *argv[])
{
	int cases;
	scanf("%d", &cases);
	rep(_, 1, cases)
		printf("Case #%d: %d\n", _, solve());
	return 0;
}

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

int N, M, cnt, lover[100], tmp_lover[100], dir[100][100], e[20][20][20][20], f[1000], id[1000];

int find(int x)
{
	return (f[x] == x) ? x : (f[x] = find(f[x]));
}

void link(int x, int y)
{
	f[find(x)] = find(y);
}

void solve()
{
	scanf("%d%d", &N, &M);
	rep(i, 1, 2 * (N + M)) scanf("%d", &tmp_lover[i]);
	rep(i, 1, N + M)
	{
		int x = tmp_lover[i * 2 - 1];
		int y = tmp_lover[i * 2];
		lover[x] = y;
		lover[y] = x;
	}
	cnt = 0;
	rep(i, 0, N) rep(j, 0, M)
	{
		if (j + 1 <= M) e[i][j][i][j + 1] = ++cnt;
		if (i + 1 <= N) e[i][j][i + 1][j] = ++cnt;
	}
	rep(i, 1, M) id[i] = e[0][i - 1][0][i];
	rep(i, 1, N) id[i + M] = e[i - 1][M][i][M];
	rep(i, 1, M) id[2 * M + N - i + 1] = e[N][i - 1][N][i];
	rep(i, 1, N) id[2 * M + 2 * N - i + 1] = e[i - 1][0][i][0];
	REP(mask, 0, 1 << (N * M))
	{
		rep(i, 1, cnt) f[i] = i;		
		rep(i, 1, N)
			rep(j, 1, M)
			{
				int id = (i - 1) * M + j;
				dir[i][j] = bool((1 << id - 1) & mask);
				if (!dir[i][j])
				{
					link(e[i - 1][j - 1][i - 1][j], e[i - 1][j - 1][i][j - 1]);
					link(e[i - 1][j][i][j], e[i][j - 1][i][j]);
				}
				else
				{
					link(e[i - 1][j - 1][i - 1][j], e[i - 1][j][i][j]);
					link(e[i - 1][j - 1][i][j - 1], e[i][j - 1][i][j]);					
				}
			}
		int valid = true;
		rep(i, 1, 2 * (N + M))
			rep(j, 1, 2 * (N + M))
				if (i != j)
					if (lover[i] == j)
					{
						if (find(id[i]) != find(id[j])) valid = false;
					}
					else
					{
						if (find(id[i]) == find(id[j])) valid = false;
					}
		if (valid) 
		{
			rep(i, 1, N) 
			{
				rep(j, 1, M)
					if (!dir[i][j]) putchar('/');
					else putchar('\\');
				puts("");
			}
			return;
		}
	}
	puts("IMPOSSIBLE");
}

int main(int argc, char *argv[])
{
	int cases;
	scanf("%d", &cases);
	rep(_, 1, cases)
	{
		printf("Case #%d:\n", _);
		solve();
	}
	return 0;
}

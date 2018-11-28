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

char C[1000], J[1000];
ll dp[100][3];
pair<ll, ll> sol[100][3];
int n, a[1000], b[1000];

pair<string, string> work()
{
	scanf("%s%s", C, J);
	n = strlen(C);
	REP(i, 0, n)
	{
		if (C[i] == '?') a[i + 1] = -1;
		else a[i + 1] = C[i] - '0';
		if (J[i] == '?') b[i + 1] = -1;
		else b[i + 1] = J[i] - '0';
	}
	rep(i, 0, n) rep(j, 0, 2) dp[i][j] = INF;
	dp[0][0] = 0;
	rep(i, 0, n - 1)
		rep(j, 0, 2)
			if (dp[i][j] < INF)
			{
				rep(x, 0, 9)
					rep(y, 0, 9)
					{
						if (a[i + 1] != -1 && a[i + 1] != x) continue;
						if (b[i + 1] != -1 && b[i + 1] != y) continue;
						int nxtj = j;
						if (j == 0)
						{
							if (x < y) nxtj = 1;
							else if (x > y) nxtj = 2;
						}
						ll nxt = dp[i][j];
						if (nxtj == 1) 
							nxt = nxt * 10 + (y - x);
						else
							nxt = nxt * 10 + (x - y);
						if (nxt < dp[i + 1][nxtj] 
						|| nxt == dp[i + 1][nxtj] && sol[i][j].xx * 10 + x < sol[i + 1][nxtj].xx
						|| nxt == dp[i + 1][nxtj] && sol[i][j].xx * 10 + x == sol[i + 1][nxtj].xx && sol[i][j].yy * 10 + y < sol[i + 1][nxtj].yy)
						{
							dp[i + 1][nxtj] = nxt;
							sol[i + 1][nxtj].xx = sol[i][j].xx * 10 + x;
							sol[i + 1][nxtj].yy = sol[i][j].yy * 10 + y;
						}
					}
			}
	ll finalDp = INF;
	pair<ll, ll> ans = mp(-1, -1);
	rep(j, 0, 2) 
		if (dp[n][j] < finalDp || dp[n][j] == finalDp && sol[n][j].xx < ans.xx || dp[n][j] == finalDp && sol[n][j].xx == ans.xx && sol[n][j].yy < ans.yy)
		{
			finalDp = dp[n][j];
			ans = sol[n][j];
		}
	pair<string, string> Ans = mp(to_string(ans.xx), to_string(ans.yy));
	while (Ans.xx.size() < n) Ans.xx = "0" + Ans.xx;
	while (Ans.yy.size() < n) Ans.yy = "0" + Ans.yy;
	return Ans;
}

int main(int argc, char *argv[])
{
	int cases;
	scanf("%d", &cases);
	rep(_, 1, cases)
	{
		pair<string, string> res = work();
		printf("Case #%d: %s %s\n", _, res.xx.c_str(), res.yy.c_str());
	}
	return 0;
}

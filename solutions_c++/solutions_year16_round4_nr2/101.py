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

double pp[500], p[500], dp[500][500];
int N, K, id[500];

bool cmp(const int &a, const int &b)
{
	return p[a] < p[b];
}

double solve()
{
	double best = 0;
	rep(i, 1, N) id[i] = i;
	sort(id + 1, id + N + 1, cmp);
	rep(i, 0, K)
	{
		int cnt = 0;
		rep(j, 1, i) pp[++cnt] = p[id[j]];
		rep(j, N - (K - i) + 1, N) pp[++cnt] = p[id[j]];	
		clr(dp);
		dp[0][0] = 1;
		rep(i, 0, K - 1)
			rep(j, 0, K / 2)			
			{
				dp[i + 1][j] += dp[i][j] * (1. - pp[i + 1]);
				dp[i + 1][j + 1] += dp[i][j] * pp[i + 1];
			}
		if (dp[K][K / 2] > best)
			best = dp[K][K / 2];
	}
	return best;
	/*double best = 0;
	int opt = 0;
	REP(mask, 0, 1 << N)
	{
		int cnt = 0;
		rep(i, 1, N)
			if ((1 << i - 1) & mask) pp[++cnt] = p[i];
		if (cnt != K) continue;
		clr(dp);
		dp[0][0] = 1;
		rep(i, 0, K - 1)
			rep(j, 0, K / 2)			
			{
				dp[i + 1][j] += dp[i][j] * (1. - pp[i + 1]);
				dp[i + 1][j + 1] += dp[i][j] * pp[i + 1];
			}
		if (dp[K][K / 2] > best)
			best = dp[K][K / 2], opt = mask;
	}
	rep(i, 1, N)
		cerr << (bool)((1 << i - 1) & opt) << ' ';
	cerr<<endl;
	return best;*/
}

int main(int argc, char *argv[])
{
	int cases;
	scanf("%d", &cases);
	rep(_, 1, cases)
	{
		scanf("%d%d", &N, &K);
		rep(i, 1, N) scanf("%lf", &p[i]);
		printf("Case #%d: %.10lf\n", _, solve());
	}
	return 0;
}

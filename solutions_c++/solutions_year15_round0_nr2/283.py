/*
    Author: Zhouxing Shi
    Created on Apr11, 2014
*/
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
typedef pair<int, int> pii;
const int inf = ~0U >> 1;
const ll INF = ~0ULL >> 1;

//***************************

int N, a[10000];

int solve()
{
	int ans = inf;
	scanf("%d", &N);
	rep(i, 1, N) scanf("%d", &a[i]);
	rep(i, 1, 1200)
	{
		int t = 0;
		rep(j, 1, N) 
			if (a[j] > i) 
				t += (a[j] - i) / i + bool((a[j] - i) % i);
		ans = min(ans, i + t);
	}
	return ans;
}

int main()
{
	int cases;
	scanf("%d", &cases);
	rep(_, 1, cases) printf("Case #%d: %d\n", _, solve());
    return 0;
}



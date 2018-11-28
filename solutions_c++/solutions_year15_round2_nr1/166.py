/*
    Author: Zhouxing Shi
    Created on May3, 2015
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

namespace subtask1
{
	
/*	int rev[2000000];
	int dp[1200000], N;
	*/
	ll Reverse(ll x) 
	{
		ll r = 0;
		while (x) r = r * 10 + x % 10, x /= 10;
		return r;
	}
/*	
	int work()
	{
		clr(dp);
		rep(i, 1, 1000000) rev[i] = Reverse(i);
		scanf("%d", &N);
		dp[1] = 1;
		rep(i, 2, N) 
		{
			dp[i] = inf;
			if (i % 10 && rev[i] < i) dp[i] = dp[rev[i]] + 1;
			dp[i] = min(dp[i], dp[i - 1] + 1);
		}
		
		return dp[N];
	}
	*/
	
	ll cost[100], d[100];
	
	ll solve(ll N)
	{
		if (N == 1) return 1;
		int m = 0;
		for (ll t = N; t; t /= 10) d[++m] = t % 10;
		if (m == 1) return N;
		if (!d[1]) return solve(N - 1) + 1;
		cost[1] = 1;
		rep(i, 2, m) cost[i] = cost[i - 1] * 10;
		ll ret = 0;
		rep(i, 1, m)
		{
			if (i == 1) 
			{
				if (d[i] > 1) ret += (d[i] - 1) * cost[i];
			}
			else if (i == m) ret += (d[i] - 1) * cost[i];
			else
			{
				ret += d[i] * cost[i];
			}
		}
		ll Ret = 1;
		if (!d[1]) Ret += solve(N - 1);
		else
		{
			rep(i, 1, m)
			{
				if (i == 1) 
				{
					if (d[i] > 1) Ret += (d[i] - 1) * cost[i];
				}
				else if (i == m) Ret += (d[i] - 1) * min(cost[i], cost[m - i + 1]);
				else
				{
					Ret += d[i] * min(cost[i], cost[m - i + 1]);
				}
			}
		}
		ll ans = min(Ret, ret);
		if (d[1]) ans++;
		ll nxt = 9;
		rep(i, 2, m - 1) nxt = nxt * 10 + 9;
		return ans + 1 + solve(nxt);
	}
	
	ll Work()
	{
		ll N;
		scanf("%lld", &N);
		return solve(N);
	}
	
	int main()
	{
		int cases;
		scanf("%d", &cases);
		rep(_, 1, cases) printf("Case #%d: %lld\n", _, Work()),cerr<<_<<endl;
	}
}

int main()
{
	subtask1::main();
	return 0;
}



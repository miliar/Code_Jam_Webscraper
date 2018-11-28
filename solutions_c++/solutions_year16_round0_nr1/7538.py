#include <bits/stdc++.h>

#define ft first
#define st second
#define mp make_pair
#define pb push_back
#define sz(n) int(n.size())


using namespace std;

typedef long long ll;
typedef pair<int,int> pii;

const int N = 1e5;
const int inf = 1e9 + 7;
const ll INF = 1e18 + 7;

bool u[15];
ll n, t;

void get(ll x)
{
	while (x)
	{
		ll p = x % 10;
		x /= 10;
		u[p] = true;
	}
}

bool check()
{
	for (int i = 0; i < 10; i ++) if (!u[i]) return false;
	return true;
}

int main ()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cin >> t;
	for (int q = 1; q <= t; q ++)
	{
		cin >> n;
		ll cur = n;
		if (n == 0)
		{
			printf("Case #%d: INSOMNIA\n", q);
			continue;
		}
		memset(u, false, sizeof u);
		while (true)
		{
			get(cur);
			if (check()) break;
			cur += n;
		}
		printf("Case #%d: %I64d\n", q, cur);
	}
}
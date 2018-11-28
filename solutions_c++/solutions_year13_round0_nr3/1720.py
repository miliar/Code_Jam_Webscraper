#include <iostream>
using namespace std;

typedef long long ll;

int p[20];
int ind = 0;
ll all[(int)1e7];

bool check(ll x)
{
	int u = 0;
	while (x)
	{	
		p[u++] = x % 10;
		x /= 10;
	}
	for (int i = 0; i < u; i++)
		if (p[i] != p[u - i - 1])
			return false;
	return true;
}

int main()
{
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt", "w", stdout);

	for (ll i = 1; i <= (ll)1e7; i++)
	{
		ll t = i * i;
		if (check(i) && check(t))
			all[ind++] = t;
	}                           

	int n;
	scanf("%d", &n);
	int cnt = 0;
	for (int i = 0; i < n; i++)
	{
		ll a, b;
		cnt = 0;
		scanf("%lld %lld", &a, &b);
		for (int s = 0; s < ind; s++)
			if (all[s] >= a && all[s] <= b)
				cnt++;
		printf("Case #%d: %d\n", i + 1, cnt);
	}

	return 0;
}
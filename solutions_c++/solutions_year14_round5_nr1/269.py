#include <cstdio>
using namespace std;

typedef long long ll;
const int max_n = 1048576;
int n; ll p, q, r, s;
ll a[max_n];

int main()
{
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		scanf("%d %lld %lld %lld %lld", &n, &p, &q, &r, &s);
		ll tot = 0LL;
		for(int i = 0; i < n; i++)
		{
			a[i] = (ll(i) * p + q) % r + s;
			tot += a[i];
		}
		ll lb = 0LL, ub = tot;
		while(lb < ub)
		{
			ll md = lb + (ub - lb) / 2LL;
			ll sum_l = 0LL;
			for(int i = 0;
				i < n && sum_l + a[i] <= md;
				sum_l += a[i], i++);
			ll sum_r = 0LL;
			for(int i = n - 1;
				i >= 0 && sum_r + a[i] <= md;
				sum_r += a[i], i--);
			if(tot - sum_l - sum_r <= md)
				ub = md;
			else
				lb = md + 1LL;
		}
		printf("Case #%d: %.10f\n", t, double(tot - lb) / double(tot));
	}
	return 0;
}

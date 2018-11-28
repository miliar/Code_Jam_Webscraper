#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main()
{
	int t, x;
	cin.tie(0);
	ios::sync_with_stdio(false);
	cin >> t;
	for (x = 1; x <= t;++x)
	{
		ll n;
		cin >> n;
		printf("Case #%d: ", x);
		ll a[10] = { 0 };
		ll i, j, k;
		if (n == 0)
			printf("INSOMNIA\n");
		else
		{
			for (i = 1; ; ++i)
			{
				j = i*n;
				while (j)
				{
					a[j % 10] = 1;
					j = j / 10;
				}
				int flag = 1;
				for (j = 0; j < 10; ++j)
				{
					if (!a[j])
					{
						flag = 0;
						break;
					}
				}
				if (flag)
				{
					printf("%lld\n", n);
					break;
				}
			}
		}
	}
	return 0;
}
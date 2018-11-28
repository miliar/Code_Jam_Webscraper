#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int main()
{
	ll t, n, i, res, temp;
	set<ll> s;
	scanf("%lld", &t);
	for (i = 1; i <= t; ++i)
	{
		scanf("%lld", &n);
		s.clear();
		if (n == 0)
		{
			printf("Case #%lld: INSOMNIA\n", i);
			continue;
		}
		for (res = n; ; res += n)
		{
			temp = res;
			while (temp > 0)
			{
				if (s.find(temp%10) == s.end())
					s.insert(temp%10);
				temp /= 10;
				// cout << temp << endl;
			}
			if (s.size() == 10)
				break;
			// cout << s.size() << endl;
		}
		printf("Case #%lld: %lld\n", i, res);
	}
	return 0;
}
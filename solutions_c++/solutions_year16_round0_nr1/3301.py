#include <bits/stdc++.h>
using namespace std;

bool found[10];
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, it;
	long long n;
	scanf("%d", &t);
	for (int tt = 1;tt <= t;tt++)
	{
		scanf("%lld", &n);
		for (it = 1;it <= 1000000;it++)
		{
			long long temp = long long(it)*n;
			while (temp)
			{
				int rem = temp % 10;
				found[rem] = 1;
				temp /= 10;
			}
			bool ok = 1;
			for (int j = 0;j <= 9;j++)
				if (!found[j])
					ok = 0;
			if (ok)
				break;
		}
		bool ok = 1;
		for (int i = 0;i <= 9;i++)
		{
			if (!found[i])
				ok = 0;
			found[i] = 0;
		}
		printf("Case #%d: ", tt);
		if (ok)
			printf("%lld\n", long long(it)*n);
		else
			puts("INSOMNIA");
	}
	return 0;
}
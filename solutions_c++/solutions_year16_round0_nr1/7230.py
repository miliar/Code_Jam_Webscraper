#include<bits/stdc++.h>

using namespace std;

int main()
{
	int t, n, f, done;
	long long ans;

	scanf("%d", &t);

	for(int x = 1; x <= t; x++)
	{
		done = 0;	f = 1;

		scanf("%d", &n);

		if(n == 0)
		{
			printf("Case #%d: INSOMNIA\n", x);
			continue;
		}

		int d[10];

		for(int i = 0; i < 10; i++)
			d[i] = 0;

		while(!done)
		{
			ans = 1LL*f*n;
			f++;

			long long temp = ans;

			while(temp > 0)
			{
				d[temp%10] = 1;
				temp /= 10;
			}

			done = 1;
			for(int i = 0; i < 10; i++)
			{
				if(!d[i])
				{
					done = 0;
					break;
				}
			}
		}

		printf("Case #%d: %lld\n", x, ans);
	}

	return 0;
}
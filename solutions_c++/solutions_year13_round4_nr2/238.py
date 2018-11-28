#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
//*
    freopen(".in", "r", stdin);
    freopen(".out", "w", stdout);
//*/
	int T;
	scanf("%d", &T);
	
	for (int t = 1; t <= T; t++, printf("\n"))
	{
		printf("Case #%d: ", t);
		long long n, p;
		cin >> n >> p;
		p -= 1;
		long long l, r, c;
		
		l = 0;
		r = (1LL << n) - 1;
		while (l < r)
		{
			c = (l + r + 1) / 2;
			long long k = c;
			for (int i = 0; i < n; i++)
			{
				if (((1LL << (n - i - 1)) & p) == 0)
				{
					if (k > 0)
						break;
					else
						continue;
				}
				
				k -= 1;
				if (k < 0)
					break;
				k /= 2;
			}
			
			if (k <= 0)
				l = c;
			else
				r = c - 1;
		}
		cout << l << " ";

		l = 0;
		r = (1LL << n) - 1;
		while (l < r)
		{
			c = (l + r + 1) / 2;
			long long k = (1LL << n) - c - 1;
			for (int i = 0; i < n; i++)
			{
				if ((1LL << (n - i - 1)) & p)
				{
					if (k > 0)
						break;
					else
						continue;
				}
				
				k -= 1;
				if (k < 0)
					break;
				k /= 2;
			}
			if (k >= 0)
				l = c;
			else
				r = c - 1;
		}
		cout << l;
	}	
    return 0;
}

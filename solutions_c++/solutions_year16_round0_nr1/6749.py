#include <iostream>
#include <vector>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <list>
#include <map>
#include <functional>
#include <algorithm>

using namespace std;

int main()
{
	int t;

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);


	scanf("%d", &t);
	
	for (int z = 0;z < t;z++)
	{
		unsigned long long n,p;
		printf("Case #%d: ", z + 1);
		scanf("%llu", &n);
		
		p = n;
		if (n == 0)
			printf("INSOMNIA");
		else
		{
			unsigned long long m = 0;
			while (1)
			{
				unsigned long long tmp = n;
				while (tmp)
				{
					int d = tmp % 10;
					m |= 1u << d;
					tmp /= 10;
				}
				if (m == 1023)
				{
					break;
				}
				n += p;
			}
			printf("%llu", n);
		}
		printf("\n");
	}
	return 0;
}
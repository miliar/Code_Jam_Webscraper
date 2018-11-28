#include <stdio.h>
#include <vector>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <queue>
#include <iostream>
#include <map>
#include <iostream>
#include <set>
#include <string>
#include <queue>
#define ll long long int
#define s(x) scanf("%d",&x)
#define p(x) printf("%d ",x)

using namespace std;
int main()
{

	int t, i, tt;
	s(t);
	for( tt = 1; tt <= t; tt++)
	{
		printf("Case #%d: ", tt);
		int n, all = 10, d;
		ll s = 0, tmp;
		s(n);
		int digit[10];

		for( i = 0 ; i < 10; i++)
			digit[i] = 0;
		
		if(n != 0)
		{
			while(all != 0)
			{
				s += n;
				tmp = s;
				while(tmp)
				{
					d = tmp % 10;
					if(digit[d] == 0)
					{
						digit[d] ++;
						all --;
					}
					tmp /= 10;		
				}

			}
			printf("%lld\n",s );
		}
		else
			printf("INSOMNIA\n");
	}
	return 0;
}
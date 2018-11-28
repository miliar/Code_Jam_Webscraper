#include <stdio.h>
#include <string.h>
#include <string>
#include <iostream>
#include <algorithm>
#include <math.h>
using namespace std;


int main ()
{
	freopen ("in.txt","r",stdin);
	freopen ("out.txt","w",stdout);
	int n,c=1;
	scanf ("%d",&n);
	
	while (n--)
	{
		long long r,t;

		scanf ("%lld %lld",&r,&t);

		double k,R,T;
		R = r,T = t;
		double one = (double)(1);
		double two = (double)(2);
		double four = (double)(4);
		long long ret;
		long long hi = min(1000000000LL,t/(2LL*r-1LL));
		long long lo = 0;
		long long mid;
		while (lo<=hi)
		{
			mid = (lo+hi)/2;
			long long cur = mid*mid*2LL + (2LL*r-1LL)*mid;
			if (cur > t)
			{
				hi = mid - 1;
				continue;
			}
			ret = mid;
			lo = mid + 1;
		}
		/*k = (one-two*R)/two + sqrt ((two*R-1)*(two*R-1)/four+two*T);
		cout << k << endl;
		k /= two;
		cout << k << endl;
		k += 1e-9;
		cout << k << endl;*/
		printf ("Case #%d: %lld\n",c++,ret);
	}

	return 0;
}

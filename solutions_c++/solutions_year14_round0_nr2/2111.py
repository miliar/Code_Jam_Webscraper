/* bhupkas */

using namespace std;

#include "bits/stdc++.h"

#define EPS 1e-9

int main()
{
	int t;
	cin >> t;
	for(int tc = 1 ; tc <= t ; ++tc)
	{
		double c,f,x;
		scanf("%lf %lf %lf",&c,&f,&x);
		double re = 0.0;
		double curr = 2.0;
		long long cnt = 0;
		while(1)
		{	
			if((x/curr + EPS) < (c/curr + x/(curr + f)))	break;
			curr += f;
			cnt++;
		}
		curr = 2.0;
		for(int i = 0 ; i < cnt ; ++i)
		{
			re += c/curr;
			curr += f;
		}
		re += x/curr;
		printf("Case #%d: %0.12lf\n",tc,re);
	}
	return 0;
}

#include <iostream>
#include <algorithm>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;
int main()
{
	int t,i;
    freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>t;
	for( i=1;i<=t;i++ )
        {
		double c,r,x,timebyc,b,rate,check,sum;
		cin>>c>>r>>x;
		rate = 2;
		sum = x/rate;
		check = 0;
		while(1){
			check+= c/rate;
			rate=rate+r;
			timebyc = x/rate;
			if(sum>check+timebyc)
			sum = check+timebyc;
			else
			break;
		}
		printf("Case #%d: %0.7lf\n",i,sum);
	}
	return 0;
}

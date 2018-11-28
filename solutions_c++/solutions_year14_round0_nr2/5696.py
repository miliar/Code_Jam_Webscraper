#include <iostream>
#include <string.h>
#include <stdio.h>

#define dis 0.00000001
using namespace std;



int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);

    double C,F,X,ans,now,op;
    int T;
	scanf("%d",&T);
	for ( int kase = 1; kase <= T; ++kase )
	{
		scanf("%lf%lf%lf",&C,&F,&X);
		op = 2.0;
		ans = X/op;
		now = 0;
		while ( 1 )
		{
			ans = min(ans,now+X/op);
			now += ( C / op );
			op += F;
			if (  ans - (now + X / op ) < dis) break;
		}
		printf("Case #%d: %0.7lf\n",kase,ans);
	}
	return 0;
}

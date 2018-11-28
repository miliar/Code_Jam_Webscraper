#include<bits/stdc++.h>
using namespace std;

main()
{
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
	int t,C=1;
	scanf("%d",&t);
	while(t--)
	{
	    double c,f,x,rate=2.0,time=0.0;
	    scanf("%lf%lf%lf",&c,&f,&x);
        while((c/rate)+(x/(rate+f))<x/rate){
            time+=(double)c/(double)rate;
            rate+=f;
        }
        time+=(double)(x/rate);
	    printf("Case #%d: %.7lf\n",C++,time);
	}
}

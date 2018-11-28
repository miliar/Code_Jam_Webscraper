#include<iostream>
#include<stdio.h>

using namespace std;

#define D double

int main()
{
    int T;
    int cas=1;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&T);
    while(T--)
    {
        D C,F,X;
        scanf("%lf%lf%lf",&C,&F,&X);
        D ans=X/2.0;

        D rate=2.0;
        D curr=0.0;
        D temp1=0.0,temp=0.0;
        D tot=0.0;
        while(tot+(X/rate) <= ans) {
                temp1=X/rate;
                ans=(D)min(ans,tot+temp1);
                temp=C/rate;
                tot += temp;
                rate+=F;
        }

        printf("Case #%d: %.7lf\n",cas,ans);
        cas++;
    }
    return 0;
}

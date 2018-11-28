#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t,i;
    scanf("%d",&t);
    double c,f,x,res=0.0,r=2.0;
    for(i=1;i<=t;i++)
    {
        res=0.0;
        r=2.0;
        scanf("%lf %lf %lf",&c,&f,&x);
        while((c/r+(x/(r+f)))<x/r)
        {
            res+=c/r;
            r+=f;
        }
        res+=x/r;
        printf("Case #%d: %.7lf\n",i,res);
    }
    return 0;
}

#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cmath>
using namespace std;
int main()
{
    //freopen("input.in","r",stdin);
    //freopen("output.txt","w",stdout);
    int t,k=1;
    scanf("%d",&t);
    while(t--)
    {
        double c,f,x,i,ans,p,q,r,s,ans2,tmp;
        ans=10000000.0;
        scanf("%lf%lf%lf",&c,&f,&x);
        i=2.0;r=0.0;
        while(1)
        {
            p=c/i;
            q=x/i;
            q+=r;
            r+=p;
            tmp=(i+f);
            s=r+(x/tmp);
            ans2=min(q,s);
            if(ans>ans2)
            {
                i+=f;
                ans=ans2;
            }
            else break;
        }
        printf("Case #%d: %.7lf\n",k,ans);
        k++;
    }
    return 0;
}

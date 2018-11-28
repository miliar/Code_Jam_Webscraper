#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int main()
{
    freopen("t.in","r",stdin);
    freopen("t.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int cc=0;cc<t;cc++)
    {
        int n;
        double v,x,v1=0,x1=0,v2=0,x2=0,ve=0;
        double r[111],c[111];
        double ans=-10;
        scanf("%d%lf%lf",&n,&v,&x);
        for(int i=0;i<n;i++)
        {
            scanf("%lf%lf",&r[i],&c[i]);
            if(c[i]<x)
            {
                v1+=r[i];
                x1+=c[i]*r[i];
            }
            else if(c[i]>x)
            {
                v2+=r[i];
                x2+=c[i]*r[i];
            }
            else
            {
                ve+=r[i];
            }
        }
        if(v1>0)
            x1/=v1;
        if(v2>0)
            x2/=v2;
        if(v1==0||v2==0)
        {
            if(ve>0)
                ans=v/ve;
        }
        else
        {
            double l=0,r=1e10,mid;
            while(l+1e-8<r)
            {
                mid = (l+r)/2;
                if(mid*ve>=v)
                {
                    r=mid;
                    continue;
                }

                double t2=(v-mid*ve)*(x-x1)/(v2*(x2-x1)),t1=(v-mid*ve)*(x-x2)/(v1*(x1-x2));
                if(max(t2,t1)<mid)
                    r=mid;
                else
                    l=mid;

            }
            ans=r;
        }
        if(ans<-1)
            printf("Case #%d: IMPOSSIBLE\n",cc+1);
        else
            printf("Case #%d: %.8lf\n",cc+1,ans);

    }
    return 0;
}

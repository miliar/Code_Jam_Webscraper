#include<bits/stdc++.h>
using namespace std;


int main()
{
    freopen("2inp.in","r",stdin);
    freopen("2out.txt","w",stdout);
    int i,j,k,l,n,m,T,t;
    double v,x,r[10],c[10];
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        scanf("%d %lf %lf",&n,&v,&x);
        for(i=0; i<n; i++)
            scanf("%lf %lf",&r[i],&c[i]);

        double ans,v0,v1;
        ans=1000000000000.00;
        if(n==1)
        {
            if(c[0]==x)
            {
                ans=v/r[0];
                printf("Case #%d: %.9lf\n",t,ans);
                continue;
            }
            else
            {
                printf("Case #%d: IMPOSSIBLE\n",t);
                continue;
            }
        }
        else
        {
            if(c[0]==c[1])
            {
                if(c[0]!=x)
                {
                    printf("Case #%d: IMPOSSIBLE\n",t);
                    continue;
                }
                else
                {

                    ans=v/r[0];
                    ans=min(ans,v/r[1]);
                    ans=min(ans,v/(r[0]+r[1]));
                    printf("Case #%d: %.9lf\n",t,ans);
                    continue;
                }
            }
            if(c[0]==x)
                ans=v/r[0];
            if(c[1]==x)
                ans=min(ans,v/r[1]);
            v0=(v*(x-c[1]))/(c[0]-c[1]);
            if(v0<0)
            {
                printf("Case #%d: IMPOSSIBLE\n",t);
                continue;
            }
            v1=(v*(c[0]-x))/(c[0]-c[1]);
            if(v1<0)
            {
                printf("Case #%d: IMPOSSIBLE\n",t);
                continue;
            }
            ans=min(ans,max((v0/r[0]),(v1/r[1])));
            printf("Case #%d: %.9lf\n",t,ans);

        }
    }
    return 0;
}


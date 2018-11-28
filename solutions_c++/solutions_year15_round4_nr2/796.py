#include<bits/stdc++.h>
using namespace std;
#define mp make_pair
#define pb push_back
#define f first
#define s second
#define ll long long
#define mod 1000000007LL
#define pii pair<int,int>
#define pll pair<ll,ll>
#define vi vector<int>
#define vpii vector< pii >
int main()
{
    freopen("inp.in","r",stdin);
    freopen("out2.txt","w",stdout);
    int i,j,k,l,n,m,t1,c=1;
    double v,t2,r[10],t[10];
    scanf("%d",&t1);
    while(t1--)
    {
        scanf("%d %lf %lf",&n,&v,&t2);
        for(i=0; i<n; i++)
            scanf("%lf %lf",&r[i],&t[i]);

//        printf("%d\n",n);
//        for(i=0;i<n;i++)
//            printf("%d ",a[i]);
//        printf("\n");

        double ans,v0,v1;
        ans=1000000000000.00;
        if(n==1)
        {
            if(t[0]==t2)
            {
                ans=v/r[0];
                printf("Case #%d: %.9lf\n",c,ans);
                c++;
                continue;
            }
            else
            {
                printf("Case #%d: IMPOSSIBLE\n",c);
                c++;
                continue;
            }
        }
        else
        {
            if(t[0]==t[1])
            {
                if(t[0]!=t2)
                {
                    printf("Case #%d: IMPOSSIBLE\n",c);
                    c++;
                    continue;
                }
                else
                {

                    ans=v/r[0];
                    ans=min(ans,v/r[1]);
                    ans=min(ans,v/(r[0]+r[1]));
                    printf("Case #%d: %.9lf\n",c,ans);
                    c++;
                    continue;
                }
            }
            if(t[0]==t2)
                ans=v/r[0];
            if(t[1]==t2)
                ans=min(ans,v/r[1]);
            v0=(v*(t2-t[1]))/(t[0]-t[1]);
            if(v0<0)
            {
                printf("Case #%d: IMPOSSIBLE\n",c);
                c++;
                continue;
            }
            v1=(v*(t[0]-t2))/(t[0]-t[1]);
            if(v1<0)
            {
                printf("Case #%d: IMPOSSIBLE\n",c);
                c++;
                continue;
            }
            ans=min(ans,max((v0/r[0]),(v1/r[1])));
            printf("Case #%d: %.9lf\n",c,ans);
            c++;

        }
    }
    return 0;
}


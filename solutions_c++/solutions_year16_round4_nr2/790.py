#include<bits/stdc++.h>
using namespace std;
#define f first
#define s second
#define mp make_pair
#define pb push_back
#define pii pair<int,int>
#define ll long long
#define pli pair<ll,int>
#define pil pair<int,ll>
#define pll pair<ll,ll>
#define all(v) v.begin(),v.end()
#define inf 1000000000
double a[100011],p1[100011];
int main()
{
    freopen("2.in","r",stdin);
    freopen("2-out.txt","w",stdout);
    int t,cs=1;
    scanf("%d",&t);
    while(t--)
    {
        int n,i,j,k,k1;
        double ans=0.0;
        scanf("%d %d",&n,&k1);
        for(i=0;i<n;i++)
            scanf("%lf",&a[i]);
        for(i=0;i<(1<<n);i++)
        {
            if(__builtin_popcount(i)!=k1)
                continue;
            for(j=0;j<=n;j++)
                p1[j]=0.0;
            p1[0]=1.0;
            for(j=0;j<n;j++)
            {
                if(((i>>j)&1)==0)
                    continue;
                for(k=n;k>=0;k--)
                    if(k!=0)
                        p1[k]=(p1[k]*(1.0-a[j])+p1[k-1]*a[j]);
                    else
                        p1[k]=(p1[k]*(1.0-a[j]));
            }
//            cout<<i<<endl;
//            for(j=0;j<=n;j++)
//                printf("%lf ",p1[j]);
//            printf("\n");
            ans=max(ans,p1[k1/2]);
        }
        printf("Case #%d: %.9lf\n",cs,ans);
        cs++;
    }
    return 0;
}


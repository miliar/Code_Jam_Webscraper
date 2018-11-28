#include<bits/stdc++.h>
using namespace std;

double f[300][300],p[300];

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B_l.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int tcnt=1;tcnt<=T;tcnt++)
    {
        int n,K;
        scanf("%d%d",&n,&K);
        for(int i=0;i<n;i++)
            scanf("%lf",p+i);
        sort(p,p+n);
        double ans=0;
        vector<double>v;
        for(int tt=0;tt<=K;tt++)
        {
            v.clear();
            for(int i=0;i<tt;i++)
                v.push_back(p[i]);
            for(int i=0,j=n-1;i<K-tt;i++,j--)
                v.push_back(p[j]);
            memset(f,0,sizeof(f));
            f[0][0]=1;
            for(int i=0;i<K;i++)
                for(int j=0;j<K;j++)
                {
                    f[i+1][j+1]+=f[i][j]*v[i];
                    f[i+1][j]+=f[i][j]*(1-v[i]);
                }
            ans=max(ans,f[K][K/2]);
        }
        printf("Case #%d: %.20f\n",tcnt,ans);
    }
    return 0;
}

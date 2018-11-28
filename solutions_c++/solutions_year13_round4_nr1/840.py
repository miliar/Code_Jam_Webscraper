#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;

const int mod=1000002013;
long long cnt[1111];
int n,m,t;
pair<int,int> p[2222];

long long calc(int a,int b)
{
    int len=b-a;
    long long res=(long long)(len+1)*(n+n-len)/2;
    return res%mod;
}

int main()
{
    scanf("%d",&t);
    for (int id=1;id<=t;id++)
    {
        memset(cnt,0,sizeof(cnt));
        int tot=0;

        scanf("%d%d",&n,&m);
        long long resa=0;
        for (int i=0;i<m;i++) 
        {
            int x,y,z;
            scanf("%d%d%d",&x,&y,&z);
            resa+=(long long)z%mod*calc(x,y)%mod;
            resa%=mod;
            p[tot++]=make_pair(x,-z);
            p[tot++]=make_pair(y,z);
        }
        sort(p,p+tot);
        long long resb=0;
        for (int i=0;i<tot;i++)
        if (p[i].second<0)
        {
           cnt[p[i].first]-=p[i].second;
        } else
        {
            for (int j=p[i].first;p[i].second;j--)
            if (cnt[j])
            {
                long long k=min(cnt[j],(long long)p[i].second);
                p[i].second-=k;
                resb+=k%mod*calc(j,p[i].first)%mod;
                resb%=mod;
                cnt[j]-=k;
            }
        }
        printf("Case #%d: %lld\n",id,(resa-resb+mod)%mod);
    }
}

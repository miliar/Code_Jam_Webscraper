#include <stdio.h>
#include <algorithm>
#include <map>
#define MAX 2003
#define MOD 1000002013LL

typedef long long ll;

using namespace std;

struct s
{
    ll x,tot,tp;
};

s pnt[MAX];
ll ase[MAX];
map<ll,ll> mp;

bool cmp(s a,s b)
{
    if (a.x!=b.x) return a.x<b.x;
    return a.tp>b.tp;
}

int main()
{
    freopen("ain.txt","r",stdin);
    freopen("aout.txt","w",stdout);
    ll test,cas,n,m,cnt,ans,i,a,b,c,c1,j,p,m1;
    scanf("%lld",&test);
    for (cas=1;cas<=test;cas++)
    {
        scanf("%lld%lld",&n,&m);
        cnt=0;
        ans=0;
        for (i=0;i<m;i++)
        {
            scanf("%lld%lld%lld",&a,&b,&c);
            pnt[cnt].x=a;
            pnt[cnt].tot=c;
            pnt[cnt++].tp=1;
            pnt[cnt].x=b;
            pnt[cnt].tot=c;
            pnt[cnt++].tp=-1;
            m1=((b-a)*(b-a-1))/2;
            m1%=MOD;
            ans=((ans-m1*c)%MOD+MOD)%MOD;
        }
        sort(pnt,pnt+cnt,cmp);
        c1=0;
        for (i=0;i<cnt;i++)
        {
            if (pnt[i].tp==1)
            {
                if (!mp[pnt[i].x]) ase[c1++]=pnt[i].x;
                mp[pnt[i].x]+=pnt[i].tot;
            }
            else
            {
                j=pnt[i].tot;
                while (j)
                {
                    p=min(j,mp[ase[c1-1]]);
                    m1=((pnt[i].x-ase[c1-1])*(pnt[i].x-ase[c1-1]-1))/2;
                    m1%=MOD;
                    ans=(ans+m1*p)%MOD;
                    j-=p;
                    mp[ase[c1-1]]-=p;
                    if (mp[ase[c1-1]]==0) c1--;
                }
            }
        }
        printf("Case #%lld: %lld\n",cas,ans);
        mp.clear();
    }
    return 0;
}

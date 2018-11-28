#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#define MOD (1000002013ll)
#define INF ((long long)(~0llu>>2))
using namespace std;
int T,m,h[3005],lim[3005],v[10000005],next[10000005],tot,dep[3005],head,tail,q[3005];
long long a1,a2,n,f[10000005],w[10000005],d[3005]; bool s[3005];
struct tp {long long x,y,z;} l[1005];
bool cmp(const tp &a,const tp &b) {return a.x<b.x;}
void ae(int x,int y,long long z,long long u)
{
    v[++tot]=y; next[tot]=h[x]; h[x]=tot; f[tot]=z; w[tot]=u;
    v[++tot]=x; next[tot]=h[y]; h[y]=tot; f[tot]=0; w[tot]=-u;
}
bool spfa()
{
    for(int i=1;i<=3000;++i) {d[i]=INF; dep[i]=0;}
    dep[0]=1; s[q[(++tail)%=3000]=0]=1; int x;
    memcpy(lim,h,sizeof(lim));
    while(head!=tail)
    {
        s[x=q[(++head)%=3000]]=0;
        for(int i=h[x];i;i=next[i]) if(f[i]&&d[v[i]]>d[x]+w[i])
        {
            d[v[i]]=d[x]+w[i]; dep[v[i]]=dep[x]+1;
            if(!s[v[i]]) s[q[(++tail)%=3000]=v[i]]=1;
        }
    }
    return dep[3000];
}
long long go(int x,long long y)
{
    if(x==3000) return y; long long y0=y,t;
    for(int &i=lim[x];i;i=next[i]) if(f[i]&&d[v[i]]==d[x]+w[i]&&dep[v[i]]==dep[x]+1)
        {t=go(v[i],min(y,f[i])); f[i]-=t; y-=t; f[i^1]+=t; if(!y) break;}
    return y0-y;
}
void build(int x,int y)
{
    memset(h,0,sizeof(h)); tot=1;
    for(int i=x;i<=y;++i)
        for(int j=i;j<=y;++j)
        {
            if(l[i].x<=l[j].y) ae(i,j+1000,INF,(n+n-(l[j].y-l[i].x-1))*(l[j].y-l[i].x)/2);
            if(l[j].x<=l[i].y) ae(j,i+1000,INF,(n+n-(l[i].y-l[j].x-1))*(l[i].y-l[j].x)/2);
        }
    for(int i=x;i<=y;++i) {ae(0,i,l[i].z,0); ae(i+1000,3000,l[i].z,0);}
}
int main()
{
    freopen("i1.txt","r",stdin);
    freopen("o1.txt","w",stdout);
    scanf("%d",&T);
    for(int I=1;I<=T;++I)
    {
        scanf("%lld%d",&n,&m); a1=a2=0;
        for(int i=1;i<=m;++i)
        {
            scanf("%lld%lld%lld",&l[i].x,&l[i].y,&l[i].z);
            (a2+=((n+n-(l[i].y-l[i].x-1))*(l[i].y-l[i].x)/2)%MOD*l[i].z)%=MOD;
        }
        sort(l+1,l+m+1,cmp);
        for(int i=1;i<=m;++i)
        {
            long long t=l[i].y; int p=i;
            while(i<m&&t>=l[i+1].x) {++i; t=max(t,l[i].y);}
            build(p,i); while(spfa()) (a1+=d[3000]*go(0,MOD*1000))%=MOD;
        }
        printf("Case #%d: %lld\n",I,(a2-a1+MOD)%MOD);
    }
    return 0;
}

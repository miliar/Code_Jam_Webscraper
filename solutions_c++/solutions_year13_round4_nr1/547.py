//c++  #pragma comment(linker, "/STACK:1024000000,1024000000")
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <map>
#include <set>
#define rep(i,a,b) for(int i=a;i<=b;i++)
#define INF (1<<29)
#define eps (1e-5)
#define pb push_back
using namespace std;
/*
struct Edge{
    int v,next,w;
}edge[MAXN*3];
int E,list[MAXN];
void init() {memset(list,E=-1,sizeof(list)); }
void add(int u,int v,int w)
{
    edge[++E].v=v; edge[E].w=w; edge[E].next=list[u]; list[u]=E;
}
*/
int input()
{
    int a,k=1; char c;
    while ( (c=getchar())>'9' || c<'0')
        if (c=='-') k=-1;
    a=c-'0';
    while ( (c=getchar())<='9' && c>='0') a=a*10+c-'0';
    return a*k;
}

struct node
{
    long long id;
    long long w;
    int p;
    bool operator<(node a)const{
        if (id==a.id) return p>a.p;
        return id<a.id;
    }
}a[1005*2];
long long n;
int m;
const long long MOD=1000002013LL;

long long f(long long a,long long b)
{
    a=b-a;
    return n*a-(a-1)*a/2;
}

stack<long long> s1; //ÄÄÀï
stack<long long> s2; //ÈËÊý
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("a0.out","w",stdout);
    int T=input(),cas=0;
    while (T--)
    {
        int s=0;
        scanf("%lld%d",&n,&m);
        rep(i,1,m)
        {
            scanf("%lld",&a[i*2-1].id);
            scanf("%lld",&a[i*2].id);
            scanf("%lld",&a[i*2-1].w);
            a[i*2].w=a[i*2-1].w;
            a[i*2-1].p=1;
            a[i*2].p=-1;
        }
        long long ans=0;
        rep(i,1,m) ans=(ans+f(a[i*2-1].id,a[i*2].id)*a[i*2].w)%MOD;
        sort(a+1,a+m*2+1);
        rep(i,1,2*m)
            if (a[i].p==1)
            {
                s1.push(a[i].id);
                s2.push(a[i].w);
            }
            else
            {
                while (a[i].w)
                {
                    long long id=s1.top(); s1.pop();
                    long long w=s2.top(); s2.pop();
                    long long k=min(a[i].w , w);

                    ans=((ans-f(id,a[i].id)*k)%MOD+MOD)%MOD;
                    w-=k;
                    a[i].w-=k;
                    if (w>0)
                    {
                        s1.push(id);
                        s2.push(w);
                    }
                }
            }
        printf("Case #%d: %lld\n",++cas,ans);
    }
    //system("pause");
    return 0;
}

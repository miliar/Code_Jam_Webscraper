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
#define MAXN 105
long long a[MAXN],f[MAXN][MAXN];
int main()
{
    freopen("A-large (1).in","r",stdin);
    freopen("a_s.out","w",stdout);
    int T=input(),cas=0;
    while (T--)
    {
        long long m;
        int n;
        scanf("%lld%d",&m,&n);
        rep(i,1,n) scanf("%lld",&a[i]);
        sort(a+1,a+n+1);
        /*
        memset(f,0,sizeof(f));
        long long MAX=(1LL<<60);
        f[0][0]=m;
        rep(i,1,n) f[0][i]=min(MAX,f[0][i-1]*2-1);
        rep(i,1,n)
            rep(j,0,n)
            {
                if (j)
                {
                    f[i][j]=f[i-1][j-1];
                    long long tmp=min(MAX,f[i-1][j-1]*2-1);
                    if (tmp>a[i]) f[i][j]=max(f[i][j],tmp+a[i]);
                }
                if (f[i-1][j]>a[i]) f[i][j]=max(f[i][j],f[i-1][j]+a[i]);
            }
        int ans=0;
        rep(i,0,n)
            if (f[n][i])
            {
                ans=i;
                break;
            }
        */
        int ans=n,now=0;
        rep(i,1,n)
        {
            while (m!=1 && m<=a[i]) m=m*2-1 , now++;
            if (m<=a[i]) break;
            m=m+a[i];
            ans=min(ans,now+n-i);
        }
        printf("Case #%d: %d\n",++cas,ans);
    }
    //system("pause");
    return 0;
}

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

int main()
{
    freopen("B-small-attempt0 (2).in","r",stdin);
    freopen("b0.out","w",stdout);
    int T=input(),cas=0;
    while (T--)
    {
        int n,p;
        scanf("%d%d",&n,&p);
        printf("Case #%d:",++cas);
        int ans1,ans2=0;
        int m=1<<n;
        rep(i,1,m)
        {
            int id=0;
            rep(j,1,n)
                if ((1<<j)<=i)
                    id=id+(1<<(n-j));
            if (id<p) ans1=i;

            id=0;
            rep(j,1,n)
                if ((1<<j)>m-i+1)
                    id=id+(1<<n-j);
            if (id<p) ans2=i;
        }
        printf(" %d %d\n",ans1-1,ans2-1);
    }
    //system("pause");
    return 0;
}

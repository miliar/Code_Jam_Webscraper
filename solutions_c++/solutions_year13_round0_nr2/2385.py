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

int n,m,a[105][105];

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("b_l.out","w",stdout);
    int T,cas=0;
    scanf("%d",&T);
    while (T--)
    {
        scanf("%d%d",&n,&m);
        rep(i,1,n) rep(j,1,m) scanf("%d",&a[i][j]);

        bool y=true;
        rep(i,1,n)
            rep(j,1,m)
            {
                int t=0;
                rep(k,1,m)
                    if (a[i][j]<a[i][k])
                    {
                        t++;
                        break;
                    }
                rep(k,1,n)
                    if (a[i][j]<a[k][j])
                    {
                        t++;
                        break;
                    }
                if (t==2) y=false;
            }
        printf("Case #%d: ",++cas);
        if (y) puts("YES"); else puts("NO");
    }
    //system("pause");
    return 0;
}

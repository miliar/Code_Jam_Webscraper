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
bool f[1005];

bool judge(int x)
{
    int a[10],len=0,tmp=x;
    while (x)
    {
        a[len++]=x%10;
        x/=10;
    }
    for (int i=0;i<len;i++)
        if (a[i]!=a[len-1-i])
            return false;
    return true;
}

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("c.out","w",stdout);
    memset(f,0,sizeof(f));
    for (int i=1;i*i<=1000;i++)
        if (judge(i) && judge(i*i))
            f[i*i]=true;
    int T,cas=0;
    scanf("%d",&T);
    while (T--)
    {
        int l,r,s=0;
        scanf("%d%d",&l,&r);
        rep(i,l,r)
            if (f[i])
                s++;
        printf("Case #%d: %d\n",++cas,s);
    }
    //system("pause");
    return 0;
}

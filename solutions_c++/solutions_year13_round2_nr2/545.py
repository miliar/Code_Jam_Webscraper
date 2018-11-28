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
    int l,r;
    double w;
};
queue<node> q;
int n,X,Y;
bool judge(int h,int l,int r)
{
    if (abs(Y)+abs(X)<=h) return true;
    if (X<=0)
    {
        return -h-2*(l>0)<=X && X<=-h-3*(l>0)+l && abs(X)+abs(Y)<=h+2*(l);
    }else
    {
        return h+3*(r>0)-r<=X && X<=h+2*(r>0) && abs(X)+abs(Y)<=h+2*(r);
    }
    return false;
}
int main()
{
    freopen("B-small-attempt3.in","r",stdin);
    freopen("b_s.out","w",stdout);
    int T=input(),cas=0;
    while (T--)
    {
        scanf("%d%d%d",&n,&X,&Y);
        int h=1;
        while (h*(1+h)/2<=n) h+=2;
        h-=2;
        int tx,ty,s;
        tx=0; ty=(h-1)/2*2;
        s=n-(h*(h+1)/2);
        //printf("h=%d\n",h);printf("ty=%d\n",ty);printf("s=%d\n",s);
        double ans=0;
        while (q.size()) q.pop();
        node tmp;
        tmp.l=tmp.r=0; tmp.w=1;
        q.push(tmp);
        while (q.size())
        {
            node now=q.front(); q.pop();
            if (judge(ty,now.l,now.r))
            {
            //printf("%d %d\n",now.l,now.r);
                ans=ans+now.w;
            }else
            if (now.l+now.r<s)
            {
                int aaa=2;
                if (now.l==h+1) aaa--;
                if (now.r==h+1) aaa--;
                if (now.l<=h)
                {
                    now.l++; now.w/=aaa; q.push(now); now.l--; now.w*=aaa;
                }
                if (now.r<=h)
                {
                    now.r++; now.w/=aaa; q.push(now); now.r--; now.w*=aaa;
                }
            }
        }
        printf("Case #%d: %.6lf\n",++cas,ans);
    }
    //system("pause");
    return 0;
}

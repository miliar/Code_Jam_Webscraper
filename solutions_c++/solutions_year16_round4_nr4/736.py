#include <map>
#include <set>
#include <stack>
#include <queue>
#include <cmath>
#include <string>
#include <vector>
#include <cstdio>
#include <cctype>
#include <cstring>
#include <sstream>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#pragma comment(linker,"/STACK:102400000,102400000")

using namespace std;
#define   MAX           6005
#define   MAXN          1000005
#define   maxnode       10
#define   sigma_size    2
#define   lson          l,m,rt<<1
#define   rson          m+1,r,rt<<1|1
#define   lrt           rt<<1
#define   rrt           rt<<1|1
#define   middle        int m=(r+l)>>1
#define   LL            long long
#define   ull           unsigned long long
#define   mem(x,v)      memset(x,v,sizeof(x))
#define   lowbit(x)     (x&-x)
#define   pii           pair<int,int>
#define   bits(a)       __builtin_popcount(a)
#define   mk            make_pair
#define   limit         10000

//const int    prime = 999983;
const int    INF   = 0x3f3f3f3f;
const LL     INFF  = 0x3f3f;
const double pi    = acos(-1.0);
const double inf   = 1e18;
const double eps   = 1e-9;
const LL     mod   = 1e9+7;
const ull    mxx   = 1333331;

/*****************************************************/
inline void RI(int &x){
    char c;
    while((c=getchar())<'0' || c>'9');
    x=c-'0';
    while((c=getchar())>='0' && c<='9') x=(x<<3)+(x<<1)+c-'0';
}
/*****************************************************/

struct Edge{
    int u,v,next;
}edge[MAX*MAX];
int dfn[MAX],low[MAX],belong[MAX],sstack[MAX],instack[MAX];
int head[MAX],tot,Index,top,cnt;// tot是建图//cnt是强联通分量个数
int n;
void init(){
    mem(head,-1);
    mem(instack,0);
    mem(dfn,0);
    tot=0;
    top=0;
    cnt=0;
    Index=0;
}

void add_edge(int a,int b){
    edge[tot]=(Edge){a,b,head[a]};
    head[a]=tot++;
}

void tarjan(int u){//判断可行只需要一个tarjan即可
    dfn[u]=low[u]=++Index;
    sstack[++top]=u;
    instack[u]=1;
    for(int i=head[u]; i!=-1; i=edge[i].next){
        int v=edge[i].v;
        if(!dfn[v]){
            tarjan(v);
            low[u]=min(low[u],low[v]);
        }
        else if(instack[v])
            low[u]=min(low[u],dfn[v]);
    }
    if(dfn[u]==low[u]){
        ++cnt;
        while(1){
            int k=sstack[top--];
            instack[k]=0;
            belong[k]=cnt;
            if(k==u) break;
        }
    }
}

int main(){
    //freopen("in.txt","r",stdin);
    int t,m;
    while(cin>>t>>m){
        init();
        for(int i=0;i<t;i++){
            int a,b,c;
            scanf("%d%d%d",&a,&b,&c);
            add_edge(a,b+3*t);
            add_edge(a,c+3*t);
            add_edge(a+3*t,b);
            add_edge(a+3*t,c);
            add_edge(b,c);
            add_edge(b,a+3*t);
            add_edge(b+3*t,c+3*t);
            add_edge(b+3*t,a);
            add_edge(c,b);
            add_edge(c,a+3*t);
            add_edge(c+3*t,b+3*t);
            add_edge(c+3*t,a);
        }
        for(int i=0;i<m;i++){
            int a,b;
            scanf("%d%d",&a,&b);
            add_edge(a,b+3*t);
            add_edge(b,a+3*t);
            //add_edge(a+3*t,b);
            //add_edge(b+3*t,a);
        }
        for(int i=0;i<6*t;i++){
            if(!dfn[i]) tarjan(i);
        }
        int flag=0;
        for(int i=0;i<3*t;i++){
            if(belong[i]==belong[i+3*t]) flag=1;
        }
        if(flag) printf("no\n");
        else printf("yes\n");
    }
    return 0;
}

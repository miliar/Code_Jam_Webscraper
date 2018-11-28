#include <vector>
#include <list>
#include <queue>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <tr1/unordered_set>
#include <tr1/unordered_map>

using namespace std;
using namespace tr1;

const int MaxN=9000;
const int MaxM=100005;
const int INF=(1<<29)-1;
typedef struct tNode
{
    int v,f;
    tNode *nxt,*rev;
} Edge;
Edge E[MaxN],mem[MaxM*2];
Edge *Cur[MaxN];
int M,S,T,N,eCnt;
int gap[MaxN],d[MaxN];
int flow,aug;
bool done;
void Init(int SS,int TT,int NN)
{
    S=SS,T=TT,N=NN;
    eCnt=0;
    for(int i=0; i<N; i++) E[i].nxt=NULL;
}
void Add_edge(int u,int v,int f)
{
    //printf("%d->%d %d\n",u,v,f);
    Edge *p=&mem[eCnt++],*q=&mem[eCnt++];
    p->v=v,p->f=f,p->rev=q;
    p->nxt=E[u].nxt,E[u].nxt=p;
    q->v=u,q->f=0,q->rev=p;
    q->nxt=E[v].nxt,E[v].nxt=q;
}
void Sap(int u)
{
    if(u==T)
    {
        done=true;
        flow+=aug;
        return ;
    }
    Edge *p=NULL;
    int augOri=aug;
    for(p=Cur[u]; p!=NULL; p=p->nxt)
    {
        if(p->f<=0) continue;
        if(d[p->v]+1==d[u])
        {
            Cur[u]=p;
            aug=min(aug,p->f);
            Sap(p->v);
            if(d[S]>=N) return ;
            if(done) break;
            aug=augOri;
        }
    }
    if(done) p->f-=aug,p->rev->f+=aug;
    else
    {
        if(!(--gap[d[u]])) d[S]=N;
        int minD=N;
        Cur[u]=E[u].nxt;
        for(p=Cur[u]; p!=NULL; p=p->nxt)
            if(p->f>0) minD=min(minD,d[p->v]);
        d[u]=minD+1;
        gap[d[u]]++;
    }
}
int Maxflow()
{
    for(int i=0; i<N; i++)
    {
        gap[i]=d[i]=0;
        Cur[i]=E[i].nxt;
    }
    gap[0]=N;
    flow=0;
    while(d[S]<N)
    {
        aug=INF;
        done=false;
        Sap(S);
    }
    return flow;
}

int n,idx;
string str,s;
map<string,int> mp;
vector<int> f[2005];

int main(){
    //freopen("c.in","r",stdin);
    //freopen("c.out","w",stdout);
    freopen("C-small-attempt1.in","r",stdin);
    freopen("C-small-attempt1.out","w",stdout);
    //freopen("C-large.in","r",stdin);
    //freopen("C-large.out","w",stdout);
    static int T,Cas;
    cin>>T;
    for(Cas=1;Cas<=T;Cas++){
        cin>>n;
        getline(cin,str);
        idx=0;
        mp.clear();
        for(int i=0;i<n;i++){
            getline(cin,str);
            stringstream liu;
            liu<<str;
            f[i].clear();
            while(liu>>s){
                if(mp.find(s)==mp.end())mp[s]=++idx;
                f[i].push_back(mp[s]-1);
            }
            sort(f[i].begin(),f[i].end());
        }
        Init(n+idx,n+idx+1,n+idx+2);
        Add_edge(n+idx,0,INF);
        Add_edge(1,n+idx+1,INF);
        for(int i=0;i<n;i++)
        for(int j=0;j<(int)f[i].size();j++){
            if(j && f[i][j]==f[i][j-1])continue;
            Add_edge(i,n+f[i][j],1);
            Add_edge(n+f[i][j],i,1);
        }
        printf("Case #%d: %d\n",Cas,Maxflow());
    }
    return 0;
}

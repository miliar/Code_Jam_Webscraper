// @author peter50216
// #includes {{{
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<functional>
#include<math.h>
#include<assert.h>
#include<stdarg.h>
#include<time.h>
#include<limits.h>
#include<ctype.h>
#include<string>
#include<map>
#include<set>
#include<queue>
#include<algorithm>
#include<vector>
#include<iostream>
#include<sstream>
using namespace std;
// }}}
// #defines {{{
#define FOR(i,c) for(__typeof((c).begin()) i=(c).begin();i!=(c).end();i++)
#define SZ(x) ((int)(x).size())
#define ALL(x) (x).begin(),(x).end()
#define REP(i,n) for(int i=0;i<(n);i++)
#define REP1(i,a,b) for(int i=(a);i<=(b);i++)
#define REPL(i,x) for(int i=0;x[i];i++)
#define PER(i,n) for(int i=(n)-1;i>=0;i--)
#define PER1(i,a,b) for(int i=(a);i>=(b);i--)
#define RI(x) scanf("%d",&x)
#define DRI(x) int x;RI(x)
#define RII(x,y) scanf("%d%d",&x,&y)
#define DRII(x,y) int x,y;RII(x,y)
#define RIII(x,y,z) scanf("%d%d%d",&x,&y,&z)
#define DRIII(x,y,z) int x,y,z;RIII(x,y,z)
#define RS(x) scanf("%s",x)
#define PI(x) printf("%d\n",x)
#define PIS(x) printf("%d ",x)
#define CASET int ___T,cas=1;scanf("%d ",&___T);while(___T--)
#define CASEN0(n) int cas=1;while(scanf("%d",&n)!=EOF&&n)
#define CASEN(n) int cas=1;while(scanf("%d",&n)!=EOF)
#define MP make_pair
#define PB push_back
#define MS0(x) memset(x,0,sizeof(x))
#define MS1(x) memset(x,-1,sizeof(x))
#define SEP(x) ((x)?'\n':' ')
#define F first
#define S second
#ifdef ONLINE_JUDGE
#define FILEIO(x) freopen(#x ".in","r",stdin);freopen(#x ".out","w",stdout);
#define FILEIOS freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
#else
#define FILEIO(x) ;
#define FILEIOS ;
#endif
typedef pair<int,int> PII;
typedef long long LL;
typedef unsigned long long ULL;
// }}}

struct XD{
    int x,y,a,b,id;
    bool iss;
    XD(){}
    void get(int ii){
        RII(x,y);
        RII(a,b);
        x--;y--;
        id=ii;
        iss=1;
    }
    int getl(){
        return iss?a:b;
    }
};
vector<int> ed[1010];
vector<int> rev[1010];
vector<XD> alle;
pair<int,LL> q[550];
//bool good[550];
int id[550];
const LL INF=100000000000LL;
int n,m,p;
LL dis[1010];
LL disr[1010];
bool ul[1010];
inline bool solve(int pp,LL dd){
    REP(i,SZ(alle))alle[i].iss=1;
    while(1){
        {
            priority_queue<pair<LL,int> > pq;
            REP(i,n)dis[i]=INF;
            dis[0]=0;
            pq.push(MP(-dis[0],0));
            ul[0]=1;
            while(!pq.empty()){
                pair<LL,int> pp=pq.top();
                pq.pop();
                if(pp.F!=-dis[pp.S])continue;
                int np=pp.S;
                REP(i,SZ(ed[np])){
                    int ii=ed[np][i];
                    int y=alle[ii].y;
                    if(dis[y]>dis[np]+alle[ii].getl()){
                        dis[y]=dis[np]+alle[ii].getl();
                        pq.push(MP(-dis[y],y));
                    }
                }
            }
        }
        {
            priority_queue<pair<LL,int> > pq;
            REP(i,n)disr[i]=INF;
            disr[1]=0;
            pq.push(MP(-disr[1],1));
            while(!pq.empty()){
                pair<LL,int> pp=pq.top();
                pq.pop();
                if(pp.F!=-disr[pp.S])continue;
                int np=pp.S;
                REP(i,SZ(rev[np])){
                    int ii=rev[np][i];
                    int y=alle[ii].x;
                    if(disr[y]>disr[np]+alle[ii].getl()){
                        disr[y]=disr[np]+alle[ii].getl();
                        pq.push(MP(-disr[y],y));
                    }
                }
            }
        }
        bool f=0;
        queue<int> que;
        que.push(0);
        while(!que.empty()){
            int np=que.front();
            que.pop();
            //printf("np=%d\n",np+1);
            REP(i,SZ(ed[np])){
                int ii=ed[np][i];
                int x=alle[ii].x,y=alle[ii].y;
                if(dis[x]+alle[ii].getl()==dis[y]){
                    if(alle[ii].iss==1){
                        //printf("%d -> %d %d %d\n",x+1,y+1,alle[ii].a,alle[ii].b);
                        alle[ii].iss=0;f=1;
                    }else{
                        que.push(y);
                    }
                }
            }
        }
        //puts("======");
        /*
        REP(i,SZ(alle)){
            int x=alle[i].x,y=alle[i].y;
            if(dis[x]+disr[y]+alle[i].getl()==dis[1]){
                if(alle[i].iss==1){
                    alle[i].iss=0;f=1;
                }
            }
        }*/
        //printf("dis[1]=%d\n",dis[1]);
        if(disr[pp]+dd==dis[1])return 1;
        if(!f)break;
    }
    return 0;
}
int main(){
    CASET{
        RIII(n,m,p);
        REP(i,n)ed[i].clear();
        REP(i,n)rev[i].clear();
        alle.clear();
        REP(i,m){
            XD t;
            t.get(i);
            ed[t.x].PB(alle.size());
            rev[t.y].PB(alle.size());
            alle.PB(t);
        }
        LL d=0;
        REP(i,p){
            DRI(a);
            a--;
            int y=alle[a].y;
            //printf("(%d)%d ",a+1,y+1);
            d+=alle[a].a;
            q[i]=MP(y,d);
            id[i]=a;
        }
        //puts("");
        //MS0(good);
        int ans=-1;
        REP(i,p){
            //printf("i=%d\n",i);
            alle[id[i]].b=alle[id[i]].a;
            if(!solve(q[i].F,q[i].S)){
                ans=i;break;
            }
        }
        printf("Case #%d: ",cas++);
        if(ans==-1)puts("Looks Good To Me");
        else printf("%d\n",id[ans]+1);
    }
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread


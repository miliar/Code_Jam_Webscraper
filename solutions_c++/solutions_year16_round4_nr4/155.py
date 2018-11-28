#include<bits/stdc++.h>
#define MAX   111
#define FOR(i,a,b) for (int i=(a),_b=(b);i<=_b;i=i+1)
#define FORD(i,b,a) for (int i=(b),_a=(a);i>=_a;i=i-1)
#define REP(i,n) for (int i=0,_n=(n);i<_n;i=i+1)
#define FORE(i,v) for (__typeof((v).begin()) i=(v).begin();i!=(v).end();i++)
#define ALL(v) (v).begin(),(v).end()
#define fi   first
#define se   second
#define MASK(i) (1LL<<(i))
#define BIT(x,i) (((x)>>(i))&1)
#define next   ___next
#define prev   ___prev
#define left   ___left
#define right   ___right
#define __builtin_popcount __builtin_popcountll
using namespace std;
template<class X,class Y>
    void minimize(X &x,const Y &y) {
        if (x>y) x=y;
    }
template<class X,class Y>
    void maximize(X &x,const Y &y) {
        if (x<y) x=y;
    }
class DinicFlow {
private:
    static const int INF=(int)1e9+7;
    vector<int> dist,head,q,work;
    vector<int> point,capa,flow,next;
    int n,m;
public:
    DinicFlow() {
        n=0;m=0;
    }
    DinicFlow(int n) {
        this->n=n;m=0;
        dist.assign(n+7,0);
        head.assign(n+7,-1);
        q.assign(n+7,0);
        work.assign(n+7,0);
    }
    void addEdge(int u,int v,int c1,int c2) {
        //printf("Add %d %d %d %d\n",u,v,c1,c2);
        point.push_back(v);capa.push_back(c1);flow.push_back(0);next.push_back(head[u]);head[u]=m++;
        point.push_back(u);capa.push_back(c2);flow.push_back(0);next.push_back(head[v]);head[v]=m++;
    }
    bool bfs(int s,int t) {
        FOR(i,1,n) dist[i]=-1;
        int sz=0;
        q[sz++]=s;dist[s]=0;
        for (int x=0;x<sz;x=x+1) {
            int u=q[x];
            for (int i=head[u];i>=0;i=next[i])
                if (dist[point[i]]<0 && flow[i]<capa[i]) {
                    dist[point[i]]=dist[u]+1;
                    q[sz++]=point[i];
                }
        }
        return (dist[t]>=0);
    }
    int dfs(int s,int t,int f) {
        if (s==t) return (f);
        for (int &i=work[s];i>=0;i=next[i])
            if (dist[point[i]]==dist[s]+1 && flow[i]<capa[i]) {
                int d=dfs(point[i],t,min(f,capa[i]-flow[i]));
                if (d>0) {
                    flow[i]+=d;
                    flow[i^1]-=d;
                    return (d);
                }
            }
        return (0);
    }
    int maxFlow(int s,int t) {
        int totflow=0;
        while (bfs(s,t)) {
            FOR(i,1,n) work[i]=head[i];
            while (true) {
                int d=dfs(s,t,INF);
                if (d<=0) break;
                totflow+=d;
            }
        }
        return (totflow);
    }
};
int n;
bool canFail(int mask,int id) {
    DinicFlow df(2*n+2);
    int src=2*n+1;
    int snk=2*n+2;
    REP(i,n) if (i!=id) df.addEdge(src,i+1,1,0);
    REP(i,n) if (BIT(mask,id*n+i)) df.addEdge(i+n+1,snk,1,0);
    REP(i,n) if (i!=id) REP(j,n) if (BIT(mask,i*n+j)) df.addEdge(i+1,j+n+1,1,0);
    int numReq=0;
    REP(i,n) if (BIT(mask,id*n+i)) numReq++;
    return (df.maxFlow(src,snk)>=numReq);
}
bool ok(int mask) {
    REP(i,n) if (canFail(mask,i)) return (false);
    return (true);
}
void process(int tc) {
    cerr<<"TEST "<<tc<<endl;
    scanf("%d",&n);
    int curState=0;
    REP(i,n) {
        char s[MAX];
        scanf("%s",s);
        REP(j,n) if (s[j]=='1') curState|=MASK(i*n+j);
    }
    int res=n*n+7;
    REP(i,MASK(n*n)) if (ok(curState|i)) minimize(res,__builtin_popcount(i));
    printf("Case #%d: %d\n",tc,res);
}
int main(void) {
    int t; scanf("%d",&t);
    FOR(i,1,t) process(i);
    return 0;
}

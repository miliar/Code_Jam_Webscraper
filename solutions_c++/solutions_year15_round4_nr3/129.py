#include <bits/stdc++.h>
#define SZ(X) ((int)(X).size())
#define ALL(X) (X).begin(), (X).end()
#define REP(I, N) for (int I = 0; I < (N); ++I)
#define REPP(I, A, B) for (int I = (A); I < (B); ++I)
#define RI(X) scanf("%d", &(X))
#define RII(X, Y) scanf("%d%d", &(X), &(Y))
#define RIII(X, Y, Z) scanf("%d%d%d", &(X), &(Y), &(Z))
#define DRI(X) int (X); scanf("%d", &X)
#define DRII(X, Y) int X, Y; scanf("%d%d", &X, &Y)
#define DRIII(X, Y, Z) int X, Y, Z; scanf("%d%d%d", &X, &Y, &Z)
#define RS(X) scanf("%s", (X))
#define CASET int ___T, case_n = 1; scanf("%d ", &___T); while (___T-- > 0)
#define MP make_pair
#define PB push_back
#define MS0(X) memset((X), 0, sizeof((X)))
#define MS1(X) memset((X), -1, sizeof((X)))
#define LEN(X) strlen(X)
#define PII pair<int,int>
#define VPII vector<pair<int,int> >
#define PLL pair<long long,long long>
#define F first
#define S second
typedef long long LL;
using namespace std;
const int MOD = 1e9+7;
const int SIZE = 1e6+10;
// template end here
#define FN 500010
#define FM 4200010
#define INF 1034567890
#define FOR(it,c) for ( __typeof((c).begin()) it=(c).begin(); it!=(c).end(); it++ )
using namespace std;
typedef long long LL;
struct E {
    int k,c;
    E(){}
    E( int _k, int _c ):k(_k),c(_c){}
} es[FM];

struct Flow {
    int n,m,dis[FN];
    int qq[FN],qr,ql;
    vector<int> e[FN];
    void init( int _n ) {
        n=_n; m=0;
        for ( int i=0; i<n; i++ ) e[i]=vector<int>();
    }
    void add_edge( int a, int b, int c ) {
        e[a].push_back(m); es[m]=E(b,c); m++;
        e[b].push_back(m); es[m]=E(a,0); m++;
    }
    bool BFS() {
        memset(dis,-1,n*sizeof(int));
        ql=qr=0;
        qq[qr++]=0;
        dis[0]=0;
        while ( ql!=qr && dis[n-1]==-1 ) {
            int p=qq[ql++];
            FOR(it,e[p]) {
                E ee=es[*it];
                if ( ee.c==0 || dis[ee.k]!=-1 ) continue;
                dis[ee.k]=dis[p]+1;
                qq[qr++]=ee.k;
            }
        }
        return dis[n-1]!=-1;
    }
    LL go( int p, LL c ) {
        if ( p==n-1 ) return c;
        LL ret=0,tmp;
        FOR(it,e[p]) {
            E &ee=es[*it];
            if ( ee.c==0 || dis[p]+1!=dis[ee.k] ) continue;
            tmp=go(ee.k,min(c-ret,(LL)ee.c));
            ret+=tmp; ee.c-=tmp; es[(*it)^1].c+=tmp;
            if ( ret==c ) break;
        }
        if ( ret==0 ) dis[p]=-1;
        return ret;
    }
    LL maxflow() {
        LL ret=0;
        while ( BFS() ) ret+=go(0,1LL<<60);
        return ret;
    }
} flow;
map<string,int>H;
int id;
int get(const string& str){
    if(H.count(str))return H[str];
    return H[str]=id++;
}
vector<int>d[240];
char s[SIZE];
char con[4000][4000],tt;
const int KERKER=100000;
int main(){
    CASET{
        tt++;
        H.clear();
        DRI(n);
        id=1;
        gets(s);
        REPP(i,1,n+1){
            d[i].clear();
            gets(s);
            stringstream ss(s);
            string str;
            while(ss>>str){
                d[i].PB(get(str));
            }
        }
        int wn=id-1;
        //printf("wn:%d\n",wn);
        int ed=n+wn+wn+1;
        flow.init(n+wn+wn+2);
        flow.add_edge(0,1,INF);
        flow.add_edge(2,ed,INF);
        REPP(i,3,n+1){
            flow.add_edge(0,i,KERKER);
            flow.add_edge(i,ed,KERKER);
        }
        REPP(i,1,n+1){
            REP(j,SZ(d[i])){
                int x=d[i][j];
                REPP(k,1,SZ(d[i])){
                    int y=d[i][k];
                    con[x][y]=con[y][x]=tt;
                }
                flow.add_edge(i,x+n,INF);
                flow.add_edge(n+wn+x,i,INF);
            }
        }
        REPP(i,1,wn+1)flow.add_edge(n+i,n+i+wn,1);
        REPP(i,1,wn+1)REPP(j,i+1,wn+1){
            if(con[i][j]==tt){
                flow.add_edge(n+wn+i,n+j,INF);
                flow.add_edge(n+wn+j,n+i,INF);
            }
        }
        assert(flow.m<FM);
        printf("Case #%d: %lld\n",case_n++,flow.maxflow()-(n-2LL)*KERKER);
    }
    return 0;
}

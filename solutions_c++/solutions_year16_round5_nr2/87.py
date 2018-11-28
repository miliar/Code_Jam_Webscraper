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
#define div   ___div
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
template<class T>
    T Abs(const T &x) {
        return (x<0?-x:x);
    }
const int rate=100;
vector<int> allow[MAX];
string name,str[MAX];
int cnt[MAX],req[MAX],numChild[MAX],n,m;
void init(void) {
    cin>>n;
    REP(i,n+1) allow[i].clear();
    FOR(i,1,n) {
        cin>>req[i];
        allow[req[i]].push_back(i);
    }
    cin>>name>>m;
    REP(i,m) cin>>str[i];
    REP(i,m) cnt[i]=0;
}
void dfs(int u) {
    numChild[u]=1;
    FORE(it,allow[u]) {
        dfs(*it);
        numChild[u]+=numChild[*it];
    }
}
int getRandom(const vector<pair<int,int> > &can) {
    int sum=0;
    FORE(it,can) sum+=it->se;
    int tmp=rand()%sum;
    REP(i,can.size()) {
        if (tmp<can[i].se) return (i);
        tmp-=can[i].se;
    }
    assert(false);
}
void randomTry(void) {
    string cur;
    vector<pair<int,int> > can;
    can.push_back(make_pair(0,numChild[0]));
    int comp=0;
    REP(love,n+1) {
        if (__builtin_popcount(comp)==m) return;
        int id=getRandom(can);
        int chs=can[id].fi;
        if (chs>0) cur.push_back(name[chs-1]);
        FORE(it,allow[chs]) can.push_back(make_pair(*it,numChild[*it]));
        swap(can[id],can.back()); can.pop_back();
        REP(i,m) if (!BIT(comp,i) && cur.size()>=str[i].size())
            if (cur.substr(cur.size()-str[i].size(),str[i].size())==str[i]) {
                cnt[i]++;
                comp|=MASK(i);
            }
    }
}
void process(int tc) {
    dfs(0);
    int numTry=rate*n;
    REP(love,numTry) randomTry();
    printf("Case #%d:",tc);
    REP(i,m) printf(" %.5lf",1.0*cnt[i]/numTry); printf("\n");
    fflush(stdout);
}
int main(void) {
    srand(time(NULL));
    int t; cin>>t;
    FOR(i,1,t) {
        cerr<<i<<endl;
        init();
        process(i);
    }
    return 0;
}

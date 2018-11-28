#include<bits/stdc++.h>
#define MAX   1000100
#define FOR(i,a,b) for (int i=(a),_b=(b);i<=_b;i=i+1)
#define FORD(i,b,a) for (int i=(b),_a=(a);i>=_a;i=i-1)
#define REP(i,n) for (int i=0,_n=(n);i<_n;i=i+1)
#define FORE(i,v) for (__typeof((v).begin()) i=(v).begin();i!=(v).end();i++)
#define ALL(v) (v).begin(),(v).end()
#define fi   first
#define se   second
using namespace std;
class FenwickTree {
    private:
    int n;
    vector<int> v;
    public:
    FenwickTree() {
        n=0;
    }
    FenwickTree(int n) {
        this->n=n;
        v.assign(n+7,0);
    }
    void update(int x,int d) {
        for (;x<=n;x+=x&-x) v[x]+=d;
    }
    int get(int x) const {
        int res=0;
        for (;x>=1;x&=x-1) res+=v[x];
        return (res);
    }
};
vector<int> child[MAX];
int val[MAX],minVal[MAX],maxVal[MAX];
int n,allow;
void loadTree(void) {
    scanf("%d%d",&n,&allow);
    FOR(i,1,n) child[i].clear();
    int s0,as,cs,rs;
    scanf("%d%d%d%d",&s0,&as,&cs,&rs);
    FOR(i,1,n) {
        val[i]=s0;
        s0=(1LL*s0*as+cs)%rs;
    }
    scanf("%d%d%d%d",&s0,&as,&cs,&rs);
    FOR(i,2,n) {
        s0=(1LL*s0*as+cs)%rs;
        child[s0%(i-1)+1].push_back(i);
    }
}
void dfs(int u) {
    FORE(it,child[u]) {
        int v=*it;
        maxVal[v]=max(maxVal[u],val[v]);
        minVal[v]=min(minVal[u],val[v]);
        dfs(v);
    }
}
void process(int tc) {
    maxVal[1]=minVal[1]=val[1];
    dfs(1);
    vector<pair<int,int> > range;
    FOR(i,1,n) range.push_back(make_pair(minVal[i],maxVal[i]));
    sort(ALL(range),greater<pair<int,int> >());
    FenwickTree bit(MAX);
    int j=0;
    int res=0;
    FORD(i,MAX-1,0) {
        while (j<range.size() && range[j].fi>=i) {
            bit.update(range[j].se+1,1);
            j++;
        }
        res=max(res,bit.get(min(MAX,i+allow+1)));
    }
    printf("Case #%d: %d\n",tc,res);
}
int main(void) {
    int t;
    scanf("%d",&t);
    FOR(i,1,t) {
        loadTree();
        process(i);
    }
    return 0;
}

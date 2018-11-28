#include<bits/stdc++.h>
#define MAX   1111
#define FOR(i,a,b) for (int i=(a);i<=(b);i=i+1)
#define REP(i,n) for (int i=0;i<(n);i=i+1)
#define FORE(i,v) for (__typeof((v).begin()) i=(v).begin();i!=(v).end();i++)
using namespace std;
vector<int> v[MAX];
string a[MAX];
int n,m,cnt,best;
void init(void) {
    cin>>n>>m;
    FOR(i,1,n) cin>>a[i];
    best=-1;
}
int node(const vector<int> &v) {
    if (v.empty()) return (0);
    set<string> s;
    FORE(it,v) FOR(i,1,a[*it].size()) s.insert(a[*it].substr(0,i));
    return (s.size()+1);
}
void update(void) {
    int tmp=0;
    FOR(i,1,m) tmp+=node(v[i]);
    if (tmp>best) {
        best=tmp;
        cnt=1;
    }
    else if (tmp==best) cnt++;
}
void backtrack(int t) {
    FOR(i,1,m) {
        v[i].push_back(t);
        if (t==n) update(); else backtrack(t+1);
        v[i].pop_back();
    }
}
void process(int tc) {
    backtrack(1);
    printf("Case #%d: %d %d\n",tc,best,cnt);
}
int main(void) {
    //freopen("tmp.txt","r",stdin);
    int tc;
    scanf("%d",&tc);
    FOR(i,1,tc) {
        cerr<<"TEST "<<i<<endl;
        init();
        process(i);
    }
    return 0;
}

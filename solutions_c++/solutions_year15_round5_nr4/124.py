#include<bits/stdc++.h>
#define FOR(i,a,b) for (int i=(a),_b=(b);i<=_b;i=i+1)
#define REP(i,n) for (int i=0,_n=(n);i<_n;i=i+1)
#define FORE(i,v) for (__typeof((v).begin()) i=(v).begin();i!=(v).end();i++)
#define ALL(v) (v).begin(),(v).end()
#define fi   first
#define se   second
using namespace std;
multiset<int> splitSet(multiset<int> &s,int x) {
    multiset<int> res;
    while (!s.empty()) {
        int tmp=*s.begin();
        res.insert(tmp);
        s.erase(s.find(tmp));
        s.erase(s.find(tmp+x));
    }
    return (res);
}
void process(int tc) {
    vector<int> res;
    multiset<int> cur;
    int n;
    scanf("%d",&n);
    vector<pair<int,int> > v(n);
    REP(i,n) scanf("%d",&v[i].fi);
    REP(i,n) scanf("%d",&v[i].se);
    FORE(it,v) REP(love,it->se) cur.insert(it->fi);
    while (cur.size()>1) {
        __typeof(cur.begin()) it=cur.begin();
        it++;
        res.push_back(*it);
        cur=splitSet(cur,res.back());
    }
    sort(ALL(res));
    printf("Case #%d:",tc);
    FORE(it,res) printf(" %d",*it); printf("\n");
}
int main(void) {
    int t;
    scanf("%d",&t);
    FOR(i,1,t) process(i);
    return 0;
}

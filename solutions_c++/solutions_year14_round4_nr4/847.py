#include <bits/stdc++.h>
using namespace std;

#define debug(args...) fprintf(stderr,args)

typedef long long lint;
typedef pair<int,int> pii;
typedef pair<lint,lint> pll;

const int INF = 0x3f3f3f3f;
const lint LINF = 0x3f3f3f3f3f3f3f3fll;
const int MAXM = 10, MAXN = 10;
const int MAXQ = 1e5+10;

string s[MAXM];
int ans;
int m,n;
vector<string> v[MAXN];
int q[MAXQ];

map<char,int> node[MAXQ];

int build(int i) {
    int qnode = 1;
    node[0].clear();
    for(string s: v[i]) {
        int at = 0;
        for(char c: s) {
            if(node[at].find(c) == node[at].end()) {
                node[qnode].clear();
                node[at][c] = qnode++;
                at = qnode-1;
            }
            else at = node[at][c];
        }
    }
    return qnode;
}    

void go(int i) {
    if(i == m) {
        for(int a=0;a<n;++a) if(v[a].size() == 0) return;
        /*        printf("0:");
        for(string s: v[0]) printf(" %s",s.c_str());
        printf("\n1:");
        for(string s: v[1]) printf(" %s",s.c_str());
        printf("\n\n");
        */
        int got = 0;
        for(int a=0;a<n;++a)
            got += build(a);
        ans = max(ans, got);
        q[got]++;
        return;
    }
    for(int a=0;a<n;++a) {
        v[a].push_back(s[i]);
        go(i+1);
        v[a].pop_back();
    }
}    

int main() {
    int t=1,T;
    for(scanf("%d",&T);t<=T;++t) {
        memset(q,0,sizeof(q));
        ans = 0;
        scanf("%d%d",&m,&n);
        for(int a=0;a<m;++a) cin >> s[a];
        go(0);
        printf("Case #%d: %d %d\n",t,ans,q[ans]);
    }        
    return 0;
}

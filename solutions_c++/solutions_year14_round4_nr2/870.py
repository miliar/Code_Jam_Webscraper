#include<bits/stdc++.h>
#define MAX   1111
#define FOR(i,a,b) for (int i=(a);i<=(b);i=i+1)
#define REP(i,n) for (int i=0;i<(n);i=i+1)
#define FORE(i,v) for (__typeof((v).begin()) i=(v).begin();i!=(v).end();i++)
#define BIT(x,i) (((x)>>(i))&1)
using namespace std;
const int INF=(int)1e9+7;
int a[MAX],p[MAX],c[MAX];
int n,im,best;
vector<int> v[2];
void init(void) {
    scanf("%d",&n);
    FOR(i,1,n) scanf("%d",&a[i]);
    im=1;
    FOR(i,1,n) if (a[im]<a[i]) im=i;
    best=INF;
}
bool cmpl(int x,int y) {
    return (a[x]<a[y]);
}
bool cmpg(int x,int y) {
    return (a[x]>a[y]);
}
void update(void) {
    sort(v[0].begin(),v[0].end(),cmpl);
    sort(v[1].begin(),v[1].end(),cmpg);
    int j=0;
    FORE(it,v[0]) p[++j]=*it;
    p[++j]=im;
    FORE(it,v[1]) p[++j]=*it;
    FOR(i,1,n) c[i]=i;
    int cur=0;
    FOR(i,1,n) {
        int j;
        for (j=i;j<=n;j=j+1) if (c[j]==p[i]) break;
        assert(j>=i && j<=n);
        for (;j>i;j=j-1) {
            cur++;
            swap(c[j],c[j-1]);
        }
    }
    best=min(best,cur);
    //printf("Res %d\n",cur);
    sort(v[0].begin(),v[0].end());
    sort(v[1].begin(),v[1].end());
}
void backtrack(int t) {
    REP(i,2) {
        if (t!=im) v[i].push_back(t);
        if (t==n) update(); else backtrack(t+1);
        if (t!=im) v[i].pop_back();
    }
}
void process(int tc) {
    backtrack(1);
    printf("Case #%d: %d\n",tc,best);
}
int main(void) {
    //freopen("tmp.txt","r",stdin);
    int tc;
    scanf("%d",&tc);
    FOR(i,1,tc) {
        init();
        process(i);
    }
    return 0;
}

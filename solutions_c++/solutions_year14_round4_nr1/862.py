#include<bits/stdc++.h>
#define MAX   10101
#define FOR(i,a,b) for (int i=(a);i<=(b);i=i+1)
#define REP(i,n) for (int i=0;i<(n);i=i+1)
using namespace std;
int a[MAX];
int n,m;
void init(void) {
    scanf("%d%d",&n,&m);
    FOR(i,1,n) scanf("%d",&a[i]);
    sort(a+1,a+n+1);
}
bool ok(int x) {
    if (2*x<n) return (false);
    int t=n-x;
    FOR(i,1,t) if (a[i]+a[2*t+1-i]>m) return (false);
    return (true);
}
void process(int tc) {
    printf("Case #%d: ",tc);
    int l=0;
    int r=n;
    while (true) {
        if (l==r) {
            printf("%d\n",l);
            return;
        }
        if (r-l==1) {
            if (ok(l)) printf("%d\n",l);
            else printf("%d\n",r);
            return;
        }
        int m=(l+r)>>1;
        if (ok(m)) r=m; else l=m+1;
    }
}
int main(void) {
    int tc;
    scanf("%d",&tc);
    FOR(i,1,tc) {
        init();
        process(i);
    }
    return 0;
}

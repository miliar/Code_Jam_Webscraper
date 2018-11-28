#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <string>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
using namespace std;
#define FOR(i, a, b) for(int i=a; i<=b; i++)
#define DOW(i, a, b) for(int i=a; i>=b; i--)
#define FOREACH(it, c) for(typeof(c.begin()) it=c.begin(); it!=c.end(); it++)
#define RESET(c, val) memset(c, val , sizeof(c))

#include <conio.h>
#define maxn 1005

int n, m;
int a[maxn], b[maxn], p[maxn];
int x[maxn*3];
set<int> se;
map<int, int> mm;
long long f[maxn*3];
int test;

long long get(int k) {
    k--;
    return 1LL*n*(k+1)-1LL*(k+1)*k/2;
}
long long cal(int u, int v, int cc) {
    if (u==v) return 0;
    int Min=u;
    FOR(i, u, v-1) if (f[i]<f[Min]) Min=i;
    return cal(u, Min, f[Min])+cal(Min+1, v, f[Min])
          +1LL*(f[Min]-cc)*get(x[v]-x[u]);
}
int main() {
    freopen("r2_a.in", "r", stdin);
    freopen("test.out", "w", stdout);
    cin >> test;
    FOR(t, 1, test) {
        cin >> n >> m;
        se.clear(); mm.clear();
        long long rr=0;
        FOR(i, 1, m) {
            scanf("%d%d%d", &a[i], &b[i], &p[i]);
            rr+=1LL*p[i]*get(b[i]-a[i]);
            se.insert(a[i]); se.insert(b[i]);
        }
        int ns=0;
        FOREACH(it, se) ns++, mm[*it]=ns, x[ns]=*it;
        RESET(f, 0);
        FOR(i, 1, m) 
            FOR(j, mm[a[i]], mm[b[i]]-1) f[j]+=p[i];
        long long res=cal(1, ns, 0);
        printf("Case #%d: ", t);
        cout << rr-res << endl;
    }
    getch();
    return 0;
}

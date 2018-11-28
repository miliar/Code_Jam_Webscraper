#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <string>
using namespace std;
#define FOR(i, a, b) for(int i=a; i<=b; i++)
#define DOW(i, a, b) for(int i=a; i>=b; i--)
#define FOREACH(it, c) for(typeof(c.begin()) it=c.begin(); it!=c.end(); it++)
#define RESET(c, val) memset(c, val , sizeof(c))

int test, m, n, a[105][105];

bool check(int i, int j) {
    bool k1=false, k2=false;
    FOR(k, 1, n) if (a[i][k]>a[i][j]) k1= true;
    FOR(k, 1, m) if (a[k][j]>a[i][j]) k2= true;
    return k1&&k2;
}
int main() {
    freopen("b1.in", "r", stdin);
    freopen("test.out", "w", stdout);
    cin >> test;
    FOR(t, 1, test) {
        scanf("%d%d", &m, &n);
        FOR(i, 1, m) FOR(j, 1, n) scanf("%d", &a[i][j]);
        bool flag=true;
        FOR(i, 1, m) FOR(j, 1, n) if (check(i, j)) flag=false;
        if (flag) printf("Case #%d: YES\n", t);
        else printf("Case #%d: NO\n", t);
    }
    //system("pause");
    return 0;
}

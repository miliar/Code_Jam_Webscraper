#include <iostream>
#include <cstring>
#include <cstdio>
#include <queue>
#include <cmath>
#include <algorithm>
using namespace std;
bool is(long long x)
{
    char g[15];
    int n = 0;
    while (x) {
        g[n++] = x%10;
        x/=10;
    }
    for(int i=0, j=n-1;i<=j;i++,j--)
        if (g[i]!=g[j]) return false;
    return true;
}
int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("test.out", "w", stdout);
    int Case;
    scanf("%d", &Case);
    for(int ca=1;ca<=Case;ca++) {
        printf("Case #%d: ", ca);
        long long a, b, ans = 0;
        cin >> a >> b;
        for(long long i=sqrt(a)-1;i<=b;i++) {
            if (i*i > b) break;
            if (i*i < a) continue;
            if (is(i) && is(i*i)) ans++;
        }
        cout << ans << endl;
    }
    return 0;
}

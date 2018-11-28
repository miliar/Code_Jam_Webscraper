#include <iostream>
#include <cstdio>

using namespace std;

int a[1111];

inline void solve(int cs){
    int n;
    scanf("%d ", &n); n++;
    for(int i = 0; i < n; i++) a[i] = getchar()-'0';
    getchar();
    int sum = 0, ans = 0;
    for(int i = 0; i < n; i++)
        if (i > sum) ans += i-sum, sum += a[i] + i-sum; else sum += a[i];
    printf("Case #%d: %d\n", cs, ans);
}

int main(int argc, const char * argv[]) {
    freopen("1.in", "r", stdin);
    freopen("1.out", "w", stdout);
    int ttt;
    scanf("%d", &ttt);
    for(int cs = 1; cs <= ttt; cs++) solve(cs);
    return 0;
}

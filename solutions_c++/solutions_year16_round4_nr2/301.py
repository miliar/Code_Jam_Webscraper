#include "iostream"
#include "algorithm"
#include "vector"
#include "set"
#include "map"
#include "cstring"
#include "string"
#include "vector"
#include "cassert"
#include "queue"
#include "cstdio"
#include "cstdlib"
#include "ctime"
#include "cmath"
#include "bitset"

using namespace std;

typedef long long ll;
typedef pair < int, int > ii;

const int N = 200 + 5;

int n, k;
double a[N], b[N], dp[N][N * 2];

double calc() {
    dp[0][0 + N] = 1;
    for(int i = 1; i <= k; i++)
        for(int dif = -i; dif <= +i; dif++)
            dp[i][dif + N] = dp[i - 1][dif - 1 + N] * a[i] + dp[i - 1][dif + 1 + N] * (1 - a[i]);
    return dp[k][0 + N];
}

void solve() {
    scanf("%d %d", &n, &k);
    for(int i = 1; i <= n; i++)
        scanf("%lf", b + i);
    sort(b + 1, b + n + 1);
    double ans = 0;
    for(int i = 0; i <= k; i++) {
        int c = 0;
        for(int it = 0; it < i; it++)
            a[++c] = b[1 + it];
        for(int it = 0; it < k - i; it++)
            a[++c] = b[n - it];
        ans = max(ans, calc());
    }
    printf("%.12lf\n", ans);
}

int main () {
    
    freopen("B-large.in.txt", "r", stdin);
    freopen("hardB.txt", "w", stdout);
    
    int tt;
    
    scanf("%d", &tt);
    
    for(int it = 1; it <= tt; it++) {
        printf("Case #%d: ", it);
        solve();
    }
    
    return 0;
    
}
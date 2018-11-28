#include <cstdio>
#include <algorithm>
using namespace std;

const int N = 1000010;

int dp[N];

int reverse(int x) {
    int y = x, c = 0, p;
    long long t = 1, res = 0;
    while(y > 0) y /= 10, c++, t *= 10;
    t /= 10;
    for(int i = 0; i < c; i++) {
        p = x % 10, res += p * t, t /= 10, x /= 10;
    }
    return res;
}

int main() {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    int _;
    for(int i = 0; i < N; i++) dp[i] = 1000000000;
    dp[1] = 1;
    for(int i = 2; i < N; i++) {
        int t = reverse(i);
        //printf("%d\n", t);
        dp[i] = min(dp[i], dp[i - 1] + 1);
        if(t <= i || t >= N) continue;
        dp[t] = min(dp[t], dp[i] + 1);
    }
    scanf("%d", &_);
    int p = 0;
    while(_--) {
        int x;
        scanf("%d", &x);
        printf("Case #%d: %d\n", ++p, dp[x]);
    }

    return 0;
}

#include <cstdio>
#include <algorithm>
#include <set>
#define scanf(args...) (scanf(args) ? : 0)
const int MAXN = 1005;

int test, T[MAXN], value[MAXN];

void testCase() {
    test++;

    int n;
    scanf("%d", &n);

    for (int i=0; i<n; i++)
        scanf("%d", &T[i]);
    std::sort(T, T+n);

    int res = T[n-1];
    for (int i=1; i<=T[n-1]; i++) {
        int cnt = i;
        for (int j=0; j<n; j++)
            cnt += ((T[j]+i-1)/i)-1;
        res = std::min(res, cnt);
    }
    
    printf("Case #%d: %d\n", test, res);
}

int main() {
    int t;
    scanf("%d", &t);

    while (t--) {
        testCase();
    }
}

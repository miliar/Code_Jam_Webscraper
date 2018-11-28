#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <stack>
#include <bitset>
#define INF 0x3f3f3f3f
#define eps 1e-8
#define FI first
#define SE second
using namespace std;
typedef long long ll;

int n, J;

int ans[60];

int main() {
    freopen("C-large.in", "r", stdin);
    freopen("C.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int cas = 1; cas <= T; ++ cas) {
        printf("Case #%d:\n", cas);
        scanf("%d%d", &n, &J);
        int m = (n - 2) / 2;
        for(int i = 0; i < J; ++ i) {
            memset(ans, 0, sizeof(ans));
            ans[n - 1] = ans[0] = 1;
            for(int k = 0; k < m; ++ k) {
                if(~i >> k & 1) continue;
                int p = n - 2 - k * 2;
                ans[p] = ans[p - 1] = 1;
            }
            for(int i = n - 1; i >= 0; -- i) {
                printf("%d", ans[i]);
            }
            for(int i = 2; i <= 10; ++ i) {
                if(i & 1) {
                    printf(" %d", 2);
                } else {
                    printf(" %d", i + 1);
                }
            }
            puts("");
        }
    }
    return 0;
}

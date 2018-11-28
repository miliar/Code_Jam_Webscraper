#include <bits/stdc++.h>
using namespace std;

int nTest;
int d, p[1010];

int main() {

    freopen("B-large.in", "r", stdin);
    freopen("B_out.txt", "w", stdout);

    scanf("%d", &nTest);
    for (int test = 1; test <= nTest; test++) {
        scanf("%d", &d);
        for (int i = 1; i <= d; i++) 
            scanf("%d", p + i);

        int ret = 1e9;
        for (int max_p = 1; max_p <= 1000; max_p++) {
            int t_ret = max_p;
            for (int i = 1; i <= d; i++)
                t_ret += (p[i] - 1) / max_p;
            ret = min(ret, t_ret);
        }
        printf("Case #%d: %d\n", test, ret);
    }

    return 0;
}
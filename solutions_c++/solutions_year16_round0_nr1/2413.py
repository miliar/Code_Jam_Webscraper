#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("D://A-large.in", "r", stdin);
    freopen("D://A.out", "w", stdout);
    int t;
    scanf("%d", &t);
    for(int ca = 1; ca <= t; ++ca) {
        int check[10];
        for(int i = 0; i < 10; ++i) check[i] = 0;
        int n, ans;
        scanf("%d", &n);
        for(int i = 1; i < 100; ++i) {
            int tmp = n * i;
            while(tmp) {
                check[tmp%10] = 1;
                tmp /= 10;
            }
            ans = 1;
            for(int j = 0; j < 10; ++j) if(!check[j]) {
                ans = 0;
                break;
            }
            if(ans) {
                printf("Case #%d: %d\n", ca, n * i);
                break;
            }
        }
        if(!ans) printf("Case #%d: INSOMNIA\n", ca);
    }
    return 0;
}

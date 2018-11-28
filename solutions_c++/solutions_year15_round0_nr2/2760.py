#include<cstdio>
#include<iostream>
#include<cstdlib>

using namespace std;
int p[1010];
int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T = 0, cas = 0;
    scanf("%d", &T);
    while(T--) {
        int D;
        scanf("%d", &D);
        for(int i = 1; i <= D; i++) {
            scanf("%d", &p[i]);
        }
        int ans = 10000000;
        for(int i = 1; i <= 1000; i++) {
            int cnt = 0;
            for(int j = 1; j <= D; j++) {
                if(p[j] > i) {
                    cnt += p[j] / i;
                    if(p[j] % i == 0) {
                        cnt--;
                    }
                }
            }
            ans = min(ans,  cnt + i);
        }
        printf("Case #%d: %d\n", ++cas, ans);
    }
    return 0;
}

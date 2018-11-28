#include<cstdio>
#include<iostream>
#include<cstdlib>

using namespace std;
char shy[1010];
int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T = 0, cas = 0;
    scanf("%d", &T);
    while(T--) {
        int sm;
        scanf("%d", &sm);
        scanf("%s", shy);
        int cnt = 0;
        int ans = 0;
        for(int i = 0; i <= sm; i++) {
            int tmp = shy[i] - '0';
            if(cnt >= i) {

            } else {
                ans += i - cnt;
                cnt = i;
            }
            cnt += tmp;
        }
        printf("Case #%d: %d\n", ++cas, ans);
    }
    return 0;
}

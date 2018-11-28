#include<cstdio>

int main() {
int ans[1000001];
    for(int i=0; i<=1000000; i++) {
        int used = 0;
        for(int j=1; j<=1000; j++) {
            int tmp = i*j;
            while(tmp) {
                used |= 1<<(tmp%10);
                tmp /= 10;
            }
            if(used == (1<<10) - 1) {
                ans[i] = i*j;
                break;
            }
        }
        if(used != (1<<10) - 1)
            ans[i] = -1;
    }
    int t;
    scanf("%d", &t);
    for(int ca=1; t--; ca++) {
        int n;
        scanf("%d", &n);
        if(~ans[n])
            printf("Case #%d: %d\n", ca, ans[n]);
        else
            printf("Case #%d: INSOMNIA\n", ca);
    }
    return 0;
}

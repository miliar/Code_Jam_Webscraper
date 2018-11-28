#include <cstdio>

int main() {
    int tc, n; scanf("%d",&tc);
    char str[1024];
    for(int tt=1; tt<=tc; tt++) {
        scanf("%d%s",&n,str);
        int cnt = str[0]-'0', inv = 0;
        for(int i=1; i<=n; i++) {
            if(str[i] == '0') continue;
            if(cnt <= i) {
                inv += i-cnt;
                cnt += inv;
            }
            cnt += str[i]-'0';
        }
        printf("Case #%d: %d", tt, inv);
        if(tt < tc) printf("\n");
    }
    return 0;
}
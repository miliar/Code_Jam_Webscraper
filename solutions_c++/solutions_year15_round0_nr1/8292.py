#include <cstdio>
int main() {
    int T;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d", &T);
    for (int cs = 1; cs<= T; cs++) {
        int max;
        scanf("%d", &max);
        char str[max+1];
        int ans = 0, current = 0;
        scanf("%s", str);
        for (int i = 0; i<=max; i++) {
            while (1) {
                if (current >= i) {
                    current += (str[i]-'0');
                    break;
                }
                else {
                    ans++;
                    current++;
                }
            }
        }
        printf("Case #%d: %d\n",cs,ans);
    }
    return 0;
}

#include <stdio.h>

char str[1005];

int main() {
    freopen("/Users/wenzhengjiang/A-large.in", "r", stdin);
    freopen("/Users/wenzhengjiang/A-large.out", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int ncase = 1; ncase <= t; ncase++) {
        int smax;
        scanf("%d%s", &smax, str);
        int cur_pep = 0, added_pep = 0;
        for (int i = 0; i <= smax; ++i) {
            if ( cur_pep < i) {
                added_pep += i - cur_pep;
                cur_pep = i;
            }
            cur_pep += str[i] - '0';
        }
        printf("Case #%d: %d\n",ncase, added_pep);
    }
    fclose(stdout);
}
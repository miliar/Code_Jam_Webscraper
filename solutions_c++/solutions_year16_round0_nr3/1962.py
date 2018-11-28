#include <cstdio>
#include <cstring>
#include <string>
typedef long long LL;
const int length = 14;
int num = 0;
LL n, j;
char str[50];
void DFS(int idx) {
    if(idx == length) {
        num++;
        printf("1");
        printf("%s", str);
        printf("11");
        printf("%s", str);
        printf("1");
        for(int i = 2; i <= 10; i++) {
            LL ans = 1;
            for(int k = 0; k < length; k++) {
                ans = ans * i + (str[k] - '0');
            }
            ans = ans * i + 1;
            printf(" %lld", ans);
        }
        printf("\n");
        return;
    }
    if(num == j) return;
    str[idx] = '0';
    DFS(idx + 1);
    str[idx] = '1';
    DFS(idx + 1);
}

int main() {
//    freopen("C-large.in", "r", stdin);
//    freopen("C-large.out", "w", stdout);
    int T, tcase = 1;
    scanf("%d", &T);
    while(T--) {
        scanf("%lld%lld", &n, &j);
        printf("Case #%d:\n", tcase++);
        DFS(0);
    }
    return 0;
}

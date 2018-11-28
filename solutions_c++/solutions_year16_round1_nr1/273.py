#include <bits/stdc++.h>
using namespace std;
const int N = 1005;

int n;
char str[N];
bool f[N];
void work() {
    scanf("%s" , str);
    n = strlen(str);
    memset(f , 0 , sizeof(f));
    int R = n - 1;
    while (R >= 0) {
        int mx = 0;
        for (int i = 0 ; i <= R ; ++ i) {
            mx = max(mx , (int)str[i]);
        }
        if (mx < str[0])
            break;
        for (int i = R ; i >= 0 ; -- i) {
            if (str[i] == mx) {
                f[i] = 1;
                putchar(str[i]);
                R = i - 1;
            }
        }
    }
    for (int i = 0 ; i < n ; ++ i)
        if (!f[i])
            putchar(str[i]);
    puts("");
}

int main() {
    int T , ca = 0;
    scanf("%d" , &T);
    while (T --) {
        printf("Case #%d: " , ++ ca);
        work();
    }
    return 0;
}

#include <bits/stdc++.h>
using namespace std;


int CAS, n, m;

int s[32], t[32];

int check(int s[], int base) {
    long long x = 0, p = 1;
    for (int i = 0; i < 16; i++) {
        x += p * s[i];
        p *= base;
    }
    for (long long i = 2; i * i <= x; i++)
    if (x % i == 0) return i;
    return 0;
}


int main(){
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &CAS);
    for (int cas = 1; cas <= CAS; cas++) {
        scanf("%d%d", &n, &m);
        printf("Case #%d:\n", cas);
        for (int i = 0; i < (1 << n - 2); i++) {
            memset(s, 0, sizeof(s));
            s[0] = 1;
            s[n - 1] = 1;
            for (int j = 0; j < n - 2; j++){
                if (i >> j & 1) s[j + 1] = 1;
            }
            int flag = 0;
            for (int j = 2; j <= 10; j++)
            if ((t[j] = check(s, j)) == 0) {
                flag = 1;
                break;
            }
            if (!flag) {
                for (int j = n - 1; j >= 0; j--)
                    printf("%d", s[j]);
                for (int j = 2; j <= 10; j++)
                    printf(" %d", t[j]);
                puts("");
                if (--m == 0) break;
            }
        }
    }
}

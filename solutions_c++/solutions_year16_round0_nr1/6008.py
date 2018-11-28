#include <bits/stdc++.h>
using namespace std;

int CAS, n;

int v[10];


int main(){
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &CAS);
    for (int cas = 1; cas <= CAS; cas++) {
        scanf("%d", &n);
        printf("Case #%d: ", cas);
        if (n == 0) {
            puts("INSOMNIA");
            continue;
        }
        int y = n;
        memset(v, 0, sizeof(v));
        while (1) {
            int x = y;
            do{
                v[x % 10] = 1;
                x /= 10;
            }while (x);
            int flag = 0;
            for (int i = 0; i < 10; i++) {
                if (!v[i]) {
                    flag = 1;
                }
            }
            if (!flag) {
                printf("%d\n", y);
                break;
            }
            y += n;
        }
    }
}

#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
int ok[10];
int f[1100000];
int main(){
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    for (int i = 1; i <= 1000000; ++ i){
        int now = i;
        memset(ok, 0, sizeof ok);
        while (1){
            int tmp = now;
            while (tmp){
                ok[tmp % 10] = 1;
                tmp /= 10;
            }
            int flag = 1;
            for (int i = 0; i < 10; ++ i) if (!ok[i]) flag = 0;
            if (flag) break;
            now += i;
        }
        f[i] = now;
        assert(now >= 0);
    }
    int t; scanf("%d", &t);
    while (t--){
        int n;
        static int ca = 0;
        printf("Case #%d: ", ++ ca);
        scanf("%d", &n);
        if (n == 0){
            puts("INSOMNIA");
        }else{
            printf("%d\n", f[n]);
        }
    }
}

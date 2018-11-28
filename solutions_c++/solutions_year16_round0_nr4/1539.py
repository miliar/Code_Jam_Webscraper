#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

int k, c, s;
ll f[110];
int main(){
    //freopen("in.txt", "r", stdin);
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);

    int t; scanf("%d", &t);
    while (t--){
        static int ca = 0;
        printf("Case #%d:", ++ ca);
        scanf("%d %d %d", &k, &c, &s);
        int cc = c - 1;
        if ((1ll << cc) * s < k){
            printf(" IMPOSSIBLE\n");
            continue;
        }
        if (s == k){
            for (int i = 1; i <= s; ++ i) printf(" %d", i);
            puts("");
            continue;
        }
        f[0] = 1;
        for (int i = 1; i <= c; ++ i) f[i] = f[i - 1] * k;
        ll now = 0, id = 0;
        ll del = 0;
        while (s){
            id = 0;
            for (int i = 0; i < c; ++ i){
                id = id * k + min(k,(1 << i));
                if (id >= f[c]) break;
             //   printf("p %I64d\n", id);
            }
            id = id + del;
            if (id >= f[c]) id = f[c];
            s--;
            printf(" %I64d", id);
            if (id == f[c]) break;
            del += (1ll << cc);
        }
        //now = 2;
        //while (s--) printf(" %I64d", now++);
        puts("");
    }
}

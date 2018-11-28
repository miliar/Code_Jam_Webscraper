#include <cstdio>
#include <cstring>
#include <iostream>
#include <cmath>
#include <vector>
#include <map>
#include <algorithm>
#include <cstdlib>
#define LL long long

int T;
bool out[55][55];
int b, use[55];
LL m, k;

void solve(){
    scanf("%d%lld", &b, &m);
    memset(out, 0, sizeof(out));
    memset(use, 0, sizeof(use));
    k = (1 << (b - 2));
    if (m > k){
        printf("IMPOSSIBLE\n");
        return;
    }else{
        printf("POSSIBLE\n");
        int j = 1;
        bool sp = (k == m);
        if (!sp){
            for (LL i = 1; i <= m; i <<= 1, j++){
                if (sp || (m & i) > 0) use[j] = 1;
                else use[j] = 0;
            }
            for (int i = 0; i < b - 1; i++){
                for (int j = 0; j < b - 1; j++){
                    if (i < j) out[i][j] = 1;
                    else out[i][j] = 0;
                }
                out[i][b - 1] = use[i];
            }
        }else{
           for (int i = 0; i < b - 1; i++){
                for (int j = 0; j < b; j++){
                    if (i < j) out[i][j] = 1;
                    else out[i][j] = 0;
                }
            }           
        }
        for (int i = 0; i < b; i++){
            for (int j = 0; j < b; j++){
                printf("%d", out[i][j]);
            }
            printf("\n");
        }
    }
}

int main(){
    scanf("%d", &T);
    for (int i = 1; i <= T; i++){
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}

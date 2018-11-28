#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#define LL long long

using namespace std;

LL proof(LL num){
    LL ret = -1;
    for(LL i = 2; i * i <= num; i++){
        if(num % i == 0){
            ret = i;
            break;
        }
    }
    return ret;
}

LL code(LL num, int base){
    LL ret = 0, add = 1;
    for(; num; add *= base, num >>= 1){
        if(num & 1) ret += add;
    }
    return ret;
}

void print(LL i){
    int b[19];
    int cnt = 0;
    while(i){
        b[cnt++] = (i & 1);
        i >>= 1;
    }
    for(int i = cnt - 1; i >= 0; i--) printf("%d", b[i]);
}



int main(void){
    int T, kase = 0;
    scanf("%d", &T);
    while(T--){
        int N, J, cnt = 0;
        scanf("%d %d", &N, &J);
        printf("Case #%d: \n", ++kase);
        int maxn = (1 << 16) - 1;
        for(int i = (1 << 15) + 1; i <= maxn; i++){
             if(!(i & 1)) continue;
             bool flg = true;
             LL num, ret;
             LL prf[11];
             for(int k = 2; k <= 10; k++){
                 num = code(i, k);
                 ret = proof(num);
                 if(ret == -1){ flg = false; break; }
                 prf[k] = ret;
             }
             if(flg){
                 print(i);
                  printf(" ");
                  for(int q = 2; q <= 10; q++){
                      printf("%lld ", prf[q]);
                  }
                  puts("");
                  cnt++;
             }
             if(cnt == J) break;
        }
    }
    return 0;
}


#include "iostream"
#include "cstring"
#include "cstdio"
using namespace std;
const int N = 110;
int a[N], factor[11];
const int PRIMERANGE = 100000010;
int prime[PRIMERANGE + 1];
int getPrime()
{
    for (int i = 2; i <= PRIMERANGE; ++ i){
        if (!prime[i]) prime[++prime[0]] = i;
        for (int j = 1; j <= prime[0] && prime[j] <= PRIMERANGE / i; ++j){
            prime[prime[j] * i] = 1;
            if (i % prime[j] == 0) break;
        }
    }
    return prime[0];
}
int main(void)
{
    getPrime();
    int T;
    scanf("%d", &T);
    int g = 0, n, m;
    while(T--){
        printf("Case #%d:\n", ++g);
        scanf("%d %d", &n, &m);
        for(int i = 0; i < (1 << n); ++ i){
            if (m == 0) break;
            for(int j = 0; j < n; ++ j){
                if ((1 << j) & i){
                    a[j] = 1;
                }else{
                    a[j] = 0;
                }
            }
            if(a[0] == 0 || a[n - 1] == 0) continue;
            bool flag = 0;
            long long value = 0;
            for(int j = 2; j <= 10; ++ j) {
                value = 0;
                for (int k = 0; k < n; ++ k){
                    value = value * j + a[k];
                }
                bool hasfactor = false;
                for(int k = 1; k <= prime[0]; ++k){
                    if(value % prime[k] == 0 && value != prime[k]){
                        hasfactor = true;
                        factor[j] = prime[k];
                        break;
                    }
                }
                if (!hasfactor){
                    flag = 1;
                    break;
                }
            }
            if (flag) continue;
            for(int j = 0; j < n; ++ j){
                printf("%d", a[j]);
            }
            for(int j = 2; j <= 10; ++ j){
                printf(" %d", factor[j]);
            }
            printf("\n");
            m --;

        }
    }
    return 0;
}
#include <algorithm>
#include <iostream>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdio.h>
#include <utility>
#include <math.h>
#include <time.h>
#include <vector>
#include <queue>
#include <set>
#include <map>
using namespace std;

const int N = 16;
const int J = 50;
typedef __int64 LL;
const int maxn = 1000;
const int prin = 500;

int prime[prin];
///仅包含奇数，isprime[k]代表2*k+3
bool isprime[maxn>>1];
int ptop = 0;

void sieve() {
    memset(isprime, true, sizeof(isprime));
    prime[0] = 2;
    int sq = sqrt(maxn);
    for(int i = 3; i < maxn; i += 2) {
        if(isprime[(i-3)>>1]) {
            if(i <= sq+3) {
                for(int j = i*i; j < maxn; j += 2*i)
                    isprime[(j-3)>>1] = false;
            }
            prime[++ptop] = i;
        }
    }
    return ;
}

int dig[40];
LL base[20][40];
int fac[20];

LL getNumber(int k) {
    LL ret = 0;
    for(int i = 0; i < N; i++)
        ret += base[k][i] * dig[i];
    return ret;
}
int cnt;
void work(int k, int len) {
    if(cnt >= J) exit(0);
    if(k == len) {
        for(int i = 2; i <= 10; i++) {
            LL p = getNumber(i);
//            cout << p << endl;
            int tmp = 0;
            while((tmp < ptop) && (p > prime[tmp]) && (p % prime[tmp])) tmp++;
            if(tmp >= ptop || (p <= prime[tmp])) return ;
            fac[i] = prime[tmp];
        }
        for(int i = 0; i < N; i++)
            printf("%d", dig[i]);
        for(int i = 2; i <= 10; i++)
            printf(" %d", fac[i]);
        printf("\n");
        cnt++;
        return ;
    }
    dig[k] = 1;
    work(k+1, len);
    dig[k] = 0;
    work(k+1, len);
}

int main() {
//    freopen("C-small.out", "w", stdout);
    puts("Case #1:");
    for(int i = 2; i <= 10; i++)
        base[i][0] = 1;
    for(int i = 2; i <= 10; i++)
        for(int j = 1; j < N; j++)
            base[i][j] = base[i][j-1] * i;
    for(int i = 2; i <= 10; i++)
        reverse(base[i], base[i] + 16);
    sieve();
    memset(dig, 0, sizeof dig);
    dig[0] = dig[N-1] = 1;
    cnt = 0;
    work(1, N-1);
    return 0;
}

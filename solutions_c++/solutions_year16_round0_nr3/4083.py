#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <string.h>

using namespace std;
long long a[20];
long long ans[11];
int N;
long long interpret(long long b) {
    long long num = 0;
    for(int i = 0; i < N; i++) {
        num = num * b + a[i];
    }
    return num;
}

long long isPrime(long long x) {
    for(long long i = 2; i * i <= x; i++) {
        if(x % i == 0)return i;
    }
    return 0;
}

long long judge(){
    for(long long i = 2; i <= 10; i++) {
        long long x = interpret(i);
        long long num = isPrime(x);
        if(!num)return 0;
        ans[i-2] = num;
    }
    return 1;
}

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int t;
    scanf("%d",&t);
    for (int ca = 1; ca <= t; ca++) {
        int J;
        scanf("%d %d",&N, &J);
        printf("Case #%d:\n",ca);
        long long s = 1LL << (N-2);
        int _count = 0;
        for(long long i = 0; i < s; i++) {
            memset(a,0,sizeof(a));
            a[0] = 1; a[N-1] = 1;
            for(long long j = 0; j < N-2; j++) {
                if(i & (1LL << j)) {
                    a[N-2-j] = 1;
                }
            }
            if(judge()) {
                for(int j = 0; j < N; j++) {
                    printf("%lld",a[j]);
                }
                for(long long j = 0; j < 9; j++) {
                    printf(" %lld", ans[j]);
                }
                printf("\n");
                _count++;
            }
            if(_count == J)break;
        }

    }
    return 0;
}

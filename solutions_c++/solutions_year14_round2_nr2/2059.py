#include<stdio.h>
#include<string>
#include<math.h>
#include<stdlib.h>
#include<set>
#include<bitset>
#include<map>
#include<vector>
#include<string.h>
#include<algorithm>
#include<iostream>
#include<list>
#define RI(X) scanf("%d", &(X))
#define RII(X, Y) scanf("%d%d", &(X), &(Y))
#define RIII(X, Y, Z) scanf("%d%d%d", &(X), &(Y), &(Z))
#define DRI(X) int (X); scanf("%d", &X)
#define DRII(X, Y) int X, Y; scanf("%d%d", &X, &Y)
#define DRIII(X, Y, Z) int X, Y, Z; scanf("%d%d%d", &X, &Y, &Z)
#define RS(X) scanf("%s", (X))
#define CASET int ___T, case_n = 1; scanf("%d ", &___T); while (___T-- > 0)
using namespace std;

unsigned A, B, K;

int main()
{
    CASET {
        scanf("%u %u %u", &A, &B, &K);
        unsigned C = A;
        if(C > B) C = B;
        
        long long cnt;
        cnt = A * B;
        for(unsigned a = K; a < A; a++){
            for(unsigned b = K; b < B; b++){
                if( (a & b) >= K ) cnt--;
            }
        }
        printf("Case #%d: %ld\n", case_n++, cnt);
    }
    return 0;
}


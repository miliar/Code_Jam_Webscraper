#include <iostream>
#include <string>
#include <string.h>
#include <cstdio>
#include <bitset>

#define LL long long
using namespace std;
const int maxn = 105;

int n, j;

char * gao(int m){
    static char s[100];
    s[0] = s[n-1] = '1'; s[n] = 0;
    for(int i=1;i<=(n-2)/2;i++){
        s[i*2-1] = s[i*2] = '0' + (m&1);
        m >>= 1;
    }
    return s;
}

// (x^d+1) % (d+1)
int main(){

    int t; scanf("%d", &t);
    for(int it=1;it<=t;it++){
        scanf("%d%d", &n, &j);
        printf("Case #%d:\n", it);
        
        int m = 0;
        for(int i=1;i<=j;i++){
            printf("%s ", gao(m) );

            for(int k=1;k<=9;k++){
                printf(" %d", k+2 );
            }
            puts("");

            m++;
        }
    }


    return 0;
}
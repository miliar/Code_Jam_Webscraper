/*
 */
#include <cassert>
#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <cmath>
#include <vector>
using namespace std;
#define oo 0xfffffffful
#define N 0x400

int n,ts,cs,p[N];
unsigned int z[N];
char s[0x400];

int main() {
    int i,j,k;
    for ( scanf("%d",&ts); ts--; ) {
        scanf("%d %s",&n,s);
        printf("Case #%d: ",++cs);
        for ( i = 0; i <= n; ++i ) {
            p[i] = s[i]-'0';
            if ( i ) p[i] += p[i-1];
            z[i] = +oo;
        }
        for ( z[0] = 0, i = 1; i <= n; ++i ) {
            if ( z[i-1]+p[i-1] >= i )
                z[i] = z[i-1];
            else {
                z[i] = z[i-1] + (i-z[i-1]-p[i-1]);
            }
        }
        printf("%u\n",z[n]);
    }
    return 0;
}


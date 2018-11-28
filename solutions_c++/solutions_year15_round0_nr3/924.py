#include <stdio.h>
#include <algorithm>
#include <string.h>
#include <limits.h>
#include <math.h>
#include <vector>
using namespace std;

typedef long long LL;

const LL N = 20000+10;
char s[N];
LL n,value, m;

const LL matrix[5][5] = {
    {0,0,0,0,0},
    {0,1,2,3,4},
    {0,2,-1,4,-3},
    {0,3,-4,-1,2},
    {0,4,3,-2,-1}

};

LL ord(char c) {
    switch(c) {
        case 'i': return 2;
        case 'j': return 3;
        case 'k': return 4;
    }
}

LL calc(LL x,LL y) {
    LL k = x*y<0?-1:1;
    x = x<0?-x:x;
    y = y<0?-y:y;
    return matrix[x][y]*k;
}

LL left;
LL right;

void init() {
    left = INT_MAX;
    right = INT_MAX;
    value = 1;
    for(LL i = 0 ; i < n ; ++i) {
        value = calc(value,ord(s[i]));
    }
}

bool work() {
    LL check = 1;
    for(LL i = 0 ; i < m%4 ; ++i)check = calc(check,value);
    if(check != -1)return false;


    LL q = 1;
    for(LL i = 0 ; i < n ; ++i) {
        q = calc(q,ord(s[i]));
        LL p = 1;
        for(LL j = 0 ; j < 4 ; ++j) {
            if(calc(p,q) == 2) {

                left = min(left, j*n+i+1);
            }
            p = calc(p,value);
        }
    }


    q = 1;
    for(LL i = n-1; i >=0 ; --i) {
        q = calc(ord(s[i]),q);
        LL p = 1;
        for(LL j = 0 ; j < 4 ; ++j) {

            if(calc(q,p) == 4) {
                right = min(right,j*n+n-i);
            }
            p = calc(value,p);
        }
    }
    return left+right < n*m;
}

int main() {
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    LL T;
    scanf("%I64d",&T);
    for(LL cas = 1 ; cas <= T ; ++cas) {
        scanf("%I64d%I64d",&n,&m);
        scanf("%s",s);
        init();
        printf("Case #%I64d: %s\n", cas, work()?"YES":"NO");
    }
}

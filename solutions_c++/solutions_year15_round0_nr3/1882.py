#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <math.h>
#include <vector>
#include <string>
#include <queue>
#include <iostream>
using namespace std;

bool fless(double a,double b){ return b-a>1e-6; }
bool fequal(double a,double b){ return fabs(b-a)<=1e-6; }

#define MAXL 100010

#define I 2
#define J 3
#define K 4

int mul(int a, int b) {
    if (a == 1 || b == 1) return a * b;
    if (a == b) return -1;

    if (a < 0) return -1 * mul(-a, b);
    if (b < 0) return -1 * mul(a, -b);

    if (a == I && b == J) return K;
    if (a == I && b == K) return -J;

    if (a == J && b == I) return -K;
    if (a == J && b == K) return I;

    if (a == K && b == I) return J;
    if (a == K && b == J) return -I;

    printf("error!\n");
    return 0;

}

int val(char c) {
    if (c == 'i') return I;
    if (c == 'j') return J;
    return K;
}


int main(){
    int tt; scanf("%d",&tt);
    for (int ti=1;ti<=tt;ti++){
            
        int L, X; scanf("%d%d", &L, &X);
        char s[MAXL]; scanf("%s", s);

        for (int i=1, p=L;i<X;i++) {
            for (int j=0;j<L;j++) {
                s[p++] = s[j];
            }
        }
        int n = L*X;
        s[n] = 0;
        
        int curr = 1;
        bool hasI = false, hasJ = false;
        for (int i=0; i<n; i++) {
            curr = mul(curr, val(s[i]));
            if (!hasI) {
                hasI = (curr == I);
            } else if (!hasJ) {
                hasJ = (curr == K);
            }
        }

        bool ans = hasI && hasJ && (curr == -1);

        printf("Case #%d: %s\n",ti,ans ? "YES" : "NO");
    }
    return 0;
}

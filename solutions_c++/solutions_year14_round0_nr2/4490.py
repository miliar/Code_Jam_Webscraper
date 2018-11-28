#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <string>
#include <queue>
#include <stack>
#include <cctype>

using namespace std;

double C, Fm, X, S1, S2, S3, F;
int T;

int main(){

    int z, i;

    scanf("%d", &T);
    for (z=1; z<=T; z++) {
        scanf("%lf%lf%lf", &C, &Fm, &X);
        F = 2;
        S1 = X/2;
        S2 = 0;
        while(true) {
            S2 += (C/F);
            F += Fm;
            S3 = S2 + (X/F);
            if(S1 < S3)
                break;
            else {
                S1 = S3;
            }
        }
        printf("Case #%d: %.7lf\n", z, S1);
    }


    return 0;
}

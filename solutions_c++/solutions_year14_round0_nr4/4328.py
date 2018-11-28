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

double A[1004], B[1004];
int T, N, I;

int check() {
    int r, i,j;
    i = j = r = 0;
    for (; i<N; i++) {
        while(A[i]>B[j] && j<N){
            j++;
        }
        if (j==N){
            return N-r;
        }
        r++;
        j++;
    }
    return N-r;
}

int check2() {
    int r, i,j;
    i = j = r = 0;
    for (; i<N; i++) {
        while(B[i]>A[j] && j<N){
            j++;
        }
        if (j==N){
            return r;
        }
        r++;
        j++;
    }
    return r;
}

int main(){

    int z, i,j, a, m, n;
    double x;

    scanf("%d", &T);

    for (z=1; z<=T; z++) {

        scanf("%d", &N);
        for (i=0; i<N; i++) {
            scanf("%lf", &A[i]);
        }
        for (i=0; i<N; i++) {
            scanf("%lf", &B[i]);
        }

        sort(A, A+N);
        sort(B, B+N);

        n = check();

        m =check2();

        printf("Case #%d: %d %d\n", z, m, n);

    }

    return 0;
}

#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

#define Nmax 1024

int N, M, T;
double A[Nmax], B[Nmax];
char W[Nmax];

void war() {
    int scor = 0;
    for (int i=N-1; i>=0; --i) {
        double target = B[i];
        ++scor;
        for (int j=0; j<N; ++j) {
            if (!W[j] && A[j] > target) {
                W[j] = 1;
                --scor;
                break;
            }
        }
    }
    printf("%d\n", scor);
}

void dwar() {
    int scor = 0;
    for (int i=N-1; i>=0; --i) {
        double target = A[i];
        for (int j=0; j<N; ++j)
            if (!W[j] && B[j] > target) {
                W[j] = 1;
                ++scor;
                break;
            }
    }
    printf("%d ", scor);
}

int main() {
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    
    scanf("%d", &T);
    for (int t=1; t<=T; ++t) {
        scanf("%d", &N);
        for (int i=0; i<N; ++i) {
            scanf("%lf", &B[i]);
        }
        for (int i=0; i<N; ++i) {
            scanf("%lf", &A[i]);
        }
        
        printf("Case #%d: ", t);
        sort(A, A+N);
        sort(B, B+N);
        /*
        printf("\n");
        for (int i=0; i<N; ++i)
            printf("%lf ", B[i]);
        printf("\n");
        for (int i=0; i<N; ++i)
            printf("%lf ", A[i]);
        printf("\n");
        */
        memset(W, 0, sizeof(W));
        dwar();
        memset(W, 0, sizeof(W));
        war();
    }
    
    return 0;
}
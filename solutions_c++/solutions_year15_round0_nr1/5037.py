#include <cstdio>
#include <cmath>
#include <cstdlib>

int main ()
{
    int i, j;
    int T;
    int Smax;
    int *S;
    int sum, extra;
    
    scanf("%d\n", &T);
    for (i=0; i<T; i++) {
        scanf("%d ", &Smax);
        S = (int *) malloc((Smax + 1) * sizeof(int));
        for (j=0; j<=Smax; j++) {
            S[j] = getchar() - '0';
        }
        sum = 0;
        extra = 0;
        for (j=0; j<=Smax; j++) {
            if (sum < j) {
                extra += j - sum;
                sum = j;
            }
            sum += S[j];
        }
        printf("Case #%d: %d\n", i+1, extra);
    }
    return 0;
}

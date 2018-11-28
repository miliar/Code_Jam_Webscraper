#include <cstdio>
#include <algorithm>

using namespace std;

int main() {
    int t;

    scanf("%d", &t);

    for ( int ii = 0 ; ii < t; ii++ ) {
        int A, N;
        scanf("%d %d", &A, &N);

        long long sum = A;
        int T[N + 1];
        int res = 0;

        for ( int i = 0 ; i < N ; i++ ) {
            scanf("%d", &T[i]);
        }

        if ( sum == 1 ) {
            res = N;
        } else {
            sort(T, T + N);

            for ( int i = 0; i < N; i++ ) {
    //            printf("sum = %d\n", sum);
                if ( sum > T[i] ) {
                    sum += T[i];
                } else {
                    int x = 0;
                    int tmpSum = sum;
                    
                    while (tmpSum <= T[i]) {
                        x++;
                        tmpSum += (tmpSum - 1);
                    }

    //                printf("add %d times, got %d\n", x, tmpSum);

                    if ( x < N - i ) {
                        res += x;
                        sum = tmpSum + T[i];
                    } else {
                        res += N - i;
                        i = N;
                    }
                    
    //                printf("new res = %d\n", res);
                }
            }
        }

        if ( res > N ) { res = N; }

        printf("Case #%d: %d\n", ii + 1, res);
    }

    return 0;
}

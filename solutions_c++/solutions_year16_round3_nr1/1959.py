#include <cstdio>
#include <iostream>

int main() {
    int T, N, P[26], I[26], max, pos, temp, maxi, posi;
    scanf("%d", &T);
    for (int i=1; i<=T; i++) {
        scanf ("%d", &N);
        for (int j=0; j<N; j++) {
            scanf ("%d", P+j);
            I[j] = j;
        }
        for (int p=0; p<N; p++) {
            max = P[p];
            pos = p;

            maxi = I[p];
            posi = p;
            for (int q=p+1; q<N; q++) {
                if (P[q] > max) {
                    max = P[q];
                    pos = q;

                    maxi = I[q];
                    posi = q;
                }
            }
            if (pos != p) {
                temp = P[p];
                P[p] = max;
                P[pos] = temp;

                temp = I[p];
                I[p] = maxi;
                I[posi] = temp;
            }
        }
        printf ("Case #%d: ", i);
        while (P[0] > P[1]) {
            printf ("%c ", 'A'+I[0]);
            P[0]--;
        }

        for (int p=0; p<N-2; p++) {
            while (P[p+1] > P[p+2]) {
                printf ("%c%c ", 'A'+I[p], 'A' + I[p+1]);
                P[p]--;
                P[p+1]--;
            }
            while (P[p] > 0) {
                printf ("%c ", 'A' + I[p]);
                P[p]--;
            }
        }

        while (P[N-2] >0) {
            printf ("%c%c ", 'A' + I[N-2], 'A'+I[N-1]);
            P[N-2]--;
            P[N-1]--;
        }
        printf ("\n");
    }
    return 0;
}

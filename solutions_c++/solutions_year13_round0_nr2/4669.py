#include <stdio.h>
#include <stdlib.h>

    int T,N,M;
    int H[100][100];
    int X[100];
    int Y[100];

int main(char** arg) {
    freopen("B-large.in","r",stdin);
    freopen("out2.txt","w",stdout);
    scanf("%d",&T);
    for (int t = 1 ; t <= T ; t++){
        printf("Case #%d: ",t);
        scanf("%d %d",&N,&M);
        for (int i = 0 ; i < M ; i++){
            X[i] = 0;
        }
        for (int i = 0 ; i < N ; i++) {
            Y[i] = 0;
        }
        for (int n = 0 ; n < N ; n++){
            for(int m = 0 ; m < M ; m++){
                scanf("%d",&H[n][m]);
                if (H[n][m] > X[m]) {
                    X[m] = H[n][m];
                }
                if(H[n][m] > Y[n]) {
                    Y[n] = H[n][m];
                }
            }
        }
        int b = 1;
        for (int n = 0 ; n < N ; n++){
            for(int m = 0 ; m < M ; m++){
                if (H[n][m] < Y[n] && H[n][m] < X[m]) b = 0;
            }
        }
        if (b == 1) {
            printf("YES");
        }
        else {
            printf("NO");
        }
        printf("\n");
    }
    //for(;;);
}

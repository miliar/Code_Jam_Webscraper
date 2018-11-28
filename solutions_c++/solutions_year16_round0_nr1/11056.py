#include <stdio.h>
#include <stdlib.h>

int main() {
    int T; scanf("%d",&T);
    for (int t=1; t<=T; t++) {
        printf("Case #%d: ",t);

        int num[10] = {};
        int N; scanf("%d",&N);
        if (N==0) {
            printf("INSOMNIA\n");
            continue;
        }

        int aux = N;
        int N_ = N;
        while(1) {
            //printf("N: %d\n",N);
            while(aux>0) {
                int d = aux % 10;
                aux = aux / 10;
                num[d] = 1;
                //printf("Digit: %d\n",d);
            }
            //if (aux == 0) num[0] = 1;
            int count = 0;
            for (int i=0; i<10; i++) {
                count += num[i];
            }
            if (count == 10) {
                printf("%d\n",N);
                break;
            }
            N += N_;
            aux = N;
        }
    }

    return 0;
}

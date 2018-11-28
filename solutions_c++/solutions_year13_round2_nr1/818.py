#include <stdio.h>
#include <stdlib.h>
int T,A,N;
int mote[110];

int compare(const void *_a, const void *_b){
    int *a = (int*)_a;
    int *b = (int*)_b;
    return *a - *b;
}

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&T);
    for (int tt = 1 ; tt <= T ;tt++){
        scanf("%d %d",&A,&N);
        for (int i = 0 ; i < N ; i++) {
            scanf("%d",&mote[i]);
        }
        qsort(mote,N,sizeof(int),compare);
        int ans = N; 
        int I;
        int tmp = N;
        int move = 0;
        for (int i = 0 ; i < N ; i++){
            --tmp;
            while (A <= mote[i]) {
                if (A <= 1) {
                    A = -1;
                    ans = N;
                    break;
                }
                A += A-1;
                move++;
            }
            if (A == -1) {
                break;
            }
            A+= mote[i];
            if (move + tmp < ans) {
                ans = move + tmp;
                I = i;
            }
        }
        printf("Case #%d: %d\n",tt,ans);
    }
}

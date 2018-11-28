#include <stdio.h>

int main () {
    FILE *in = fopen("B.in","r");
    FILE *out = fopen("B.out","w");
    int t,k = 1;
    fscanf (in,"%d",&t);
    while (t --) {
        fprintf (out, "Case #%d: ",k++);
        int A,B,K;
        int ret = 0;
        fscanf (in,"%d %d %d",&A,&B,&K);
        for (int i=0; i<A; i++) {
            for (int j=0; j<B; j++) {
                int tmp = i & j;
                if (tmp < K) ret ++;
            }
        }
        fprintf (out,"%d\n",ret);
    }
}

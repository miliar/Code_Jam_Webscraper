#include <stdio.h>

long long gcd (long long a , long long b) {
    if (b == 0) return a;
    return gcd (b, a%b);
}

int main () {
    FILE *in = fopen ("A.in","r");
    FILE *out = fopen ("A.out","w");
    int t,k=1;
    fscanf (in,"%d",&t);
    while (t --) {
        long long P,Q;
        fprintf (out,"Case #%d: ",k++);
        fscanf (in,"%lld",&P);
        fscanf (in,"/");
        fscanf (in,"%lld",&Q);
        long long c = gcd(P, Q);
        P /= c;
        Q /= c;
        long long start = 1;
        while (start < Q) {
            start *= 2LL;
        }
        if (start != Q) fprintf (out,"impossible\n");
        else {
            int ret = 50;
            for (int i=1; i<=40; i++) {
                Q /= 2LL;
                if (P >= Q) {
                    ret = i;
                    break;
                }
            }
            if (ret == 50) fprintf (out,"impossible\n");
            else fprintf (out,"%d\n",ret);
        }
    }
}

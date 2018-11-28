#include <stdio.h>
#include <math.h>

int main() {
    int T,r,V,hasil;
    int L;
    scanf("%d",&T);
    for(int a=1;a<=T;a++) {
            scanf("%d%d",&r,&V);
            hasil=0;
            L=0;
            while(1) {
                     L+=(r+1)*(r+1)-r*r;
                     if(V<L) break;
                     r+=2;
                     hasil++;
            }
            printf("Case #%d: %d\n",a,hasil);
    }
    return 0;
}

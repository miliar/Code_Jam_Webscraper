#include <stdio.h>
#include <stdlib.h>
#define SIZE 1000
int compare(const void *a, const void *b)
{
      double c = *(double *)a;
      double d = *(double *)b;
      if(c < d){return 1;}
      else if (c == d) {return 0;}
      else return -1;
}
int main()
{
    int T,i,N,j,k,awin1,awin2;
    double a[SIZE], b[SIZE],copy[SIZE];
    scanf("%d",&T);
    for(i = 1; i <= T; i++) {
        scanf("%d",&N);
        for(j = 0; j < N; j++) {
            scanf("%lf",&a[j]);
        }
        for(j = 0; j < N; j++) {
            scanf("%lf",&b[j]);
        }
        qsort((void *)a, N, sizeof(a[0]), compare);
        qsort((void *)b, N, sizeof(a[0]), compare);
        for(j = 0; j < N; j++) {
            copy[j] = b[j];
        }
        awin1 = 0;
        for(j = 0; j < N; j++) {
            for(k = 0; k < N; k++) {
                if(a[j] > copy[k]) {
                    awin1++;
                    copy[k] = a[j];
                    break;
                }
            }
        }
        for(j = 0; j < N; j++) {
            copy[j] = a[j];
        }
        awin2 = N;
        for(j = 0; j < N; j++) {
            for(k = 0; k < N; k++) {
                if(b[j] > copy[k]) {
                    awin2--;
                    copy[k] = b[j];
                    break;
                }
            }
        }
        printf("Case #%d: %d %d\n",i,awin1,awin2);
    }
    return 0;
}

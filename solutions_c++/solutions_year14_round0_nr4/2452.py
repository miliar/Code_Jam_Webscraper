#include <stdio.h>
#include <stdlib.h>
int cmp(const void *p, const void *q){
    double a = *(double *) p, b = *(double *) q;
    if(a>b) return 1;
    else if(a<b) return -1;
    else return 0;
}
double a[1005], b[1005];
int main(void)
{
    int tn, t, n, i, j, k, l;
    int count, dcount;
    scanf("%d", &tn);
    for(t=1;t<=tn;t++){
        printf("Case #%d: ", t);
        scanf("%d", &n);
        for(i=0;i<n;i++)
            scanf("%lf", &a[i]);
        for(i=0;i<n;i++)
            scanf("%lf", &b[i]);
        qsort(a, n, sizeof(a[0]), cmp);
        qsort(b, n, sizeof(b[0]), cmp);
        for(i=n-1, j=n-1, k=0, l=0, dcount=0, count=0;i>=0;i--,k++){
            if(a[k]>b[l]){
                dcount++;
                l++;
            }
            if(a[i]>b[j])
                count++;
            else
                j--;
        }
        printf("%d %d\n", dcount, count);
    }

    return 0;
}

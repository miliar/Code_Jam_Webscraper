#include <stdio.h>
#define MAX 10

void bsort(long int *array, size_t size) {
    int progress = 0;
    size++;
    do {
        int i;
        progress = 0;
        for (i = 0; i < size - 2; ++i) {
            if (array[i] > array[i + 1]) {
                // Swap the elements
                long int temp = array[i];
                array[i] = array[i + 1];
                array[i + 1] = temp;

                progress = 1;
            }
        }
    } while (progress);
}

int main(){
    // printf("Hello\n");

    int t, n, l, i, j;
    long int a, b[MAX], c, at, p=0;
    scanf("%d",&t);
    for ( i = 0; i < t; ++i)
    {
        scanf("%ld %d\n", &a, &n);
        for ( j = 0; j < n; ++j)
        {
            scanf("%ld", &b[j]);
        }

        bsort(b,n);
        // printf("\n%ld %d\n", a, n);
        // for ( j = 0; j < n; ++j)   printf("%ld ", b[j]);

        l=0;
        p = 0;
        while(l<n){
            c=0;
            at = a;
            if(a == 1) { p += n-l; break;}
            while(at<=b[l]){
                at += at - 1;
                c++;
            }
            if(c<n-l){p += c; a=at+b[l]; l++;}
            else {p += n-l; break;}
        }

        printf("Case #%d: %ld\n", i+1, p);
    }

    return 1;
}
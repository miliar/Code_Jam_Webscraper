#include <iostream>
#include <cstdio>
#include <cstdlib>

void qsort (void* base, size_t num, size_t size,
            int (*compar)(const void*,const void*));

int compare(const void* a,const void* b) {
    return ( *(double*)a < *(double*)b ) ? 1 : -1;
}

void calculate() {
    int n, bw = 0, gw = 0;
    double g[2000], b[2000];
    scanf("%d", &n);
    for(int i=0;i<n;i++) {
        scanf("%lf", &g[i]);
    }
    for(int i=0;i<n;i++) {
        scanf("%lf", &b[i]);
    }

    qsort(g, n, sizeof(double), compare);
    qsort(b, n, sizeof(double), compare);

    int j;
    for(bw=0, j=0; bw<n && j<n; j++) {
        if(b[bw] > g[j]) {
            bw++;
        }
    }
    for(gw=0, j=0; gw<n && j<n; j++) {
        if(g[gw] > b[j]) {
            gw++;
        }
    }

    printf("%d %d\n", gw, n-bw);
}

int main() {
    int cases, i=0;
    scanf("%d",&cases);
    for(i =1; i<=cases; i++) {
        printf("Case #%d: ", i);
        calculate();
    }
}
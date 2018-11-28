
#include<iostream>
#include<cstdio>

using namespace std;

int split(double a[], int low ,int upp) {
    int p=low+1; //c.v for left
    int q=upp;   //c.v for right
    double pivot = a[low];

    while(p<=q) {
        while(a[p]<pivot)
            p++;
        while(a[q]>pivot)
            q--;
        if(p<q) {
            //swap a[p] and a[q]
            a[p] = a[p] + a[q] - ( a[q] = a[p] );
        }
    }

    //swap a[low] and a[q]
    a[q] = a[low] + a[q] - ( a[low] = a[q] );

    return q;
}

inline void qsort(double a[], int low, int upp) {
    if(low >= upp)
        return;

    int i;
    i = split(a, low, upp);
    qsort(a, low, i-1);
    qsort(a, i+1, upp);
}

inline bool check(double a[], int i1, int j1, double b[], int i2, int j2) {
    while(i1<=j1 && i2<=j2) {
        if(a[i1] < b[i2]) {
            return false;
        }
        i1++;
        i2++;
    }
    return true;
}

int main() {
    int t;
    scanf("%d", &t);
    double a[1000] = {};
    double b[1000] = {};
    for(int k=1; k<=t; k++) {
        int n,i,j,cut=-1,normal,deceitful;

        scanf("%d", &n);

        for(i=0; i<n; i++) {
            scanf("%lf", &a[i]);
        }
        for(i=0; i<n; i++) {
            scanf("%lf", &b[i]);
        }

        qsort(a,0,n-1);
        qsort(b,0,n-1);

        for(i=0; i<n; i++) {
            for(j=cut+1; j<n; j++) {
                if(b[j] > a[i]) {
                    cut = j;
                    break;
                }
            }
            if(j==(n-1)) {
                normal = n-i-1;
                break;
            }
            else if(j==n) {
                normal = n-i;
                break;
            }
        }

        for(i=0; i<n; i++) {
            if(check(a,i,n-1, b,0,n-1-i)==true) {
                break;
            }
        }
        deceitful = n-i<1?0:n-i;

        printf("Case #%d: %d %d\n", k, deceitful, normal);

    }
    return 0;
}

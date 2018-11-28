#include <iostream>
#include <stdio.h>
#include <algorithm>
using namespace std;

int main()
{
    int t, i ,n,k,l,j,s,z = 1;
    FILE *in, *out;
    double a[1001], b[1001];
     in = fopen("a3.in","r");
    out = fopen("o3.txt","w");
    fscanf(in,"%d", &t);
    while (t--) {
        fscanf(in,"%d", &n);

        for (i = 0; i < n; ++i) {
            fscanf(in,"%lf", &a[i]);

        }
        for (i = 0; i < n; ++i) {
            fscanf(in,"%lf", &b[i]);

        }
        sort(a,a+n);
        sort(b,b+n);

        for (i = 0, j = 0; i < n && j < n;) {
            if (a[i] > b[j]) {

                i++;
                j++;
            } else {
                i++;
            }
        }
        s = 0;
        for (k = 0; k < n; ++k) {
            for (l = 0; l < n; ++l) {
                if (a[k] < b[l]) {
                    s++;
                    b[l] = -1.0;
                    break;
                }
            }

        }

        fprintf(out,"Case #%d: %d %d\n",z++,j, n - s);

    }
    return 0;
}

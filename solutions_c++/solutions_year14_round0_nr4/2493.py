#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

int main()
{
    freopen("infile.txt", "r", stdin);
    freopen("outfile.txt", "w", stdout);
    int n;
    int t;
    int v;

    scanf("%d", &t);
    for (v = 0; v < t; v++) {
    scanf("%d", &n);
    float a[n];
    float b[n];

    for (int i = 0; i < n; i++) {
        scanf("%f", &a[i]);
    }
    for (int j = 0; j < n; j++) {
        scanf("%f", &b[j]);
    }
    sort(a, a+n);
    sort(b, b+n);
    /*for (int i = 0; i < n; i++) {
        printf("%f", a[i]);
    }
    for (int j = 0; j < n; j++) {
        printf("%f", b[j]);
    }*/

    int j = 0;
    int i = 0;
    while (j < n) {
        if (b[j] > a[i]) {
            i++;
        }
        j++;
    }
    int flag1 = n-i;
    i = 0;
    j = 0;
    int c = 0;
    int x = n;
    while (i < n) {
        while (j < x) {
            if (a[i] < b[j]) {
                x--;
                i++;
            } else {
                c++;
                i++;
                j++;
            }
        }
    }
    printf("Case #%d: %d %d\n", v+1, c, flag1);
    }

    return 0;
}

#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>


using namespace std;

double a[1000];
double b[1000];


int comp(const void *a, const void *b) {
    if (*((double *)a) > *((double *)b)) {
        return 1;
    } else {
        return -1;
    }
}

int main() {

    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int T;
    scanf("%d", &T);
    for (int ti = 1; ti <= T; ++ti) {
        printf("Case #%d: ", ti);

        int n;
        scanf("%d", &n);

        for (int i = 0; i < n; ++i) {
            scanf("%lf", &a[i]);
        }
        for (int i = 0; i < n; ++i) {
            scanf("%lf", &b[i]);
        }
        qsort(a, n, sizeof(a[0]), comp);
        qsort(b, n, sizeof(b[0]), comp);
        int win1 = 0, win2 = 0;
        int i = 0, j = 0;
        while (i < n && j < n) {
            if(a[i] > b[j]) {
                ++win1;
                ++i;
                ++j;
            } else {
                ++i;
            }
        }
        i = 0, j = 0;
        while (i < n && j < n) {
            //printf("%d %d %lf %lf\n", i, j, a[i], b[j]);
            if(a[i] < b[j]) {
                ++win2;
                ++i;
                ++j;
            } else {
                ++j;
            }
        }
        printf("%d %d\n", win1, n - win2);
    }

    return 0;

}

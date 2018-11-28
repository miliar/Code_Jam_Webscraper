#include <cstdio>
#include <algorithm>
#include <iostream>

using namespace std;

double A[1000], B[1000];

int main()
{
    freopen("D-large.in", "r", stdin);
    freopen("D-large.out", "w", stdout);

    int t, n, j, k, ans;
    scanf("%d", &t);
    for (int i = 1; i <= t; i++) {
        scanf("%d", &n);
        for (j = 0; j < n; j++) scanf("%lf", &A[j]);
        for (j = 0; j < n; j++) scanf("%lf", &B[j]);
        sort(A, A + n);
        sort(B, B + n);
        for (j = k = 0, ans = n; j < n && k < n; j++) if (A[j] < B[k]) ans--; else k++;
        printf("Case #%d: %d ", i, ans);
        for (j = k = 0, ans = n; j < n && k < n; k++) if (A[j] < B[k]) ans--, j++;
        printf("%d\n", ans);
    }
    return 0;
}

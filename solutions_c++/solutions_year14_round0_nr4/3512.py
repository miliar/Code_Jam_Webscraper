#include <cstdio>
#include <algorithm>

void jizz() {
    int n;
    scanf("%d", &n);

    double arr[2][1001];
    for (int i = 0; i < 2; ++i)
        for (int j = 0; j < n; ++j)
            scanf("%lf", &arr[i][j]);

    for (int i = 0; i < 2; ++i)
        std::sort(arr[i], arr[i] + n);

    int y = 0, z = 0;

    for (int i = 0, j = 0; i < n; ++i) {
        while (j < n && arr[0][i] > arr[1][j]) j += 1;
        if (j == n) z += 1;
        else j += 1;
    }

    for (int i = 0, lb = 0, ub = n; i < n; ++i) {
        if (arr[0][i] < arr[1][lb]) ub -= 1;
        else y += 1, lb += 1;
    }

    printf("%d %d\n", y, z);
}

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        printf("Case #%d: ", t);
        jizz();
    }
    return 0;
}

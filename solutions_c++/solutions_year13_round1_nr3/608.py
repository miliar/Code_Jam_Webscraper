#include <cstdio>
#include <algorithm>
using namespace std;

#define MAXN 16
#define MAXK 16

int opt[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};

int R, N, M, K;
int a[MAXK];

int s[MAXN];

int check() {
    int flag = 1;
    for (int i = 0; flag && i < K; i++) {
        if (a[i] == 1)
            continue;
        flag = 0;
        for (int mask = 1, lim = 1 << N; mask < lim; mask++) {
            int prod = 1;
            for (int k = 0; k < N; k++)
                if (mask & (1 << k))
                    prod *= s[k];
            if (prod == a[i]) {
                flag = 1;
                break;
            }
        }
    }
    return flag;
}

int solve(int idx, int last) {
    if (idx == N)
        return check();
    for (int i = last; i <= M; i++) {
        s[idx] = opt[i];
        if (solve(idx+1, i))
            return 1;
    }
    return 0;
}

int main() {
    scanf("%*d");
    scanf("%d %d %d %d", &R, &N, &M, &K);
    printf("Case #1:\n");
    while (R--) {
        for (int i = 0; i < K; i++)
            scanf("%d", &a[i]);
        if (solve(0, 2)) {
            for (int i = 0; i < N; i++)
                printf("%d", s[i]);
        }
        else {
            for (int i = 0; i < N; i++)
                printf("%d", 2);
        }
        puts("");
    }
}

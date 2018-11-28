#include <stdio.h>
#include <algorithm>

#define x first
#define y second

using namespace std;

typedef pair<int, int> pii;

const int MAXN = 1000 + 100;

double a[MAXN], b[MAXN];

pii solve(int N) {
    sort(a, a + N);
    sort(b, b + N);

    pii ret;
    ret.x = 0;
    ret.y = N;

    for (int m = 0,n = 0;m < N;m++)
        if (a[m] > b[n]) {
            n++;
            ret.x++;
        }

    for (int m = 0,n = 0;m < N;m++)
        if (b[m] > a[n]) {
            n++;
            ret.y--;
        }

    return ret;
}

int main() {
    int T, N;

    freopen("D-large.in", "r", stdin);
    freopen("D-large.out", "w", stdout);

    scanf("%d", &T);

    for (int t = 1;t <= T;t++) {
        scanf("%d", &N);

        for (int i = 0;i < N;i++)
            scanf("%lf", &a[i]);

        for (int i = 0;i < N;i++)
            scanf("%lf", &b[i]);

        pii ans = solve(N);

        printf("Case #%d: %d %d\n", t, ans.x, ans.y);
    }

    return 0;
}

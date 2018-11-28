#include <cstdio>
#include <algorithm>
using namespace std;

#define MAXN 1010

int main() {
    int T, N;
    double a[MAXN], b[MAXN];

    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%d", &N);
        for (int i = 0; i < N; i++)
            scanf("%lf", &a[i]);
        for (int i = 0; i < N; i++)
            scanf("%lf", &b[i]);
        sort(a, a+N);
        sort(b, b+N);

        int cnt1 = 0, cnt2 = 0;
        for (int i = 0, j = 0; i < N; i++) {
            if (a[i] > b[j]) {
                cnt1++;
                j++;
            }
        }
        for (int i = 0, j = 0; i < N; i++) {
            while (j < N && b[j] < a[i])
                j++;
            j == N ? cnt2++ : j++;
        }

        printf("Case #%d: %d %d\n", t, cnt1, cnt2);
    }
}

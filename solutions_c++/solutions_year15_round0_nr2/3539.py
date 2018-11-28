/*
AUTHOR: chico.de
PROBLEM: B
*/

#include <stdio.h>
#include <algorithm>

using namespace std;

void solve() {
    int N;
    int a[1024];

    scanf ("%d", &N);
    for (int i = 0; i < N; ++i) scanf ("%d", a+i);

    sort (a, a+N);

    int ans = a[N-1];
    for (int i = 1; i < a[N-1]; ++i) {
        int add = 0;
        for (int j = N-1; j >= 0; --j) {
            if (a[j] <= i) break;
            add += (a[j] / i) + (a[j] % i != 0) - 1;
        }

        if (ans > i + add)
            ans = i + add;
    }

    printf ("%d\n", ans);
}

int main (void) {
    int T;
    scanf ("%d", &T);
    for (int t = 1; t <= T; ++t) {
        printf ("Case #%d: ", t);
        solve();
    }
    return 0;
}

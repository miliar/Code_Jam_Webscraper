/*
AUTHOR: chico.de
PROBLEM: A
*/

#include <cstdio>
#include <cstring>

void solve() {
    int N;
    char s[1024];
    scanf ("%d%s", &N, s);
    
    if (N == 0) {
        printf ("0\n");
        return;
    }

    int sum = s[0] - '0';
    int ans = 0;
    for (int i = 1; i <= N; ++i) {
        if (sum < i && s[i-1] == '0') ++ ans, ++ sum;
        sum += s[i] - '0';
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

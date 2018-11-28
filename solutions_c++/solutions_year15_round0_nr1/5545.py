#include <cstdio>

const int SMAX = 1000;

int solve () {
    int ans = 0, sum = 0, smax, s[SMAX + 1];
    char aux;

    scanf ("%d ", &smax);
    for (int i = 0; i <= smax; ++i) {
        scanf ("%c", &aux);
        s[i] = aux - '0';
    }

    for (int i = 0; i <= smax; ++i) {
        if (s[i] > 0) {
            if (sum < i) {
                ans += (i - sum);
                sum = i;
            }
            sum += s[i];
        }
    }

    return ans;
}

int main () {
    //freopen ("data.in", "r", stdin);
    //freopen ("data.out", "w", stdout);
    int tests;

    scanf ("%d", &tests);
    for (int test = 1; test <= tests; ++test) {
        int ans = solve ();
        printf ("Case #%d: %d\n", test, ans);
    }

    return 0;
}

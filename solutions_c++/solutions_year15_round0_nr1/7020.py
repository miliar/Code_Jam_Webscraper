// https://code.google.com/codejam/contest/6224486/dashboard#s=p0
// Problem A. Standing Ovation

#include <cstdio>

using namespace std;

int n;
char in[1000 + 2];

void solve() {
    scanf("%d ", &n);
    fgets(in, 1000 + 2, stdin);

    int now(in[0] - '0'), need(0);
    for (int i = 1; i <= n; i++) {
        if (in[i] == '0') continue;
        if (now < i) {
            need += (i - now);
            now = i;
        }
        now += (in[i] - '0');
    }
    printf("%d\n", need);
}

int main() {
    int t;
    scanf("%d", &t);
    for (int i = 1; i <= t; i++) {
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}

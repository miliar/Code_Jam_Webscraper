#include <cstdio>
#include <cstring>
const int MAXN = 101;

char seq[MAXN];

int solve(int i, char cur) {
    if (i == 0) return seq[i] == cur ? 0 : 1;
    if (seq[i] == cur) return solve(i - 1, cur);
    else return solve(i - 1, cur == '+' ? '-' : '+') + 1;
}

int main () {
    int T = 0;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        scanf("%s", seq);
        printf("Case #%d: %d\n", cas, solve(strlen(seq) - 1, '+'));
    }
    return 0;
}

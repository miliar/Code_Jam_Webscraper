#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int N = 105;

int T, ans;
char str[N];

int solve() {
    int n = strlen(str + 1);
    str[0] == '+';
    int cnt = 0;
    for (int i = 1; i <= n; i++) {
        if (str[i] == '-' && str[i - 1] != '-') cnt++;
    }
    return cnt * 2 - (str[1] == '-');
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        scanf("%s", str + 1);
        int n = strlen(str + 1);
        printf("Case #%d: %d\n", cas, solve());
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}

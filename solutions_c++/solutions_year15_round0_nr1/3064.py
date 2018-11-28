#include <bits/stdc++.h>

using namespace std;

const int N = 1e5 + 5;
int a[N];
int n, m;
char str[N];


int work() {
    scanf("%d", &n);
    scanf("%s", str);
    int ret = 0;
    for (int i = 0, now = 0; i <= n; i++) {
        if (str[i] != '0') {
            if (now >= i) {
                now += str[i] - '0';
            }else {
                ret += i - now; now += i - now; now += str[i] - '0';
            }
        }
    }
    return ret;
}

void init() {
    freopen("A-large.in", "r", stdin);
    freopen("A_large.out", "w", stdout);
}

int main() {
    init();
    int T; cin >> T;
    for (int cas = 1; cas <= T; cas++) {
        printf("Case #%d: %d\n", cas, work());
    }
    return 0;
}

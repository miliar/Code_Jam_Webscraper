#include <bits/stdc++.h>

bool vis[10];
int S;

void digit(long long x) {
    if (x == 0) {
        vis[0] = true;
        S += 0;
    }
    while (x) {
        int y = x % 10;
        if (!vis[y]) {
            vis[y] = true;
            S += y;
        }
        x /= 10;
    }
}

int main() {
    //freopen ("A-large.in", "r", stdin);
    //freopen ("A-large.out", "w", stdout);
    int T; scanf ("%d", &T);
    int cas = 0;
    while (T--) {
        memset (vis, false, sizeof (vis));
        S = 0;
        long long n; std::cin >> n;
        std::cout << "Case #" << ++cas << ": ";
        if (n == 0) {
            puts ("INSOMNIA");
            continue;
        }
        digit (n);
        long long m = n;
        int times = 2;
        while (!(vis[0] && S == 45) && times <= 1000000) {
            m = n * times;
            digit (m);
            times++;
        }
        if (vis[0] && S == 45) {
            std::cout << m << '\n';
        } else {
            puts ("INSOMNIA");
        }
    }

    return 0;
}

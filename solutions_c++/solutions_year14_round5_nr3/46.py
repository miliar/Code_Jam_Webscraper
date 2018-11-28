#include <cstdio>
#include <unordered_map>

std :: unordered_map <int, int> mp;

int getId(int x) {
    if (x == 0)
        return -1;
    else if (mp.find(x) == mp.end()) 
        mp[x] = (int) mp.size() - 1;
    return mp[x];
}

bool dp[16][1 << 15];

int count(int x) {
    if (x == 0)
        return 0;
    else
        return 1 + count(x - (x & -x));
}

int main() {
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++ cas) {
        int n;
        scanf("%d", &n);
        mp.clear();
        int full = 1 << n;
        std :: fill(dp[0], dp[0] + full, true);
        for (int i = 0; i < n; ++ i) {
            std :: fill(dp[i + 1], dp[i + 1] + full, false);
            char c;
            int a;
            scanf(" %c%d", &c, &a);
            int id = getId(a);
            //printf("%d\n", id);
            if (c == 'E') {
                for (int s = 0; s < full; ++ s) 
                    for (int j = 0; j < n; ++ j)
                        if (id == -1 || id == j)
                            if ((s >> j) % 2 == 0 && dp[i][s])
                                dp[i + 1][s | 1 << j] = true;
            } else {
                for (int s = 0; s < full; ++ s) 
                    for (int j = 0; j < n; ++ j)
                        if (id == -1 || id == j)
                            if ((s >> j) % 2 == 1 && dp[i][s])
                                dp[i + 1][s ^ 1 << j] = true;
            }
        }
        int ans = n + 1;
        for (int i = 0; i < full; ++ i)
            if (dp[n][i])
                ans = std :: min(ans, count(i));
        printf("Case #%d: ", cas);
        if (ans <= n)
            printf("%d\n", ans);
        else
            puts("CRIME TIME");
    }
    return 0;
}

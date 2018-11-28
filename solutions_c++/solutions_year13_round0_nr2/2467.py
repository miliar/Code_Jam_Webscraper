#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>

using namespace std;

const int N = 105;

int mp[N][N];
int tm[2][N];
int n, m;

bool judge() {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (mp[i][j] < tm[0][i] && mp[i][j] < tm[1][j])
                return false;
        }
    }
    return true;
}

int main() {
    freopen("d://in.txt", "r", stdin);
    freopen("d://out.txt", "w", stdout);

    int t;
    scanf("%d", &t);
    for (int ti = 1; ti <= t; ti++) {
        scanf("%d %d", &n, &m);
        memset(mp, 0, sizeof(mp));
        memset(tm, 0, sizeof(tm));

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                scanf("%d", &mp[i][j]);
                if (mp[i][j] > tm[0][i]) tm[0][i] = mp[i][j];
                if (mp[i][j] > tm[1][j]) tm[1][j] = mp[i][j];
            }
        }
        printf("Case #%d: %s\n", ti, judge() ? "YES" : "NO");
    }

    return 0;
}

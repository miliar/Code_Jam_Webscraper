#include <bits/stdc++.h>
using namespace std;
const int N = 30;

int n;
char g[N][N];
int p[N];

bool dfs(int k , int cur , int mask) {
    if (k == n) {
        if (cur != (1 << n) - 1) {
            return 0;
        }
        return 1;
    } else {
        int cnt = 0;
        int x = p[k];
        for (int i = 0 ; i < n ; ++ i) {
            if ((~cur >> i & 1) && (mask >> (x * n + i) & 1)) {
                ++ cnt;
                if (!dfs(k + 1 , cur | 1 << i , mask))
                    return 0;
            }
        }
        if (!cnt)
            return 0;
        return 1;
    }
}

bool check(int mask) {
    for (int i = 0 ; i < n ; ++ i) {
        p[i] = i;
    }
    do {
        if (!dfs(0 , 0 , mask)) {
            return 0;
        }
    } while (next_permutation(p , p + n));
    return 1;
}

void work() {
    scanf("%d" , &n);
    int mask = 0;
    int num = 0;
    for (int i = 0 ; i < n ; ++ i) {
        scanf("%s" , g[i]);
        for (int j = 0 ; j < n ; ++ j) {
            if (g[i][j] == '1') {
                mask |= 1 << num;
            }
            num ++;
        }
    }
    int res = 1 << 30;
    for (int i = 0 ; i < 1 << num ; ++ i) {
        if ((i & mask) != mask) {
            continue;
        }
        if (check(i)) {
            res = min(res , (int)__builtin_popcount(i));
        }
    }
    cout << res - __builtin_popcount(mask) << endl;
}

int main() {
    int ca = 0 , T;
    scanf("%d" , &T);
    while (T --) {
        printf("Case #%d: " , ++ ca);
        work();
    }
    return 0;
}

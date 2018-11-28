#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int T, N, J;

int pow_mod(int x, int k, int mod) {
    int ans = 1;
    while (k) {
        if (k&1) ans = 1LL * ans * x % mod;
        x = 1LL * x * x % mod;
        k >>= 1;
    }
    return ans;
}

const int ans[12] = {0, 0, 3, 2, 5, 2, 7, 2, 3, 2, 7};

int sb[100];

bool judge(long long x) {
    for (int i = N - 1; i >= 0; i--) sb[i] = (x>>i)&1;
    for (int i = 2; i <= 10; i++) {
        int tmp = 0;
        for (int j = N - 1; j >= 0; j--) {
            if (sb[j] == 0) continue;
            tmp = (tmp + pow_mod(i, j, ans[i])) % ans[i];
        }
        if (tmp != 0) return false;
    }
    return true;
}

void print(long long x) {
    for (int i = N - 1; i >= 0; i--) printf("%d", sb[i]);
    for (int i = 2; i <= 10; i++) printf(" %d", ans[i]);
    printf("\n");
}

int main() {
    //printf("%d\n", 111001 % 11);
    /*for (int i = 2; i <= 10; i++) {
        for (int j = 2; ; j++) {
            if ((pow_mod(i, 15, j) + 1) % j == 0) {
                printf("%d %d\n", i, j);
                break;
            }
        }
    }*/

    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        scanf("%d%d", &N, &J);
        printf("Case #%d:\n", cas);
        long long s = (1LL<<(N - 1)) + 1;
        for (int i = 0; i < J; i++) {
            while (!judge(s)) s += 2;
            print(s);
            s += 2;
        }
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}

#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <string>
#include <algorithm>
using namespace std;

typedef long long lld;

#define get(i, x) (((x) >> ((i) - 1)) & 1)

lld a, b, k;
lld cache[32][2][2][2];

lld solve(lld i, bool free_a, bool free_b, bool free_k) {
    if (i == 0) {
        return 1;
    }
    lld &cached = cache[i][free_a][free_b][free_k];
    if (cached == -1) {
        bool ai = get(i, a);
        bool bi = get(i, b);
        bool ki = get(i, k);
        cached = 0;
        cached += solve(i - 1, free_a || ai, free_b || bi, free_k || ki); // 0 0
        if (free_a || ai) cached += solve(i - 1, free_a, free_b || bi, free_k || ki); // 1 0
        if (free_b || bi) cached += solve(i - 1, free_a || ai, free_b, free_k || ki); // 0 1
        if ((free_a || ai) && (free_b || bi) && (free_k || ki)) {
            cached += solve(i - 1, free_a, free_b, free_k); // 1 1
        }
    }
    return cached;
}

int main() {
    cout.setf(ios_base::fixed);
    cout.precision(7);
    int T;
    cin >> T;
    for (int ti = 1; ti <= T; ++ti) {
        cout << "Case #" << ti << ": ";
        cin >> a >> b >> k;
        a -= 1;
        b -= 1;
        k -= 1;
        for (int i = 0; i <= 31; ++i) {
            for (int j = 0; j <= 1; ++j) {
                for (int k = 0; k <= 1; ++k) {
                    for (int l = 0; l <= 1; ++l) {
                        cache[i][j][k][l] = -1;
                    }
                }
            }
        }
        cout << solve(31, 0, 0, 0);
        cout << "\n";
    }
    return 0;
}

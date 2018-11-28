/*
 * Created by KeigoOgawa on 4/9/16.
 */


#include <cstdio>
#include <iostream>

using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> PII;

const int MAX_N = (const int) 1e6;

int T, N;
bool used[10];

bool check() {
    for (int i = 0; i < 10; ++i) {
        if (!used[i]) {
            return true;
        }
    }
    return false;
}

int solve() {
    fill(used, used + 10, false);
    int ans = 0;
    while(check()) {
        ans += N;
        int now = ans;
        while (now != 0) {
            used[now % 10] = true;
            now /= 10;
        }
    }
    return ans;
}

int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(false);
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        cin >> N;
        if (N == 0) {
            printf("Case #%d: INSOMNIA\n", i);
        } else {
            printf("Case #%d: %d\n", i, solve());
        }
    }
    solve();
    return 0;
}

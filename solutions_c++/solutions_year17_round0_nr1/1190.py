#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <cmath>
#define LL long long
using namespace std;
#define rep(i, n) for (int i = 0; i < n; i++)
#define kep(i, n) for (int i = 1; i <=n; i++)
#define N 1111

int T, n, cnt[N];
string s;

int calc() {
    memset(cnt, 0, sizeof(cnt));
    int state = 0, cur = 0, ans = 0;
    rep(i, (int)s.size()) {
        state = (s[i] == '+' ? 0 : 1);
        state ^= cur ^= cnt[i];
        if (!state) continue;
        if (s.size() - i <n) return -1;
        ++ans;
        cnt[i + n] = 1;
        cur ^= 1;
    }
    return ans;
}

void solve() {
    cin >> s >> n;
    int ans = calc();
    if (ans == -1) puts("IMPOSSIBLE");
    else printf("%d\n", ans);
}

int main() {
	freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    ios::sync_with_stdio(false);
    cin >> T;
    kep(_, T) {
        printf("Case #%d: ", _);
        solve();
    }
	return 0;
}

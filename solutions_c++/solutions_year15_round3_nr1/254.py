#include <cstdio>
#include <iostream>

using namespace std;

int T, r, c, w;

int dfs(int c, int w) {
    if (w == 1) return c;
    if (c >= 2 * w)
        return 1 + dfs(c - w, w);
    return 1 + dfs(c - 1, w - 1);
}

int main() {
    cin >> T;
    for (int cs = 1; cs <= T; ++cs) {
        cin >> r >> c >> w;
        int ans = 0;
        ans += (r - 1) * (c / w);
        ans += dfs(c, w);
        cout << "Case #" << cs << ": " << ans << endl;
    }
    return 0;
}

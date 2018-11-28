#include <iostream>
#include <algorithm>

const int MAXN = 1000;

double a[MAXN], b[MAXN];
bool chs[MAXN];

int main() {
    int T;
    std :: cin >> T;
    for (int cas = 1; cas <= T; ++ cas) {
        int n;
        std :: cin >> n;
        for (int i = 0; i < n; ++ i)
            std :: cin >> a[i];
        for (int i = 0; i < n; ++ i)
            std :: cin >> b[i];
        std :: sort(a, a + n);
        std :: sort(b, b + n);
        int ans1 = 0, ans2 = 0;
        std :: fill(chs, chs + n, false);
        for (int i = 0; i < n; ++ i) {
            int idx = -1;
            for (int j = 0; j < n; ++ j)
                if (!chs[j] && a[i] < b[j]) {
                    idx = j;
                    break;
                }
            if (-1 != idx)
                chs[idx] = true;
            else {
                ++ ans2;
                chs[std :: find_if(chs, chs + n, [] (bool x) {return !x;}) - chs] = true;
            }
        }
        std :: reverse(b, b + n);
        for (int i = 0; i < n; ++ i) {
            int tot = 0;
            std :: reverse(b + i, b + n);
            for (int j = i; j < n; ++ j)
                tot += a[j] > b[j];
            ans1 = std :: max(ans1, tot);
            std :: reverse(b + i, b + n);
        }
        std :: cout << "Case #" << cas << ": " << ans1 << " " << ans2 << std :: endl;
    }
    return 0;
}

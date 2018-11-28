#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

const int maxn = 1111;
int p[maxn];

int main() {

    freopen("b.in","r", stdin);
    freopen("b.out", "w", stdout);

    int T, ca = 0;
    cin >> T;
    while (T--) {
        int D;
        cin >> D;
        int max_p = 0;
        for (int i = 0; i < D; ++i) {
            cin >> p[i];
            max_p = max(max_p, p[i]);
        }
        int ans = max_p == 0 ? 0 : maxn;
        for (int eat = 1; eat <= max_p; ++eat) {
            int special_time = 0;
            for (int i = 0; i < D; ++i) {
                int add = (p[i] - 1) / eat;
                special_time += add;
            }
            ans = min(ans, eat + special_time);
        }
        printf("Case #%d: %d\n", ++ca, ans);
    }
    return 0;
}

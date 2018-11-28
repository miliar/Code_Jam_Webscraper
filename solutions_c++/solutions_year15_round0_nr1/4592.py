#include <bits/stdc++.h>

using namespace std;
const int MaxN = 1e3 + 7;
// const int MOD = ;
int arr[MaxN], cum[MaxN];

int main() {
        // ios_base::sync_with_stdio(0);
        freopen("A-large.in", "rt", stdin);
        freopen("A-large.out", "wt", stdout);
        int t;
        scanf("%d", &t);
        for (int i = 0; i < t; ++i) {
                memset(arr, 0, sizeof(0));
                memset(cum, 0, sizeof(0));
                printf("Case #%d: ", i + 1);
                int s_max;
                scanf("%d", &s_max);
                s_max++;
                string s;
                cin >> s;
                for (unsigned i = 0; i < s.size(); ++i) {
                        arr[i] = s[i] - '0';
                }
                cum[0] = arr[0];
                for (int i = 1; i < s_max; ++i)
                        cum[i] = cum[i - 1] + arr[i];
                int mx = 0;
                for (int i = 1; i < s_max; ++i) {
                        if (cum[i - 1] < i) {
                                mx = max(abs(cum[i - 1] - i), mx);
                        }
                }
                printf("%d\n", mx);
        }
        return 0;
}

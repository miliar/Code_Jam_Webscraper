#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;

int n;
char s[105][105];
vector<char> a[105];
int b[105][105];

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        scanf("%d", &n);
        int flag = 1;
        for (int i = 0; flag && i < n; ++i) {
            scanf("%s", s[i]);
            a[i].clear();
            for (int j = 0; s[i][j]; ++j)
                a[i].push_back(s[i][j]);
            a[i].erase(unique(a[i].begin(), a[i].end()), a[i].end());
            if (i > 0) {
                if (a[i].size() != a[0].size()) {
                    flag = 0;
                    break;
                }
                for (int j = 0; j < a[0].size(); ++j) {
                    if (a[i][j] != a[0][j]) {
                        flag = 0;
                        break;
                    }
                }
            }
        }
        if (!flag) {
            printf("Case #%d: Fegla Won\n", t);
            continue;
        }
        memset(b, 0, sizeof(b));
        for (int i = 0; i < n; ++i) {
            int idx = 0;
            for (int j = 0, k = 1; j < s[i][j]; j = k++, ++idx) {
                while (s[i][k] && s[i][k] == s[i][j]) ++k;
                b[i][idx] += k - j;
            }
        }
        int ans = 0;
        for (int i = 0; i < a[0].size(); ++i) {
            int sum = 0;
            for (int j = 0; j < n; ++j)
                sum += b[j][i];
            int qnt = (2*sum + n) / (2*n);
            for (int j = 0; j < n; ++j)
                ans += abs(b[j][i] - qnt);
        }
        printf("Case #%d: %d\n", t, ans);
    }
}

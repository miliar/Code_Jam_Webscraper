#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;

#define MAX 60

int n, g[2*MAX][MAX];
int c[2510];

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%d", &n);
        memset(c, 0, sizeof(c));
        for (int i = 1; i < 2*n; i++) {
            for (int j = 0; j < n; j++) {
                scanf("%d", &g[i][j]);
                c[g[i][j]]++;
            }
        }
        vector<int> ans;
        for (int i = 0; i < 2510; i++)
            if (c[i] % 2 == 1)
                ans.push_back(i);
        sort(ans.begin(), ans.end());
        printf("Case #%d:", t);
        for (int i = 0; i < n; i++)
            printf(" %d", ans[i]);
        puts("");
    }
}

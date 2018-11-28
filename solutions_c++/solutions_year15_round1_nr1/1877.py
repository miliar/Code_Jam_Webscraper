#include <cstdio>
#include <algorithm>

#include <vector>
#include <queue>

using namespace std;

int main() {
    int T;
    scanf("%d", &T);
    for (int ti = 1; ti <= T; ti++) {
        int res1 = 0, res2 = 0;
        int n;
        scanf("%d", &n);
        vector<int> m(n, 0);
        for (int i = 0; i < n; i++) scanf("%d", &m[i]);
        
        for (int i = 1; i < n; i++) res1 += max(0, m[i - 1] - m[i]);
        
        int max_gap = 0;
        for (int i = 1; i < n; i++) max_gap = max(max_gap, m[i - 1] - m[i]);
        for (int i = 1; i < n; i++) res2 += min(max_gap, m[i - 1]);
        
        printf("Case #%d: %d %d\n", ti, res1, res2);
    }
}

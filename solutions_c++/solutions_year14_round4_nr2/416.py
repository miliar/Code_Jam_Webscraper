#include <iostream>
#include <algorithm>
using namespace std;
const int MAXN = 1005;

struct node {
    int val, pos;
} p[MAXN];
int a[MAXN];

bool cmp(const node& a, const node& b) {
    return a.val < b.val;
}

int main() {
    int cases;
    scanf("%d", &cases);
    for (int T = 1; T <= cases; T++) {
        int n, ans = 0;
        scanf("%d", &n);
        for(int i = 0; i < n; i++) {
            scanf("%d", &p[i].val);
            p[i].pos = i;
            a[i] = 0;
        }
        sort(p, p + n, cmp);
        for (int i = 0; i < n; i++) {
            int move = a[p[i].pos];
            p[i].pos -= move;
            int tmp = (n - 1 - i) - p[i].pos;
            ans += min(p[i].pos, tmp);
            for (int j = p[i].pos + move + 1; j <= n - 1; j++) {
                a[j]++;
            }
        }
        printf("Case #%d: %d\n", T, ans);
    }
    return 0;
}

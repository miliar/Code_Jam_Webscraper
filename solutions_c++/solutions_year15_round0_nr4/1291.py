#include <cstdio>
#include <algorithm>
using namespace std;
int main() {
    int n;
    scanf("%d", &n);
    for (int k = 1; k <= n; ++k) {
        int x, r, c, ans;
        scanf("%d%d%d", &x, &r, &c);
        if (x < 7)
            ans = (r * c % x == 0) && (min(r, c) >= x - 1);
        else
            ans = 0;
        printf("Case #%d: %s\n", k, ans ? "GABRIEL": "RICHARD");
    }
}

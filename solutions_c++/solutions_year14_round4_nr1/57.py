#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <map>
#include <vector>
#include <string>
#include <set>
#include <algorithm>

using namespace std;

const int N = 10010;
int a[N];

void run(int cas) {
    int n, x;
    scanf("%d%d", &n, &x);
    for (int i = 0; i < n; i++)
        scanf("%d", &a[i]);
    int ll = 0, rr = n - 1;
    int ans = 0;
    sort(a, a + n);
    while (ll <= rr) {
        if (ll < rr) {
            if (a[ll] + a[rr] <= x) {
                ll++;
                rr--;
                ans++;
            } else {
                rr--;
                ans++;
            }
        } else {
            ans++;
            break;
        }
    }
    printf("Case #%d: %d\n", cas, ans);
}

int main() {
    int tt, cas;
    scanf("%d", &tt);
    for (cas = 1; cas <= tt; cas++)
        run(cas);
    return 0;
}


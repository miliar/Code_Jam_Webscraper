#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <vector>
#include <string>
#include <algorithm>
#include <functional>
using namespace std;
typedef long long LL;
const double EPS = 1e-8;
const int INF = 0x3f3f3f3f;

bool ok(int x) {
    char sudo[15];
    itoa(x, sudo, 10);
    string a(sudo);
    string b(sudo);
    reverse(a.begin(), a.end());
    if (a == b) return true;
    return false;
}

int main() {
    int T, cas = 1;
    scanf("%d", &T);
    while (T--) {
        int l, r;
        scanf("%d%d", &l, &r);
        int cnt = 0;
        for (int i = l; i <= r; i++) {
            int num = i;
            int fac = (int)sqrt((double)num);
            if (fac * fac == num) {
                if (ok(fac) && ok(num)) cnt++;
            }
        }
        printf("Case #%d: %d\n", cas++, cnt);
    }
    return 0;
}
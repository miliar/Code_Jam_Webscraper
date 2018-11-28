#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <utility>
#include <algorithm>
#include <cstring>
#include <string>

#define X first
#define Y second

using namespace std;

typedef pair<int, pair<int, bool> > pp;

int T, n, m;
pair<int, pair<int, bool> > a[2013], stack[2013];
int top, cnt;
long long ans, sum;

bool cmp(const pp &a, const pp & b) {
    if ((a.X != b.X) || (a.Y.Y == b.Y.Y)) return a.X < b.X;
    return a.Y.Y > b.Y.Y;
}

int main() {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("a.out", "w", stdout);
    cin >> T;
    for (int cs = 1; cs <= T; ++cs) {
        cin >> n >> m;
        ans = sum = 0;
        top = cnt = 0;
        for (int i = 1, x, y, q; i <= m; ++i) {
            cin >> x >> y >> q;
            sum += (n + n + 1 - y + x) * (y - x) / 2 * q;
            a[cnt++] = make_pair(x, make_pair(q, true));
            a[cnt++] = make_pair(y, make_pair(q, false));
        }
        sort(a, a + cnt, cmp);
        for (int i = 0; i < cnt; ++i)
            cerr << a[i].X << " " << a[i].Y.X << " " << a[i].Y.Y << endl;
        int tmp;
        for (int i = 0; i < cnt; ++i) {
            if (a[i].Y.Y)
                stack[top++] = a[i];
            else {
                l1:
                tmp = min(a[i].Y.X, stack[top - 1].Y.X);
                ans += (n + n + 1 - a[i].X + stack[top - 1].X) * (a[i].X - stack[top - 1].X) / 2 * tmp;
                cerr << a[i].X << " " <<  stack[top - 1].Y.X  << " " << tmp << endl;
                a[i].Y.X -= tmp;
                if (((stack[top - 1].Y.X -= tmp) == 0) && tmp) {
                    --top;
                    goto l1;
                }
            }
        }
        printf("Case #%d: ", cs);
        cout << sum - ans << endl;
    }
    return 0;
}

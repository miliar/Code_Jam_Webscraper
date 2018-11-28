#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

const int maxn = 1005;
int T;
int n, p, maxp, c[maxn];
int ans, cost;

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    cin >> T;
    for (int cas=1;cas<=T;cas++) {
        cin >> n;
        memset(c, 0, sizeof(c));
        maxp = 0;
        for (int i=0;i<n;i++) {
            cin >> p;
            maxp = max(p, maxp);
            c[p]++;
        }
        ans = 0x7fffffff;
        for (p=maxp;p>=1;p--) {
            cost = p;
            for (int i=p+1;i<=maxp;i++) {
                if (c[i] > 0) cost += c[i] * int((i-1) / p);
            }
            ans = min(ans, cost);
        }
        cout << "Case #" << cas << ": " << ans << endl;
    }
	return 0;
}

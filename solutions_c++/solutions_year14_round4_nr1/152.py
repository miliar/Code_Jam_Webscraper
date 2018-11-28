#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <iostream>
#include <cassert>
using namespace std;


#define INF 1e+9
#define mp make_pair
#define lint long long
#define pii pair<int, int>
#define MAXN 100000

//bool used[MAXN];
int a[MAXN];

int main() {
    ios_base::sync_with_stdio(false);
    int t; cin >> t;
    for (int i = 0; i < t; i++) {
        int n, x; cin >> n >> x;
        for (int i = 0; i < n; i++)
            cin >> a[i];
        sort(a, a + n);
        //fill(used, used + n, false);
        int l = 0;
        int ans = 0;
        for (int r = n - 1; r >= l; r--) {
            //if (used[r]) continue;
            if (a[l] + a[r] <= x) {
            //    used[l] = used[r] = true;
                l++;
            }
            ans++;
        }
        cout << "Case #" << i + 1 << ": " << ans << endl;
    }
}

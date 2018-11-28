#include <iostream>
using namespace std;

const int N = 11111;
int a[N], n, m;

int main() {
    freopen("a-large.in", "r", stdin);
    freopen("a-large.out", "w", stdout);
    int T, Case = 1;
    cin >> T;
    while (T--) {
        cin >> n >> m;
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }
        sort(a, a + n);
        reverse(a, a + n);
        int ans = 0;
        for (int i = 0; i < n; i++) {
            if (i + 1 < n && a[i] + a[n - 1] <= m) {
                n--;
            }
            ans++;
        }
        cout << "Case #" << Case++ << ": " << ans << endl;
    }
    return 0;
}

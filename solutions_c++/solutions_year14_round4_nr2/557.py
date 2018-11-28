#include <iostream>
using namespace std;

const int N = 1111;
int a[N], n;

int main() {
    freopen("b-large.in", "r", stdin);
    freopen("b-large.out", "w", stdout);
    int T, Case = 1;
    cin >> T;
    while (T--) {
        cin >> n;
        for (int i = 1; i <= n; i++) {
            cin >> a[i];
        }
        int ans = 0;
        for (int i = 1; i <= n; i++) {
            int f = 0, g = 0;
            for (int j = 0; j < i; j++) {
                if (a[j] > a[i]) f++;
            }
            for (int j = i + 1; j <= n; j++) {
                if (a[j] > a[i]) g++;
            }
            ans += min(f, g);
        }
        cout << "Case #" << Case++ << ": " << ans << endl;
    }
    return 0;
}

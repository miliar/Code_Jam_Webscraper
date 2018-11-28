#include <iostream>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int T; cin >> T;
    int x = 1;
    while (T --> 0) {
        int n; string s;
        cin >> n >> s;

        int c = (int)(s[0] - '0');
        int ret = 0;
        for (int i = 1; i <= n; i++) {
            int k = (int)(s[i] - '0');
            if (k > 0 && i > c) {
                ret += (i - c);
                c = i;
            }
            c += k;
        }

        cout << "Case #" << x << ": " << ret << endl;
        x++;
    }
    return 0;
}

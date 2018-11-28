#include <iostream>

using namespace std;

int main() {

    int t, m, f, l;
    char s[1005];

    cin >> t;
    for (int z = 1; z <= t; ++z) {
        cin >> m >> s;
        f = l = 0;
        for (int i = 0; i <= m; ++i) {
            if (s[i] != '0') {
                if (l < i) {
                    f += i - l;
                    l = i;
                }
                l += s[i] - '0';
            }
        }
        cout << "Case #" << z << ": " << f << "\n";
    }

    return 0;
}

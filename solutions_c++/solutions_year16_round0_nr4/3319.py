#include <iostream>
#include <cmath>

using namespace std;

int main() {
    int t, k, c, s;
    cin >> t;
    for(int a = 1; a <= t; a++) {
        cin >> k >> c >> s;
        cout << "Case #" << a << ":";
        if (c == 1) if (k > s)
            cout << " IMPOSSIBLE";
        else
            for (int i = 1; i <= s; i++)
                cout << " " << i;
        else {
            long long len = pow(k, c);
            if (k > 2 * s)
                cout << " IMPOSSIBLE";
            else {
                int rep = 0;
                for (long long i = 1; (i <= len) && (rep < s); i += 2*k + 1) {
                    if (i + 1 <= len) i += 1;
                    cout << " " << i;
                    rep++;
                }
            }
        }

        cout << endl;
    }
    return 0;
}
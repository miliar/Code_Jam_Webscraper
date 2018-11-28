#include <iostream>

using namespace std;

int main() {

    int t;
    cin >> t;
    for (int x = 1; x <= t; ++x) {

        int smax;
        string s;
        cin >> smax >> s;

        int standing = 0;
        int ans = 0;
        for (int i = 0; i < s.size(); ++i) {

            if (i > standing) {
                ans += i - standing;
                standing = i;
            }
            standing += s[i] - '0';
        }

        cout << "Case #" << x << ": " << ans << endl;

    }

    return 0;
}

#include <iostream>
#include <string>

using namespace std;



int main() {
    freopen("/home/artur/Загрузки/B-large.in", "r", stdin);
    freopen("/home/artur/Загрузки/output.txt", "w", stdout);
    int TESTS;
    string s;
    cin >> TESTS;
    for (int test = 1; test <= TESTS; test++) {
        cout << "Case #" << test << ": ";
        cin >> s;
        s += '+';
        int ans = 0;
        for (int i = s.length() - 1; i > 0; i--) {
            if (s[i] != s[i - 1]) {
                ans++;
            }
        }
        cout << ans << endl;
    }
    return 0;
}
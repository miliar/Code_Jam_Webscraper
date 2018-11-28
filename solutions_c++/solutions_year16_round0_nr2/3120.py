#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>

using namespace std;

int main() {
    int tests;
    cin >> tests;

    for (int test = 1; test <= tests; ++test) {
        cout << "Case #" << test << ": ";

        string s;
        cin >> s;
        s.push_back('+');

        int ans = 0;
        for (size_t i = 0; i + 1 < s.size(); ++i) {
            if (s[i] != s[i + 1])
                ans++;
        }

        cout << ans << endl;
    }
    return 0;
}

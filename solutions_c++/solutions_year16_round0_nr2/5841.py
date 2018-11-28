#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    freopen("input", "r", stdin);
    freopen("output", "w", stdout);

    long long a;
    cin >> a;

    string s;
    long long ans;
    for (int i = 0; i < a; ++i) {
        ans = 0;
        cin >> s;
        if (s[s.length() - 1] == '-') {
            ++ ans;
        }
        for (int j = s.length() - 2; j >= 0; --j) {
            if (s[j] != s[j+1]) {
                ++ans;
            }
        }
        cout << "Case #" + to_string(i + 1) + ": " + to_string(ans) << endl;
    }


    return 0;
}
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

string solve(string s) {
    string result(1, s[0]);

    for (int i = 1; i < s.size(); ++i) {
        if (result[0] <= s[i])
            result = s[i] + result;
        else
            result = result + s[i];
    }

    return result;
}

int main() {
    int T;
    cin >> T;

    for (int i = 1; i <= T; ++i) {
        string s;
        cin >> s;

        auto result = solve(s);

        printf("Case #%d: %s\n", i, result.data());
    }

    return 0;
}

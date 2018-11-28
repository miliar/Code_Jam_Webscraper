#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

int main() {
    int T;
    cin >> T;

    for (int t = 1; t <= T; t++) {
        string s;
        cin >> s;

        s += "+";
        int ret = 0;
        char prev = s[0];
        for (int i = 1; i < s.size(); i++) {
            ret += prev != s[i] ? 1 : 0;
            prev = s[i];
        }

        printf("Case #%d: %d\n", t, ret);
    }

    return 0;
}

#include <iostream>
#include <algorithm>
#include <bitset>
#include <set>
#include <map>
#include <vector>
#include <string>

using namespace std;

int main() {
    std::ios_base::sync_with_stdio(false);
    int tests_count;
    cin >> tests_count;
    for (int test_index = 0; test_index < tests_count; ++test_index) {
        string s;
        cin >> s;
        char start = s[0];
        int len = 1;
        for (int i = 1; i < s.size(); ++i) {
            len += s[i] != s[i - 1];
        }
        int res = 0;
        if (start == '+') {
            res = len / 2 * 2;
        } else {
            res = 1 + (len - 1) / 2 * 2;
        }
        cout << "Case #" << test_index + 1 << ": " << res << "\n";
    }
    return 0;
}

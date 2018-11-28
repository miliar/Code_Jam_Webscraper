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
        int k, c, s;
        cin >> k >> c >> s;
        cout << "Case #" << test_index + 1 << ":";
        for (int i = 1; i <= s; ++i) {
            cout << ' ' << i;
        }
        cout << "\n";
    }
    return 0;
}

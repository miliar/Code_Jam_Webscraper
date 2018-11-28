#include <iostream>
#include <algorithm>
#include <bitset>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <iomanip>
#include <queue>
#include <utility>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<int, char> pci;

void Solve(int test_index) {
    string s;
    int k;
    cin >> s >> k;
    int res = 0;
    for (int i = 0; i + k - 1 < s.size(); ++i) {
        if (s[i] == '+') { continue; }
        ++res;
        for (int j = 0; j < k; ++j) {
            s[i + j] = s[i + j] == '+' ? '-' : '+';
        }
    }
    for (char ch : s) {
        if (ch == '-') {
            cout << "Case #" << test_index << ": IMPOSSIBLE\n";
            return;
        }
    }
    cout << "Case #" << test_index << ": " << res << "\n";
}

int main() {
    std::ios_base::sync_with_stdio(false);
    int tests_count;
    cin >> tests_count;
    for (int test_index = 0; test_index < tests_count; ++test_index) {
        Solve(test_index + 1);
    }
    return 0;
}

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int solve() {
    int n, x;
    cin >> n >> x;
    vector<int> s(n);
    for (int i = 0; i != n; ++i)
        cin >> s[i];
    sort(s.begin(), s.end());
    int ans = 0;
    int j = n - 1;
    int pairs = 0;
    for (int i = 0; i < j; ++i) {
        while (i < j && s[i] + s[j] > x)
            --j;
        if (i < j) {
            ++pairs;
            --j;
        }
    }
    return n - pairs;
}

int main() {
    int tests;
    cin >> tests;
    for (int t = 1; t <= tests; ++t) {
        cout << "Case #" << t << ": " << solve() << '\n';
    }

    return 0;
}


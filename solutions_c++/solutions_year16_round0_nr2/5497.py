#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <algorithm>
#include <deque>
#include <cmath>
#include <ctime>

using namespace std;

int main() {
    freopen("B-large (1).in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tests;
    cin >> tests;
    for (int test = 0; test < tests; test++) {
        cout << "Case #" << test + 1 << ": ";
        string s;
        cin >> s;
        int k = 0;
        for (int i = 1; i < s.length(); ++i) {
            if (s[i] != s[i - 1]) {
                k++;
            }
        }
        k++;
        if (s[s.length() - 1] == '+') {
            cout << k - 1;
        } else {
            cout << k;
        }
        cout << "\n";
    }
    return 0;
}
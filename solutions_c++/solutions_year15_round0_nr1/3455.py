#include <iostream>
#include <stdio.h>

using namespace std;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for (int t = 0; t < T; ++t) {
        int s_max;
        cin >> s_max;
        int sum = 0;
        int add = 0;
        for (int i = 0; i <= s_max; ++i) {
            char c;
            cin >> c;
            if (sum < i) add = max(add, i - sum);
            sum += c - '0';
        }
        cout << "Case #" << t + 1 << ": " << add << "\n";
    }
    return 0;
}

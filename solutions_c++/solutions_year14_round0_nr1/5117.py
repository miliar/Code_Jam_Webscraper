#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

string solve() {
    int r, x, s[4], t[4];
    cin >> r;
    for (int i = 1; i <= 4; ++i) {
        for (int j = 1; j <= 4; ++j) {
            cin >> x;
            if (i == r) {
                s[j-1] = x;
            }
        }
    }
    cin >> r;
    for (int i = 1; i <= 4; ++i) {
        for (int j = 1; j <= 4; ++j) {
            cin >> x;
            if (i == r) {
                t[j-1] = x;
            }
        }
    }
    int ans = -1, count = 0;
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            if (s[i] == t[j]) {
                ans = s[i];
                count += 1;
            }
        }
    }
    if (count == 0) {
        return "Volunteer cheated!"; 
    }
    if (count > 1) {
        return "Bad magician!";
    }
    return to_string(ans);
}

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ": " << solve() << "\n";
    }
    return 0;
}

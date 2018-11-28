#include <iostream>
using namespace std;

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T;
    cin >> T;
    for(int t = 0; t < T; t++) {
        string s;
        cin >> s;
        s += "+";
        int flips = 0;
        for(int i = s.size() - 1; i > 0; i--) {
            flips += s[i] != s[i - 1];
        }
        printf("Case #%d: %d\n", t + 1, flips);
    }
    return 0;
}

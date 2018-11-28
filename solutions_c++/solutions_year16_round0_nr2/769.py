#include <iostream>
#include <string>
using namespace std;

int main() {
    long T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        string s;
        cin >> s;
        s += "+";
        long ans = 0;
        for (int i = 1; i < s.size(); i++) ans += s[i] != s[i-1];
        cout << "Case #" << t << ": " << ans << endl;
    }
}

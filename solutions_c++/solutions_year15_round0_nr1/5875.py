#include <iostream>
#include <string>

using namespace std;

int main() {
    int t;
    cin >> t;
    for (int tc = 0; tc < t; tc++) {
        string s;
        int l, curr = 0, sol = 0;
        cin >> l;
        cin >> s;
        for (int i = 0; i < s.length(); i++) {
            if (i > curr) {
                sol += i - curr;
                curr += (i - curr);
            }
            curr += (s[i] - '0') ;
        }
        cout << "Case #" << tc + 1 << ": " << sol << endl;
    }
    return 0;
}
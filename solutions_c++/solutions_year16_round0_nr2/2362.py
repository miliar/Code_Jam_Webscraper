#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    int nT;
    cin >> nT;
    for (int t = 1; t <= nT; ++t) {
        string s;
        cin >> s;
        reverse(s.begin(), s.end());
        char oldCh = '+';
        int changes = 0;
        for (char c: s) {
            if (c != oldCh) {
                ++changes;
                oldCh = c;
            }
        }
        cout << "Case #" << t << ": " << changes << endl;
    }

    return 0;
}

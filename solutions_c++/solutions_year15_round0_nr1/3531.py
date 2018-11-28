#include <iostream>

using namespace std;

void solve(const int test) {
    int _; string s; cin >> _ >> s;
    int standing = 0;
    int friends = 0;
    for (int i=0; i<int(s.size()); ++i) {
        if (i > standing) {
            friends += i - standing;
            standing += i - standing;
        }
        standing += s[i] - '0';
    }
    cout << "Case #" << test << ": " << friends << endl;
}

int main() {
    int t; cin >> t;
    for (int e=0; e<t; ++e)
        solve(e+1);

    return 0;
}


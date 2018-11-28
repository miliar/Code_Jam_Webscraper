#include <iostream>

using std::cin;
using std::cout;
using std::endl;
using std::string;

void solve() {
    int k;
    string s;
    cin >> s >> k;
    int cake = 0, flip_count = 0;
    while (cake < s.size() - k + 1) {
        if (s[cake] == '+') {
            ++cake;
        } else {
            ++flip_count;
            for (int i = 0; i < k; ++i) {
                s[cake + i] = s[cake + i] == '+' ? '-' : '+';
            }
            ++cake;  
        } 
    }
    if (count(s.begin(), s.end(), '+') != s.size()) {
        cout << "IMPOSSIBLE" << endl;
    } else {
        cout << flip_count << endl;
    }    
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
    return 0;
}

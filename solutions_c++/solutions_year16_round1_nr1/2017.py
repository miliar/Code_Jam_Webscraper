#include <bits/stdc++.h>

using namespace std;

int main (void) {
    int T;
    cin >> T;
    for (int c = 1; c <= T; ++c) {
        string s;
        cin >> s;
        printf ("Case #%d: ", c);
        
        deque <char> res;
        res.push_back (s[0]);
        for (int i = 1; i < s.size(); ++i) {
            if (s[i] >= res.front()) res.push_front(s[i]);
            else res.push_back (s[i]);
        }
        for (auto x : res) cout << x;
        cout << endl;
    }
    return 0;
}

#include <bits/stdc++.h>

using namespace std;

int main() {
    int test;
    cin >> test;
    for (int t = 1; t <= test; ++t) {
        string s;
        cin >> s;
        deque<char> q;
        q.push_back(s[0]);
        for (int i = 1; i < s.size(); ++i) {
            if (s[i] < q.front()) {
                q.push_back(s[i]);
            }
            else {
                q.push_front(s[i]);
            }
        }
        cout << "Case #" << t << ": ";
        for (char c : q) {
            cout << c;
        }
        cout << '\n';
    }
    return 0;
}

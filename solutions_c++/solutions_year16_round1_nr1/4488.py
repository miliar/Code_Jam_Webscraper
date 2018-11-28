#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin >> t;
    for (int cs = 1; cs <= t; ++cs) {
        cout << "Case #" << cs << ": ";

        string s;
        cin >> s;
        deque<char> d;

        d.push_back(s[0]);

        for (int i = 1; i < s.length(); ++i) {
            if (s[i] >= d[0]) {
                d.push_front(s[i]);
            } else {
                d.push_back(s[i]);
            }
        }

        while (!d.empty()) {
            cout << d.front();
            d.pop_front();
        }
        cout << endl;
    }
}

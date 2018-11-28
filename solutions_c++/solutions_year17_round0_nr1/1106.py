#include <bits/stdc++.h>

using namespace std;

int t, k;
string s;
int main() {
    cin >> t;
    for (int test = 1; test <= t; test++) {
        cin >> s >> k;
        int flips = 0;
        for (int i = 0; i <= s.size() - k; i++) {
            if (s[i] != '+') {
                flips++;
                for (int j = i; j < i + k; j++) {
                    s[j] = (s[j] == '+' ? '-' : '+');
                }
            }
        }
        bool works = true;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] != '+') {
                works = false;
                break;
            }
        }
        cout << "Case #" << test << ": ";
        if (works) cout << flips << endl;
        else cout << "IMPOSSIBLE" << endl;
    }
}
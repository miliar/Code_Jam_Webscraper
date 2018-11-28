#include <bits/stdc++.h>

using namespace std;

string s;

int main() {
    int t;
    cin >> t;
    for (int test = 1; test <= t; test++) {
        cin >> s;
        string newS;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] >= newS[0]) {
                newS = s[i] + newS;
            } else {
                newS = newS + s[i];
            }
        }
        cout << "Case #" << test << ": " << newS << endl;
    }
}
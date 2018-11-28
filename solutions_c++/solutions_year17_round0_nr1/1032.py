#include <iostream>
using namespace std;

int main() {
    int i, j, t, T, k;
    string s;
    cin >> T;
    for (t = 1; t <= T; t++) {
        cin >> s >> k;

        int r = 0;
        for (i = 0; i <= s.size()-k; i++) {
            if (s[i] == '-') {
                for (j = i; j < i+k; j++) s[j] = s[j] == '-' ? '+' : '-';
                r++;
            }
        }
        int correct = 1;
        for (i = 0; i < s.size(); i++) {
            if (s[i] == '-') correct = 0;
        }
        cout << "Case #" << t << ": ";
        correct ? cout << r : cout << "IMPOSSIBLE";
        cout << endl;
    } 
}
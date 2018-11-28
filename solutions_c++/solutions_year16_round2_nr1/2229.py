#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>

using namespace std;

int T;
int a[26], c[10];

string s;

int main() {
    std::ios_base::sync_with_stdio(false);
    cin >> T;
    for (int _t = 0; _t < T; ++_t) {
        for (int i = 0; i < 26; ++i) {
            a[i] = 0;
        }
        for (int i = 0; i < 10; ++i) {
            c[i] = 0;
        }
        cin >> s;
        for (int i = 0; i < s.length(); ++i) {
            a[s[i] - 'A']++;
        }
        c[0] = a['Z' - 'A'];
        c[6] = a['X' - 'A'];
        c[8] = a['G' - 'A'];
        c[2] = a['W' - 'A'];
        c[3] = a['T' - 'A'] - c[2] - c[8];
        c[4] = a['R' - 'A'] - c[0] - c[3];
        c[5] = a['F' - 'A'] - c[4];
        c[7] = a['V' - 'A'] - c[5];
        c[1] = a['O' - 'A'] - c[0] - c[2] - c[4];
        c[9] = a['I' - 'A'] - c[5] - c[6] - c[8];

        cout << "Case #" << _t + 1 << ": ";
        for (int i = 0; i < 10; ++i) {
            for (int j = 0; j < c[i]; ++j) cout << i;
        }
        cout << endl;
    }
}
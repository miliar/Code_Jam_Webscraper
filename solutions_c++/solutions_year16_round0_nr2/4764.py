#include <iostream>
#include <string>

using namespace std;

int t;
bool v[100];
string s;

int main() {
    cin >> t;
    for (int i = 0; i ++< t;) {
        cin >> s;
        int n = 0, l = s.length();
        for (int j = 0; j < l; ++j) v[j] = s[j] == '+';
        while (1) {
            int s = 0, e = l - 1;
            while (s < l && v[s]) v[s++] = 0;
            if (s == l) break;
            if (s) ++n;
            while (v[e]) --e;
            if (e < 0) break;
            for (int t, j = 0; j <= e / 2; ++j) t = v[j], v[j] = v[e-j] ^ 1, v[e-j] = t ^ 1;
            ++n;
        }
        cout << "Case #" << i << ": " << n << '\n';
    }
}



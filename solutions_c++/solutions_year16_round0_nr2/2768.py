#include <iostream>
#include <string>
using namespace std;

void flip(string &s, int pos) {
    int i, j;
    for (i = 0, j = pos - 1; i < j; i++, j--) {
        swap(s[i], s[j]);
        s[i] = '+' ^ '-' ^ s[i];
        s[j] = '+' ^ '-' ^ s[j];
    }
    if (i == j) {
        s[i] = '+' ^ '-' ^ s[i];
    }
}

int main() {
    int t;
    cin >> t;
    for (int ii = 1; ii <= t; ii++) {
        string s;
        cin >> s;
        int count = 0;
        int p = s.size();
        while (p > 0) {
            while (p > 0 && s[p - 1] == '+') p--;
            if (p == 0) break;
            int q = 0;
            while (q < p && s[q] == '+') q++;
            if (q > 0) flip(s, q);
            else flip(s, p);
            count++;
        }
        cout << "Case #" << ii << ": " << count << endl;
    }
    return 0;
}


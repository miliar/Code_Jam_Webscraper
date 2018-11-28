#include <iostream>
#include <string>

using namespace std;

int calc_len(string &s, int curlen) {
    int l;
    for (l = curlen; l > 0; l--) {
        if (s[l-1] == '-') {
            break;
        }
    }
    return l;
}

void flip(string &s, int amt) {
    for (int i = 0; i < amt/2; i++) {
        char tmp = s[i];
        s[i] = s[amt-i-1];
        s[amt-i-1] = tmp;
    }
    for (int i = 0; i < amt; i++) {
        if (s[i] == '-') {
            s[i] = '+';
        } else {
            s[i] = '-';
        }
    }
}

int count_plus(string &s) {
    int count = 0;
    while (s[count] == '+') {
        count++;
    }
    return count;
}

int main()
{
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cout << "Case #" << t << ": ";

        string s;
        cin >> s;
        int len = calc_len(s, s.size());
        int flips = 0;
        while (len > 0) {
            if (s[0] == '-') {
                flip(s, len);
                len = calc_len(s, len);
            } else {
                flip(s, count_plus(s));
            }
            flips++;
        }

        cout << flips << "\n";
    }
}

#include <iostream>
#include <algorithm>
using namespace std;
int c[26], d[10][26];
string m[] = {
    "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
};

int p[] = {0, 2, 8, 3, 4, 5, 1, 6, 7, 9};

void init() {
    memset(d, 0, sizeof d);
    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < m[i].size(); j++) {
            d[i][m[i][j] - 'A']++;
        }
    }
}

bool isExist(int n) {
    for (int i = 0; i < 26; i++) {
        if (c[i] < d[n][i]) return false;
    }

    for (int i = 0; i < 26; i++) {
        c[i] -= d[n][i];
    }
    return true;
}

int main() {
    init();
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        cout << "Case #" << i << ": ";
        string s;
        cin >> s;

        memset(c, 0, sizeof c);
        for (int j = 0; j < s.size(); j++) {
            c[s[j] - 'A']++;
        }

        string ret = "";
        for (int j = 0; j < 10; j++) {
            while (isExist(p[j])) ret += ('0' + p[j]);
        }
        sort(ret.begin(), ret.end());
        cout << ret << endl;
    }
    return 0;
}

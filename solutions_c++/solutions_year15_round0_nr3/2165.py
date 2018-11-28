#include <iostream>
#include <cstdio>
#include <vector>
#include <cstring>
using namespace std;

int f[10][10];
int m[20000][20000];

int mult(int a, int b) {
    int mi = 0;
    if (a < 0) {
        a = -a;
        ++mi;
    }
    if (b < 0) {
        b = -b;
        ++mi;
    }
    int r = f[a][b];
    if (r < 0) {
        r = -r;
        ++mi;
    }
    if (mi % 2) r = -r;
    return r;
}

int get(char c) {
    if (c == '1') return 1;
    if (c == 'i') return 2;
    if (c == 'j') return 3;
    if (c == 'k') return 4;
}


int main() {

    f[1][1] = 1; f[1][2] = 2; f[1][3] = 3; f[1][4] = 4;
    f[2][1] = 2; f[2][2] = -1; f[2][3] = 4; f[2][4] = -3;
    f[3][1] = 3; f[3][2] = -4; f[3][3] = -1; f[3][4] = 2;
    f[4][1] = 4; f[4][2] = 3; f[4][3] = -2; f[4][4] = -1;


    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int test;
    cin >> test;
    for (int t = 1; t <= test; ++t) {

        long long x, l;
        cin >> l >> x;
        string ss;
        cin >> ss;
        string s = "";
        string ans = "NO";
        for (int i = 0; i < x; ++i)
            s += ss;
        for (int i = 0; i < s.length(); ++i) {
            m[i][i] = get(s[i]);
            for (int j = i + 1; j < s.length(); ++j) {
                m[i][j] = mult(m[i][j - 1], get(s[j]));
            }
        }
        for (int i = 1; i < s.length() - 1; ++i)
            for (int j = i; j < s.length() - 1; ++j)
                if (m[0][i - 1] == 2 && m[i][j] == 3 && m[j + 1][s.length() - 1] == 4) ans = "YES";

        cout << "Case #" << t << ": " << ans << endl;
    }
    return 0;
}

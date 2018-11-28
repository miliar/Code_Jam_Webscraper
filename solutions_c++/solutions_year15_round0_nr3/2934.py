#include <bits/stdc++.h>

using namespace std;

typedef pair<int, char> pic;

int m[10][10];

int val(char c) {
    return c - 'i' + 2;
}

int sign(int x) {
    if (x < 0) {
        return -1;
    }
    return 1;
}

int mul(int a, int b) {
    return sign(a) * sign(b) * m[abs(a)][abs(b)];
}

int t, n, x;
string s, ss;

int cas = 1;

int main() {
    //ios::sync_with_stdio(false);
    //cin.tie(false);
    freopen("dat.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    m[1][1] = 1; m[1][2] = 2; m[1][3] = 3; m[1][4] = 4;
    m[2][1] = 2; m[2][2] = -1; m[2][3] = 4; m[2][4] = -3;
    m[3][1] = 2; m[3][2] = -4; m[3][3] = -1; m[3][4] = 2;
    m[4][1] = 4; m[4][2] = 3; m[4][3] = -2; m[4][4] = -1;
    cin >> t;
    while (t--) {
        cin >> n >> x >> s;
        int cur = 1;
        cout << "Case #" << cas++ << ": ";
        bool I = false;
        bool K = false;
        for (int i = 0; i < n * x; i++) {
            int y = val(s[i % n]);
            //cout << cur << " " << y << " " << mul(cur, y) << "\n";
            cur = mul(cur, y);
            if (cur == 2) {
                I = true;
            }
            if (I && cur == 4) {
                K = true;
            }
        }
        if (cur == -1 && I && K) {
            cout << "YES\n";
        } else {
            cout << "NO\n";
        }
    }
}

#include <bits/stdc++.h>
using namespace std;

int hsans[13][3];

void init() {
    hsans[0][0] = 1;
    hsans[0][1] = hsans[0][2] = 0;
    for (int i = 1; i < 13; i++) {
        hsans[i][0] = hsans[i - 1][0] + hsans[i - 1][2];
        hsans[i][1] = hsans[i - 1][1] + hsans[i - 1][0];
        hsans[i][2] = hsans[i - 1][2] + hsans[i - 1][1];
    }
}

string getans(int n, int w) {
    if (n == 0) {
        if (w == 0) 
            return "S";
        else if (w == 1)
            return "P";
        else
            return "R";
    } else {
        string a = getans(n - 1, w), b = getans(n - 1, (w + 1) % 3);
        if (a < b) {
            return a + b;
        } else {
            return b + a;
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    init();
    int T;
    cin >> T;
    for (int tsk = 1; tsk <= T; tsk++) {
        int n, r, p, s;
        cin >> n >> r >> p >> s;
        cout << "Case #" << tsk << ": ";
        if (s == hsans[n][0] && p == hsans[n][1] && r == hsans[n][2]) {
            cout << getans(n, 0) << endl;
        } else if (p == hsans[n][0] && r == hsans[n][1] && s == hsans[n][2]) {
            cout << getans(n, 1) << endl;
        } else if (r == hsans[n][0] && s == hsans[n][1] && p == hsans[n][2]) {
            cout << getans(n, 2) << endl;
        } else {
            cout << "IMPOSSIBLE" << endl;
        }
    }
}

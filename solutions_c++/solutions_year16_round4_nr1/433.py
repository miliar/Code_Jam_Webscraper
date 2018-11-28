#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

int R, P, S, n;
int cnt[3];
string optStr[3][20];
string sol;

int isvalid(string a) {
    int acnt[3];
    acnt[0] = 0;
    acnt[1] = 0;
    acnt[2] = 0;
    for (int i = 0; i < a.size(); i++) {
        acnt[a[i] - '0']++;
    }
    return (acnt[0] == cnt[0] && acnt[1] == cnt[1] && acnt[2] == cnt[2]);
}

void updatesol(string a) {
    if (isvalid(a)) {
        if (sol.compare("") == 0 || a.compare(sol) < 0) {
            sol = a;
        }
    }
}

string solve(int winner, int n) {

    if (optStr[winner][n].compare("") != 0) {
        return optStr[winner][n];
    }
    if (n == 0) {
        optStr[winner][0] = winner + '0';
        return optStr[winner][0];
    }

    string a = solve(winner, n - 1);
    string b = solve((winner + 1) % 3, n - 1);

    if (a.compare(b) < 0) {
        optStr[winner][n] = a + b;
    } else {
        optStr[winner][n] = b + a;
    }
    return optStr[winner][n];
}

int main() {
    int T, tc;

    cin >> T;
    for (tc = 1; tc <= T; tc++) {
        cout << "Case #" << tc << ": ";
        
        cin >> n >> cnt[1] >> cnt[0] >> cnt[2];

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 20; j++) {
                optStr[i][j] = "";
            }
        }
        sol = "";

        solve(0, n);
        solve(1, n);
        solve(2, n);

        updatesol(optStr[0][n]);
        updatesol(optStr[1][n]);
        updatesol(optStr[2][n]);

        if (sol.compare("") == 0) {
            cout << "IMPOSSIBLE" << endl;
        } else {
            for (int i = 0; i < sol.size(); i++) {
                if (sol[i] == '0') cout << 'P';
                if (sol[i] == '1') cout << 'R';
                if (sol[i] == '2') cout << 'S';
            }
            cout << endl;
        }
    }
    return 0;
}

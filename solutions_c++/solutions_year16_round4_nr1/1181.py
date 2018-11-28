#include <bits/stdc++.h>

using namespace std;

string s[3][13];
int cnt[3][13][3];

string solve() {
    int n;
    scanf("%d", &n);
    int R, P, S;
    scanf("%d%d%d", &R, &P, &S);
    for(int i = 0; i < 3; i++) {
        if(cnt[i][n][0] == P && cnt[i][n][1] == R && cnt[i][n][2] == S) {
            return  s[i][n];
        }
    }
    return "IMPOSSIBLE";
}

int main() {
    s[0][0] = "P";
    s[1][0] = "R";
    s[2][0] = "S";
    for(int i = 1; i <= 12; i++) {
        for(int j = 0; j < 3; j++) {
            int k = (j + 1) % 3;
            if(strcmp(s[j][i - 1].c_str(), s[k][i - 1].c_str()) < 0) {
                s[j][i] = s[j][i - 1] + s[k][i - 1];
            } else {
                s[j][i] = s[k][i - 1] + s[j][i - 1];
            }
        }
    }
    for(int i = 0; i < 3; i++) {
        for(int j = 0; j < 3; j++) {
            cnt[i][0][j] = 0;
        }
        cnt[i][0][i] = 1;
    }
    for(int i = 1; i <= 12; i++) {
        for(int j = 0; j < 3; j++) {
            int jj = (j + 1) % 3;
            for(int k = 0; k < 3; k++) {
                cnt[j][i][k] = cnt[j][i - 1][k] + cnt[jj][i - 1][k];
            }
        }
    }
    freopen("A-large.in", "r", stdin);
    freopen("A-small-attempt1.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int TTT = 1; TTT <= T; TTT++) printf("Case #%d: %s\n", TTT, solve().c_str());
    return 0;
}

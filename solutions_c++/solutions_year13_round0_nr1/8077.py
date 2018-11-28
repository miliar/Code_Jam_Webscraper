#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

int t;
vector<string> m;
char winner = -1;

bool hWin() {
    for (int i = 0; i < 4; i++) {
        if (m[i][0]==m[i][1] && m[i][1]==m[i][2] && (m[i][2]==m[i][3] || m[i][3]=='T') && m[i][0]!='.') {
            winner = m[i][0];
            return true;
        }
        if (m[i][3]==m[i][2] && m[i][2]==m[i][1] && (m[i][1]==m[i][0] || m[i][0]=='T') && m[i][3]!='.') {
            winner = m[i][3];
            return true;
        }
    }
    return false;
}

bool vWin() {
    for (int i = 0; i < 4; i++) {
        if (m[0][i]==m[1][i] && m[1][i]==m[2][i] && (m[2][i]==m[3][i] || m[3][i]=='T') && m[0][i]!='.') {
            winner = m[0][i];
            return true;
        }
        if (m[3][i]==m[2][i] && m[2][i]==m[1][i] && (m[1][i]==m[0][i] || m[0][i] =='T') && m[3][i]!='.') {
            winner = m[3][i];
            return true;
        }
    }
    return false;
}

bool isComplete() {
    for (int i = 0; i < 4; i++)
        for (int j = 0; j < 4; j++)
            if (m[i][j]=='.')
                return false;
    return true;
}

bool dWin() {
    if (m[0][0]==m[1][1] && m[1][1]==m[2][2] && (m[2][2]==m[3][3] || m[3][3]=='T') && m[0][0]!='.') {
        winner = m[0][0];
        return true;
    }
    if (m[3][3]==m[2][2] && m[2][2]==m[1][1] && (m[1][1]==m[0][0] || m[0][0]=='T') && m[3][3]!='.') {
        winner = m[3][3];
        return true;
    }
    if (m[0][3]==m[1][2] && m[1][2]==m[2][1] && (m[2][1]==m[3][0] || m[3][0]=='T') && m[0][3]!='.') {
        winner = m[0][3];
        return true;
    }
    if (m[3][0]==m[2][1] && m[2][1]==m[1][2] && (m[1][2]==m[0][3] || m[0][3]=='T') && m[3][0]!='.') {
        winner = m[3][0];
        return true;
    }
    return false;
}

void solve() {
    if (hWin() || vWin() || dWin())
        cout << winner << " won" << endl;
    else
        cout << (isComplete() ? " Draw" : " Game has not completed") << endl;
}

int main() {
    scanf("%d", &t);
    for (int i = 1; i <= t; i++) {
        m.clear();
        string line;
        for (int j = 0; j < 4; j++) {
            cin >> line;
            m.push_back(line);
        }
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}

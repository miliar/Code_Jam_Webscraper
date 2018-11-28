#include<iostream>
#include<fstream>
#include<sstream>
#include<cstdio>
#include<algorithm>
#include<string>
#include<vector>
#include<map>
#include<cstring>
using namespace std;

#define FOR(I,A,B) for (int I=int(A);I<int(B);++I)
#define MEM(A,B) memset(A,B,sizeof(A))
#define CPY(A,B) memcpy(A,B,sizeof(B))
#define FIN(A) freopen(A, "r", stdin)
#define FOUT(A) freopen(A, "w", stdout)
typedef long long LL;

string str[4];
int win(string s) {
    int x = 0, o = 0, t = 0;
    FOR(i, 0, 4)
        if (s[i] == 'X') ++x;
        else if (s[i] == 'O') ++o;
        else if (s[i] == 'T') ++t;
    if (x == 4 || x == 3 && t == 1) return 1;
    if (o == 4 || o == 3 && t == 1) return -1;
    return 0;
}
int solve() {
    string tmp;
    FOR(i, 0, 4)
        if (win(str[i]) != 0) return win(str[i]);
    FOR(i, 0, 4) {
        tmp = "";
        FOR(j, 0, 4)
            tmp += str[j][i];
        if (win(tmp) != 0) return win(tmp);
    }
    tmp = "";
    FOR(i, 0, 4) 
        tmp += str[i][i];
    if (win(tmp) != 0) return win(tmp);
    tmp = "";
    FOR(i, 0, 4)
        tmp += str[i][3 - i];
    if (win(tmp) != 0) return win(tmp);
    return 0;
}
int main() {
    freopen("in.txt", "r", stdin);
    int ca;
    cin >> ca;
    FOR(c, 1, ca + 1) {
        int dot = 0;
        FOR(i, 0, 4) {
            cin >> str[i];
            FOR(j, 0, 4)
                if (str[i][j] == '.') ++dot;
        }
        cout << "Case #" << c << ": ";
        int end = solve();
        if (end == 0) {
            if (dot == 0) cout << "Draw" << endl;
            else cout << "Game has not completed" << endl;
        }
        else if (end == 1) cout << "X won" << endl;
        else cout << "O won" << endl;
    }
    return 0;
}   

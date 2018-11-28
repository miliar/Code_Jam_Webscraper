#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <iostream>
#include <cassert>
using namespace std;


#define INF 1e+9
#define mp make_pair
#define lint long long
#define pii pair<int, int>
#define MAXN 101000

int decode(char x) {
    if (x == '1') return 0;
    if (x == 'i') return 1;
    if (x == 'j') return 2;
    if (x == 'k') return 3;
    return 4;
}

int cnst[4][4] = {
    {0, 1, 2, 3},
    {1, 0+4, 3, 2+4},
    {2, 3+4, 0+4, 1},
    {3, 2, 1+4, 0+4}
};

int mult[8][8];
int s[MAXN];
int mark[MAXN];

int main() {
    ios_base::sync_with_stdio(false);
    for (int i = 0; i < 8; i++) {
        for (int j = 0; j < 8; j++) {
            int m = 0;
            if (i >= 4) {m++;}
            if (j >= 4) {m++;}
            mult[i][j] = (cnst[i%4][j%4] + (m * 4)) % 8;
        }
    }
    int t; cin >> t;
    for (int ii = 0; ii < t; ii++) {
        int l, x; cin >> l >> x;
        for (int i = 0; i < l; i++) {
            char x; cin >> x;
            s[i] = decode(x);
        }
        for (int i = 1; i < x; i++) {
            for (int j = 0; j < l; j++)
                s[i * l + j] = s[j];
        }
        int imul = 0;
        for (int i = 0; i < x * l; i++)
            imul = mult[imul][s[i]];
        if (imul != mult[1][mult[2][3]]) {
            cout << "Case #" << ii + 1 << ": NO\n";
        } else {
            int m0 = 0;
            int flag = 0;
            for (int i = 0; i < x * l; i++) {
                m0 = mult[m0][s[i]];
                if (m0 == 1 && flag == 0) flag++;
                if (m0 == mult[1][2] && flag == 1) {
                    flag++;
                    cout << "Case #" << ii + 1 << ": YES\n";
                    break;
                }
            }
            if (flag != 2) 
                cout << "Case #" << ii + 1 << ": NO\n";
        }
    }
}

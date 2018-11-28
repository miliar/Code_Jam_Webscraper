#include <set>
#include <map>
#include <ctime>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <string>
#include <cstdlib>
#include <iostream>
#include <algorithm>

#define MaxN 15
#define MaxSize 5010

using namespace std;

int N, R, P, S;
int dep[MaxN][3];
char str[MaxSize];
string ans[MaxN][3];

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T, T0 = 0;
    scanf("%d", &T);
    ans[0][0] = "R";
    ans[0][1] = "P";
    ans[0][2] = "S";
    for (int i = 1; i <= 12; ++i) {
        for (int k = 0; k < 3; ++k) {
            ans[i][k] = "";
            string a, b;
            if (k == 0) {
                a = ans[i - 1][0];
                b = ans[i - 1][2];
            }
            if (k == 1) {
                a = ans[i - 1][0];
                b = ans[i - 1][1];
            }
            if (k == 2) {
                a = ans[i - 1][1];
                b = ans[i - 1][2];
            }
            if (a > b) swap(a, b);
            ans[i][k] += a;
            ans[i][k] += b;
        }
    }
    for ( ; T; --T) {
        scanf("%d%d%d%d", &N, &R, &P, &S);
        int cntR = 0, cntP = 0, cntS = 0;
        int newR = 0, newP = 0, newS = 0;
        bool flag = false;

        cntR = 1;
        for (int i = 1; i <= N; ++i) {
            newR = cntR + cntP;
            newP = cntP + cntS;
            newS = cntS + cntR;
            cntR = newR;
            cntP = newP;
            cntS = newS;
        }
        if (cntR == R && cntP == P && cntS == S) {
            str[0] = 'R';
            flag = true;
        }
        cntR = 0, cntP = 0, cntS = 0;
        newR = 0, newP = 0, newS = 0;
        cntP = 1;
        for (int i = 1; i <= N; ++i) {
            newR = cntR + cntP;
            newP = cntP + cntS;
            newS = cntS + cntR;
            cntR = newR;
            cntP = newP;
            cntS = newS;
        }
        if (cntR == R && cntP == P && cntS == S) {
            str[0] = 'P';
            flag = true;
        }
        cntR = 0, cntP = 0, cntS = 0;
        newR = 0, newP = 0, newS = 0;
        cntS = 1;
        for (int i = 1; i <= N; ++i) {
            newR = cntR + cntP;
            newP = cntP + cntS;
            newS = cntS + cntR;
            cntR = newR;
            cntP = newP;
            cntS = newS;
        }
        if (cntR == R && cntP == P && cntS == S) {
            str[0] = 'S';
            flag = true;
        }
        if (!flag) {
            printf("Case #%d: IMPOSSIBLE\n", ++T0);
        }
        else {
            printf("Case #%d: ", ++T0);
            if (str[0] == 'R') cout << ans[N][0] << endl;
            if (str[0] == 'P') cout << ans[N][1] << endl;
            if (str[0] == 'S') cout << ans[N][2] << endl;
        }
    }
    return 0;
}

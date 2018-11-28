#include <iostream>
#include <cstdio>
#include <queue>
#include <cmath>

using namespace std;

#define MAX 10005

int mulArr[5][5] = { { 0, 0, 0, 0, 0 }, { 0, 1, 2, 3, 4 }, { 0, 2, -1, 4, -3 },
        { 0, 3, -4, -1, 2 }, { 0, 4, 3, -2, -1 } };

int multiply(int val1, int val2) {
    bool neg = (val1 < 0) ^ (val2 < 0);
    
    int v1 = abs(val1);
    int v2 = abs(val2);

    int ml = mulArr[v1][v2];

    if (neg)
        return -ml;

    return ml;
}

bool possible(char *str, int len, int repeatition) {
    int strMul = 1;

    for (char *p = str; *p; p++)
        strMul = multiply(strMul, *p - 'i' + 2);

    int i = 0;
    int mul = 1;
    int nextTarget = 2;

    for (int repLeft = repeatition; repLeft; repLeft--) {
        for (char *p = str; *p; p++) {
            mul = multiply(mul, *p - 'i' + 2);

            if (mul == nextTarget && nextTarget != 4) {
                nextTarget++;
                mul = 1;
            }
        }

        if (nextTarget == 4) {
            repLeft--;

            while (repLeft--)
                mul = multiply(mul, strMul);

            return mul == 4;
        }
    }

    return false;
}

int main() {
    //freopen("/home/crysoberil/a", "r", stdin);

    cin.sync_with_stdio(false);
    cout.sync_with_stdio(false);

    int testCase;
    char str[MAX];

    cin >> testCase;

    for (int kase = 1; kase <= testCase; kase++) {
        int len, repeatition;

        cin >> len >> repeatition >> str;

        if (possible(str, len, repeatition))
            cout << "Case #" << kase << ": YES\n";
        else
            cout << "Case #" << kase << ": NO\n";
    }

    return 0;
}

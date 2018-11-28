#include <iostream>
#include <cstdio>

using namespace std;


bool r(char a, char b, char c, char d, char e) {
    return ((a == b) && (b == c) && (c == d) && (d == e));
}
int main()
{
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    int t;
    scanf("%d\n", &t);
    char a[20];
    bool f = false;
    char c;
    for (int i = 0; i < t; ++i) {
        f = false;
        c = '\n';
        while (c == '\n') {
            scanf("%c", &c);
        }
        a[0] = c;
        scanf("%c%c%c", &a[1], &a[2], &a[3] );
        scanf("%c", &c);
        scanf("%c%c%c%c", &a[4], &a[5], &a[6], &a[7] );
        scanf("%c", &c);
        scanf("%c%c%c%c", &a[8], &a[9], &a[10], &a[11]);
        scanf("%c", &c);
        scanf("%c%c%c%c", &a[12], &a[13], &a[14], &a[15]);
        int mm = -1;
        for (int ii = 0; ii < 16; ++ii) {
            if (a[ii] == 'T') mm = ii;
        }
        cout << "Case #" << i + 1 << ": ";
        for (int k = 0; k < 4; ++k) {
            if (mm != -1) a[mm] = 'O';
            if (r(a[k * 4], a[k * 4 + 1], a[k * 4 + 2], a[k * 4 + 3], 'O')) {
                cout << "O won" << endl;
                f = true;
                break;
            }
            if (r(a[k] ,  a[k + 4] ,  a[k + 8] ,  a[k + 12] ,  'O')) {
                cout << "O won" << endl;
                f = true;
                break;
            }
            if (r(a[0] ,  a[5] ,  a[10] ,  a[15] ,  'O')) {
                cout << "O won" << endl;
                f = true;
                break;
            }
            if (r(a[3] ,  a[6] ,  a[9] ,  a[12] ,  'O')) {
                cout << "O won" << endl;
                f = true;
                break;
            }
            if (mm != -1) a[mm] = 'X';
            if (r(a[k] ,  a[k + 4] ,  a[k + 8] ,  a[k + 12] ,  'X')) {
                cout << "X won" << endl;
                f = true;
                break;
            }
            if (r(a[0] ,  a[5] ,  a[10] ,  a[15] ,  'X')) {
                cout << "X won" << endl;
                f = true;
                break;
            }
            if (r(a[k * 4] ,  a[k * 4 + 1] ,  a[k * 4 + 2] ,  a[k * 4 + 3] ,  'X')) {
                cout << "X won" << endl;
                f = true;
                break;
            }
            if (r(a[3] ,  a[6] ,  a[9] ,  a[12] ,  'X')) {
                cout << "X won" << endl;
                f = true;
                break;
            }
        }
        if (f) {
            continue;
        }
        f = false;
        for (int k = 0; k < 16; ++k) {
            if (a[k] == '.') f = true;
        }
        if (f) {
            cout << "Game has not completed" << endl;
        } else {
            cout << "Draw" << endl;
        }
    }
    return 0;
}

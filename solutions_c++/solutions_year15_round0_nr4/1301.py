#include <iostream>
#include <stdio.h>

using namespace std;
const int ans[4][4][4] =
{
    0, 0, 0, 0,
    0, 0, 0, 0,
    0, 0, 0, 0,
    0, 0, 0, 0,
    1, 0, 1, 0,
    0, 0, 0, 0,
    1, 0, 1, 0,
    0, 0, 0, 0,
    1, 1, 1, 1,
    1, 1, 0, 1,
    1, 0, 0, 0,
    1, 1, 0, 1,
    1, 1, 1, 1,
    1, 1, 1, 1,
    1, 1, 1, 0,
    1, 1, 0, 0
};
int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    cin >> T;
    for (int cas = 1; cas <= T; ++cas)
    {
        int x, r, c;
        printf("Case #%d: ", cas);
        cin >> x >> r >> c;
        if (ans[x - 1][r - 1][c - 1]) puts("RICHARD");
        else puts("GABRIEL");
    }
    return 0;
}

#include <iostream>
using namespace std;
bool precalc[4][4][4] = {
    {
        {1, 1, 1, 1},
        {1, 1, 1, 1},
        {1, 1, 1, 1},
        {1, 1, 1, 1}
    },
    {
        {0, 1, 0, 1},
        {1, 1, 1, 1},
        {0, 1, 0, 1},
        {1, 1, 1, 1}
    },
    {
        {0, 0, 0, 0},
        {0, 0, 1, 0},
        {0, 1, 1, 1},
        {0, 0, 1, 0}
    },
    {
        {0, 0, 0, 0},
        {0, 0, 0, 0},
        {0, 0, 0, 1},
        {0, 0, 1, 1}
    }
};

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int tc;
    cin >> tc;
    for (int a = 0; a < tc; ++a) {
        int X, R, C;
        cin >> X >> R >> C;
        cout << "Case #" << a + 1 << ": " << (precalc[--X][--R][--C] ? "GABRIEL" : "RICHARD") << "\n";
    }
    return 0;
}
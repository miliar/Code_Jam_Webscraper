#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std;

bool win[4][4][4] = {
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
    int tt, cas = 0;
    cin >> tt;
    int a, b, c;
    while (tt--) {
        scanf("%d%d%d", &a, &b, &c);
        printf("Case #%d: %s\n", ++cas, win[a - 1][b - 1][c - 1] ? "GABRIEL" : "RICHARD");
    }
    return 0;
}

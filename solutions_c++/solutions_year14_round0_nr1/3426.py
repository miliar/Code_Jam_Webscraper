#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;

void getInt(int &x) {
    char c;
    for (c = getchar(); c < '0' || c > '9'; c = getchar());
    for (x = 0; c >= '0' && c <= '9'; c = getchar())
        x = x * 10 + c - '0';
}

int lowbitPos(int x) {
    int res = 0;
    for (; x; ++res) {
        if (1 & x)
            return res;
        x >>= 1;
    }
    return res;
}


int a[4][4];
int T, x, y, bm1, bm2;

int main() {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("a.out", "w", stdout);
    
    getInt(T);
    for (int cs = 1; cs <= T; ++cs) {
        bm1 = bm2 = 0;
        getInt(x);
        for (int i = 1; i <= 4; ++i)
            for (int j = 1; j <= 4; ++j) {
                getInt(y);
                if (i == x) bm1 |= (1 << y);
            }
        getInt(x);
        for (int i = 1; i <= 4; ++i)
            for (int j = 1; j <= 4; ++j) {
                getInt(y);
                if (i == x) bm2 |= (1 << y);
            }
        int bm = bm1 & bm2;
        printf("Case #%d: ", cs);
        if (bm == 0)
            printf("Volunteer cheated!\n");
        else if (bm == (bm & -bm))
            printf("%d\n", lowbitPos(bm));
        else
            printf("Bad magician!\n");
    }
}


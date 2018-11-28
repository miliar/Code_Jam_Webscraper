#include <cstdlib>
#include <cstdio>
#include <iostream>

using namespace std;

int main(int argc, char** argv) {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t, tc = 1;
    cin >> t;
    while (t--) {
        int x, r, c;
        cin >> x >> r >> c;

        int b = 0;

        if (x == 1)
            b = 1;

        if (x == 2 && (r * c) % 2 == 0)
            b = 1;

        else if (x == 3 && (r == 3 || c == 3) && r * c != 3)
            b = 1;

        else if (x == 4 && (r * c == 12 || r * c == 16))
            b = 1;

        if (b == 1)
            printf("Case #%d: GABRIEL\n", tc++);

        else if (b == 0)
            printf("Case #%d: RICHARD\n", tc++);
    }

    return 0;
}


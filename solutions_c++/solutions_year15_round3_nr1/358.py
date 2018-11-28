#include <iostream>
#include <stdio.h>
#include <algorithm>

using namespace std;

int T, R, C, W, inf = 1 << 29;

int main() {
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);

    cin >> T;
    for(int cs = 0; cs < T; cs++) {
        cin >> R >> C >> W;

        int find = C / W;
        int one = C % W == 0 ? 0 : 1;

        printf("Case #%d: %d\n", cs + 1, R * find + W - 1 + one);
    }

    return 0;
}

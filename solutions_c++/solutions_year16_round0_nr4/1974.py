#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
typedef unsigned long long ull;

int main() {
    int T;
    cin >> T;

    for (int t = 1; t <= T; t++) {
        ull K, C, S;
        cin >> K >> C >> S;

        ull path = 0;
        vector<ull> tiles;
        while (S--) {
            ull idx = path;

            for (ull depth = 1; depth < C; depth++) {
                if (path < K-1) path++;
                idx = idx * K + path;
            }

            tiles.push_back(idx+1);
            if (path == K-1) { // covered all possibilities
                printf("Case #%d:", t);
                for (ull tile : tiles)
                    cout << " " << tile;
                cout << endl;
                goto next_case;
            } else {
                path++; // continue from root
            }
        }

        printf("Case #%d: IMPOSSIBLE\n", t);
        next_case:;
    }

    return 0;
}

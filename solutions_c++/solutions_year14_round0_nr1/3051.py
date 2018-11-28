#include <bits/stdc++.h>

#define SZ 4

using namespace std;

int main() {
    int T;
    scanf("%d", &T);

    int grid[SZ][SZ];

    for (int i = 1; i <= T; ++i) {
        int ans;

        scanf("%d", &ans);
        vector<int> r1(4);
        for (int y = 0; y < SZ; ++y) {
            for (int x = 0; x < SZ; ++x) {
                scanf("%d", &grid[x][y]);
                if (y+1 == ans) {
                    r1[x] = grid[x][y];
                }
            }
        }

        scanf("%d", &ans);
        vector<int> r2(4);
        for (int y = 0; y < SZ; ++y) {
            for (int x = 0; x < SZ; ++x) {
                scanf("%d", &grid[x][y]);
                if (y+1 == ans) {
                    r2[x] = grid[x][y];
                }
            }
        }

        sort(r1.begin(), r1.end());
        sort(r2.begin(), r2.end());
        vector<int> u(8);
        vector<int>::iterator it = std::set_intersection (r1.begin(), r1.end(), r2.begin(), r2.end(), u.begin());
        u.resize(it-u.begin());

        int len = u.size();
        printf("Case #%d: ", i);
        if (len == 0) puts("Volunteer cheated!");
        else if (len == 1) printf("%d\n", u[0]);
        else puts("Bad magician!");
    }
}
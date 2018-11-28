#include <iostream>
#include <cstdio>
#include <cstring>
#include <utility>
#include <vector>
#include <queue>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <algorithm>
using namespace std;
typedef pair<int, int> ii;

int main()
{
    #ifndef ONLINE_JUDGE
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small.out", "w+", stdout);
    #endif

    int t;
    scanf("%d", &t);
    for (int testcase = 1; testcase <= t; ++testcase) {
        printf("Case #%d: ", testcase);
        int possible[17];
        memset(possible, 0, sizeof possible);

        int row1;
        scanf("%d", &row1);
        for (int r = 1; r <= 4; ++r)
        for (int c = 1; c <= 4; ++c) {
            int x;
            scanf("%d", &x);
            if (r == row1) ++possible[x];
        }
        int row2;
        scanf("%d", &row2);
        for (int r = 1; r <= 4; ++r)
        for (int c = 1; c <= 4; ++c) {
            int x;
            scanf("%d", &x);
            if (r == row2) ++possible[x];
        }

        int ans = -2;
        for (int i = 1; i <= 16; ++i)
        if (possible[i] == 2) {
            if (ans == -2) ans = i;
            else ans = -1;
        }
        if (ans == -2) {
            puts("Volunteer cheated!");
        } else if (ans == -1) {
            puts("Bad magician!");
        } else {
            printf("%d\n", ans);
        }
    }

    return 0;
}

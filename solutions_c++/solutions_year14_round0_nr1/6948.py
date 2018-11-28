#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>

using namespace std;

bool use[20];

int main() {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("sol.txt", "w", stdout);

    int test;
    scanf("%d", &test);

    for (int t = 1; t <= test; ++t) {
        int ans, x;
        scanf("%d", &ans); --ans;

        memset(use, 0, sizeof(use));
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                scanf("%d", &x);
                if (i == ans) use[x] = 1;
            }
        }

        int cnt = 0, card;
        scanf("%d", &ans); --ans;

        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                scanf("%d", &x);
                if (i == ans && use[x]){ ++cnt; card = x; }
            }
        }

        printf("Case #%d: ", t);
        if (cnt == 1) {
            printf("%d\n", card);
        } else {
            printf("%s\n", !cnt ? "Volunteer cheated!" : "Bad magician!");
        }
    }

    return 0;
}

#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

int main() {
    int T, cases;
    scanf("%d", &T);
    for (int cases = 1; cases <= T; cases++) {
        int row;
        scanf("%d", &row);
        int a[4];
        int p[4];
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j)
                scanf("%d", &a[j]);
            if (i+1 == row) {
                for (int j = 0; j < 4; ++j)
                    p[j] = a[j];
            }
        }
        scanf("%d", &row);
        vector<int> ans(0);
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                scanf("%d", &a[j]);
            }
            if (i+1 == row) {
                for (int j = 0; j < 4; ++j) {
                    for (int k = 0; k < 4; ++k) {
                        if (p[k] == a[j])
                            ans.push_back(a[j]);
                    }
                }
            }
        }
        if (ans.size() == 0) {
            printf("Case #%d: Volunteer cheated!\n", cases);
        } else if (ans.size() >= 2) {
            printf("Case #%d: Bad magician!\n", cases);
        } else {
            printf("Case #%d: %d\n", cases, ans[0]);
        }
    }
}

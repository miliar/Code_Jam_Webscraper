#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
using namespace std;

int n, r1, r2, brd1[4][4], brd2[4][4];

int main() {
    cin >> n;
    for (int tc = 1; tc <= n; tc++) {
        cin >> r1;
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++)
                cin >> brd1[i][j];
        cin >> r2;
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++)
                cin >> brd2[i][j];
        r1--;r2--;        
        int ans = -1, cnt = 0;
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++)
                if (brd1[r1][i] == brd2[r2][j]) {
                    ans = brd1[r1][i];
                    cnt++;
                }
        printf("Case #%d: ", tc);
        if (cnt == 0)
            printf("Volunteer cheated!\n");
        else if (cnt == 1)
            printf("%d\n", ans);
        else
            printf("Bad magician!\n");
    }
}

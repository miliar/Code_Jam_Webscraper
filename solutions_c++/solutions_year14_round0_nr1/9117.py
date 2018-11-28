#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <cstdio>

using namespace std;

int main() {
    int t, t1 = 1;
    int p1, p2;
    int a[4][4];
    int b[4][4];
    cin >> t;
    while(t--) {
        cin >> p1;
        for(int i = 0; i < 4; ++i) {
            for(int j = 0; j < 4; ++j) {
                cin >> a[i][j];
            }
        }
        cin >> p2;
        for(int i = 0; i < 4; ++i) {
            for(int j = 0; j < 4; ++j) {
                cin >> b[i][j];
            }
        }
        p1--; p2--;
        int s1 = 0, ans = -1;
        for(int i = 0; i < 4; ++i) {
            for(int j = 0; j < 4; ++j) {
                if (a[p1][i] == b[p2][j]) {
                    s1++;
                    ans = a[p1][i];
                }
            }
        }
        if (s1 == 0) {
            printf("Case #%d: Volunteer cheated!\n", t1++);
        } else if (s1 > 1) {
            printf("Case #%d: Bad magician!\n", t1++);
        } else {
            printf("Case #%d: %d\n", t1++, ans);
        }

    }
    return 0;
}

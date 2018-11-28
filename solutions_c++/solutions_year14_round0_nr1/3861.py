#include<iostream>
#include<vector>
#include<math.h>
using namespace std;

int main() {
    int cases;
    cin >> cases;
    for (int c = 1; c <= cases; c++) {
        int r1, r2;
        cin >> r1;
        r1--;
        vector<vector<int> > b1(4, vector<int>(4, 0));
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                cin >> b1[i][j];
            }
        }

        cin >> r2;
        r2--;
        vector<vector<int> > b2(4, vector<int>(4, 0));
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                cin >> b2[i][j];
            }
        }

        int matchCount = 0;
        int matchedCard = -1;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                if (b1[r1][i] == b2[r2][j]) {
                    matchCount++;
                    matchedCard = b1[r1][i];
                    break;
                }
            }
        }
        if (matchCount > 1) {
            printf("Case #%d: Bad magician!\n", c);
        } else if (matchCount == 1) {
            printf("Case #%d: %d\n", c, matchedCard);
        } else {
            printf("Case #%d: Volunteer cheated!\n", c);
        }
    }
}

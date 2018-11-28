#include <iostream>
#include <cstdlib>
#include <cstdio>

using namespace std;

void solve(int testCaseNumber) {
    int number, cnt = 0, answ;
    bool possible[32] = { 0 };

    int firstRow;
    scanf("%d", &firstRow);
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
                scanf("%d", &number);
                if (i + 1 == firstRow) {
                    possible[number] = true;
                }
        }
    }

    int secondRow;
    scanf("%d", &secondRow);
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            scanf("%d", &number);
            if (i + 1 == secondRow && possible[number]) {
                cnt++;
                answ = number;
            }

        }
    }

    if (cnt == 0) {
        printf("Case #%d: Volunteer cheated!\n", testCaseNumber);
    } else if (cnt == 1) {
        printf("Case #%d: %d\n", testCaseNumber, answ);
    } else {
        printf("Case #%d: Bad magician!\n", testCaseNumber);
    }
}

int main() {
    int tests;
    scanf("%d", &tests);
    for (int i = 1; i <= tests; ++i) {
        solve(i);
    }

    return 0;
}

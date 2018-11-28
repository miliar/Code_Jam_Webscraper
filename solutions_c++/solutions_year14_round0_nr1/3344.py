#include <iostream>
#include <vector>

using namespace std;

const char* input = "input.in";
const char* output = "output.out";

//#define LOG(string, ...) printf(string, __VA_ARGS__)
#define LOG(string, ...)

int getMatchNumber(int grid[], int number) {
    for (int i=0; i < 4; ++i) {
        //LOG("Grid %d: %d\n", i, grid[i]);
        if (number == grid[i]) {
            return i;
        }
    }
    return -1;
}

int main()
{
    freopen(input, "r", stdin);
    freopen(output, "w", stdout);

    int tc;
    cin >> tc;
    LOG("N testcases = %d\n\n", tc);

    for (int test=1; test <= tc; ++test) {
        int firstAnswer, secondAnswer;
        int firstGrid[4][4];
        int secondGrid[4][4];
        vector<int> solution[4];

        LOG("Test %d\n", test);

        cin >> firstAnswer;
        LOG("First answer: %d\n", firstAnswer);
        firstAnswer--;

        for (int i=0; i < 4; ++i) {
            scanf("\n%d %d %d %d", &firstGrid[i][0], &firstGrid[i][1], &firstGrid[i][2], &firstGrid[i][3]);
            LOG("Grid %d: %d %d %d %d\n", i, firstGrid[i][0], firstGrid[i][1], firstGrid[i][2], firstGrid[i][3]);
        }

        cin >> secondAnswer;
        LOG("\nSecond answer: %d\n", secondAnswer);
        secondAnswer--;

        for (int i=0; i < 4; ++i) {
            scanf("\n%d %d %d %d", &secondGrid[i][0], &secondGrid[i][1], &secondGrid[i][2], &secondGrid[i][3]);
            LOG("Grid %d: %d %d %d %d\n", i, secondGrid[i][0], secondGrid[i][1], secondGrid[i][2], secondGrid[i][3]);

            for (int j=0; j < 4; ++j) {
                int match;
                if ((match = getMatchNumber(&firstGrid[firstAnswer][0], secondGrid[i][j])) != -1) {
                    solution[i].push_back(secondGrid[i][j]);
                    LOG("Number %d,%d=%d of first grid matches number %d,%d=%d of second grid\n",
                        firstAnswer, match, firstGrid[firstAnswer][match], i, j, secondGrid[i][j]);
                }
            }
        }

        if (solution[secondAnswer].empty()) {
            printf("Case #%d: %s\n", test, "Volunteer cheated!");
        } else if (solution[secondAnswer].size() > 1) {
            printf("Case #%d: %s\n", test, "Bad magician!");
        } else {
            printf("Case #%d: %d\n", test, solution[secondAnswer].front());
        }
    }

    return 0;
}


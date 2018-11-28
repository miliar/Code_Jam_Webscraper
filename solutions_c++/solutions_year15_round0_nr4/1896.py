#include <cstdio>
#include <cstring>

// countTestCases should be less or equal to 100
int countTestCases = 0;

inline int Max(int row, int col) {
    return row > col ? row : col;
}

inline int Min(int row, int col) {
    return row < col ? row : col;
}

void solve(int caseNum, int x, int row, int col) {

    // if the (row * col) can not be divided by x,
    // it's impossible to be full-filled by x-omino
    if (((row * col) % x) != 0) {
        printf("Case #%d: RICHARD\n", caseNum + 1);
        return;
    }

    // if x is larger than Max(row, col)
    // Richard can specify a x-omino which is x by 1 that can't be filled into it
    if (x > Max(row, col)) {
        printf("Case #%d: RICHARD\n", caseNum + 1);
        return;
    }

    // Richard can specify a special omino such as :
    // OOO
    // O O
    // OO
    // Ans Gabriel has no way to fill the center cell
    if (x >= 7) {
        printf("Case #%d: RICHARD\n", caseNum + 1);
        return;
    }

    // Richard can make a corner which can't be covered
    //  O
    // OO
    //  O
    if (x >= 4 && Min(row, col) <= 2) {
        printf("Case #%d: RICHARD\n", caseNum + 1);
        return;
    }

    // try to transform x-omino into different shapes
    // e.x. 4-omino can be transformed into L-shaped omino, such as 1-4, 2-3 shapes
    //      Richard wins if there is one shape which shorter side is larger than Min(row, col).
    int cells = 1;
    int cellsAnotherSide = x;
    const int minCells = Min(row, col);

    for (int i = 0; cellsAnotherSide >= cells; ++i) {

        if (Min(cells, cellsAnotherSide) > minCells) {
            printf("Case #%d: RICHARD\n", caseNum + 1);
            return;
        }

        ++cells;
        --cellsAnotherSide;
    }

    printf("Case #%d: GABRIEL\n", caseNum + 1);
}


int main() {

    scanf("%d", &countTestCases);

    int i = 0;

    for ( ; i < countTestCases; ++i) {
        int x = 0;
        int row = 0;
        int col = 0;

        scanf("%d %d %d", &x, &row, &col);

        solve(i, x, row, col);
    }

    return 0;
}

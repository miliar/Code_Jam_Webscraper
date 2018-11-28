#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

void solveCase() {
    //read size
    int rows, cols;
    cin >> rows >> cols;

    //read grid
    int size = rows * cols;
    vector<int> grid(size);

    for(int i = 0; i < size; i++) {
        int h;
        cin >> h;
        grid[i] = h;
    }

    //build max arrays
    vector<int> rowMaxs(rows);
    vector<int> colMaxs(cols);

    for(int i = 0; i < rows; i++) {
        for(int j = 0; j < cols; j++) {
            int h = grid[i * cols + j];
            if(h > rowMaxs[i]) rowMaxs[i] = h;
            if(h > colMaxs[j]) colMaxs[j] = h;
        }
    }

    //check grid
    bool ok = true;

    for(int i = 0; i < rows && ok; i++) {
        for(int j = 0; j < cols && ok; j++) {
            int h = grid[i * cols + j];
            if(h < rowMaxs[i] && h < colMaxs[j]) ok = false;
        }
    }

    //output result
    cout << (ok ? "YES" : "NO") << endl;
}

int main() {
    int caseCount;
    cin >> caseCount;

    for(int i = 1; i <= caseCount; i++) {
        printf("Case #%d: ", i);
        solveCase();
    }

    return 0;
}

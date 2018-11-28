#include <iostream>
#include <algorithm>
using namespace std;

struct GridCell {
    bool canVertical, canHorizontal;
    int value;
} grid[100][100];

int N, M, maxA;

bool checkGridPos(int i, int j) {
    int height = grid[i][j].value;
    grid[i][j].canVertical = true;
    grid[i][j].canHorizontal = true;
    
    //check horizontal
    int row = i, column;
    
    for (column = 0; column < M; column++) {
        if ((grid[row][column].value < height && !grid[row][column].canVertical) ||
             grid[row][column].value > height) {
            grid[i][j].canHorizontal = false;
            break;
        }
    }
    
    //check vertical
    column = j;
    
    for (row = 0; row < N; row++) {
        if ((grid[row][column].value < height && ! grid[row][column].canHorizontal) ||
            grid[row][column].value > height) {
            grid[i][j].canVertical = false;
            break;
        }
    }
    
    //cout << "I: " << i << " J: " << j << " " << grid[i][j].canVertical << " " << grid[i][j].canHorizontal << endl;
    
    return grid[i][j].canHorizontal || grid[i][j].canVertical;
}

bool solve()
{
    for (int height = 1; height <= maxA; height++) {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (grid[i][j].value == height && ! checkGridPos(i, j)) {
                    return false;
                }
            }   
        }
    }
    return true;
}

int main()
{
    int T, case_ = 0;
    cin >> T;
    
    while (T--) {
        ++case_;
        maxA = 0;
        cin >> N >> M;
    
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                cin >> grid[i][j].value;
                maxA = max(maxA, grid[i][j].value);
            }
        }
        
        cout << "Case #" << case_ << ": " << (solve()? "YES" : "NO") << endl; 
    }

    return 0;
}

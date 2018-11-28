#include <algorithm>
#include <iostream>

using namespace std;

void readInput(int& answer, int* grid)
{
    cin >> answer;
    answer--;
    
    for(int i = 0; i < 16; i++)
    {
        cin >> grid[i];
    }
}

void solveCase()
{
    //read input
    int answer1, grid1[16];
    int answer2, grid2[16];
    
    readInput(answer1, grid1);
    readInput(answer2, grid2);
    
    int* row1 = grid1 + answer1 * 4;
    int* row2 = grid2 + answer2 * 4;

    //compare rows
    sort(row1, row1 + 4);
    sort(row2, row2 + 4);
    
    int inter[4];
    int* end = set_intersection(row1, row1 + 4, row2, row2 + 4, inter);
    int count = end - inter;
    
    //output result
    if(count == 1)      cout << inter[0];
    else if(count == 0) cout << "Volunteer cheated!";
    else                cout << "Bad magician!";
}

int main()
{
    int caseCount;
    cin >> caseCount;

    for(int i = 1; i <= caseCount; i++)
    {
        cout << "Case #" << i << ": ";
        solveCase();
        cout << endl;
    }

    return 0;
}

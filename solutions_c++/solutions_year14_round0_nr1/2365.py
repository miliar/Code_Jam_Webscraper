#include <iostream>

using namespace std;

int main()
{
    int t;
    cin >> t;
    
    for(int testCase = 1; testCase <= t; ++testCase)
    {
        // Input
        int answer1, answer2;
        int grid1[4][4];
        int grid2[4][4];
        int choice;
        int count = 0;
        
        cin >> answer1;
        --answer1;
        
        for(int i = 0; i < 4; ++i)
        {
            for(int j = 0; j < 4; ++j)
            {
                cin >> grid1[i][j];
            }
        }
        
        cin >> answer2;
        --answer2;
        
        for(int i = 0; i < 4; ++i)
        {
            for(int j = 0; j < 4; ++j)
            {
                cin >> grid2[i][j];
            }
        }
        
        // Solve
        for(int i = 0; i < 4; ++i)
        {
            for(int j = 0; j < 4; ++j)
            {
                if(grid1[answer1][i] == grid2[answer2][j])
                {
                    choice = grid1[answer1][i];
                    ++count;
                }
            }
        }
        
        // Output
        cout << "Case #" << testCase << ": ";
        if(count == 1)
        {
            cout << choice;
        }
        else
        {
            cout << (count == 0 ? "Volunteer cheated!" : "Bad magician!");
        }
        cout << endl;
    }
    
    return 0;
}

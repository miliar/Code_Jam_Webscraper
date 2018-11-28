#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void solve()
{
    int cases, current, row1, row2;
    int poss1, poss2, poss3, poss4;
    int ans;
    int board[4][4];
    current = 1;
    cin >> cases;
    for(int x = 0; x<cases; x++)
    {
        ans =-1;
        cin >> row1;
        for(int y = 0; y<4; y++)
        {
            for(int z = 0; z<4; z++)
            {
                cin >> board[y][z];
            }                  
        }
        poss1 = board[row1-1][0];
        poss2 = board[row1-1][1];
        poss3 = board[row1-1][2];
        poss4 = board[row1-1][3];
        cin >> row2;        
        for(int y = 0; y<4; y++)
        {
            for(int z = 0; z<4; z++)
            {
                cin >> board[y][z];
            }                  
        }
        
        for(int y = 0; y<4; y++)
        {
            if(ans == -1)
            {
                if(board[row2-1][y] == poss1) ans = poss1;
                if(board[row2-1][y] == poss2) ans = poss2;
                if(board[row2-1][y] == poss3) ans = poss3;
                if(board[row2-1][y] == poss4) ans = poss4;
            }
            else
            {
                if(board[row2-1][y] == poss1 ||
                   board[row2-1][y] == poss2 ||
                   board[row2-1][y] == poss3 ||
                   board[row2-1][y] == poss4) 
                   {
                       ans = -2;
                   }             
            }             
        }
        
        if(ans == -1)
        {
            cout << "Case #" << current << ": Volunteer cheated!" << endl;
        }
        else if(ans == -2)
        {
            cout << "Case #" << current << ": Bad magician!" << endl;
        }
        else
        {
            cout << "Case #" << current << ": " << ans << endl;
        }
        
        current++;
    }
    
}

int main()
{
    solve();
    return 0;
}

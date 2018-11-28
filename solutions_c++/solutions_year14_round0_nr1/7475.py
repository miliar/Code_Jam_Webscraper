#include <iostream>
using namespace std;

int main()
{
    int cases;
    cin >> cases;
    
    int grid1[4][4];
    int grid2[4][4];
    int answer1, answer2;
    
    for(int i = 0; i < cases; i++)
    {
        cin >> answer1;
        
        // Occupy grid 1
        for(int j = 0; j < 4; j++)
        {
            for(int k = 0; k < 4; k++)
            {
                cin >> grid1[j][k];
            }
        }
        
        cin >> answer2;
        
        // Occupy grid 2
        for(int j = 0; j < 4; j++)
        {
            for(int k = 0; k < 4; k++)
            {
                cin >> grid2[j][k];
            }
        }
        
        // Find a card that is in both rows
        int cardcount = 0;
        int card;
        for(int j = 0; j < 4; j++)
        {
            for(int k = 0; k < 4; k++)
            {
                if(grid1[answer1 - 1][j] == grid2[answer2 - 1][k])
                {
                    cardcount++;
                    card = grid1[answer1 - 1][j];
                }
            }
        }
        
        if(cardcount == 1)
        {
            cout << "Case #" << i + 1 << ": " << card << endl;
        }
        else if(cardcount > 1)
        {
            cout << "Case #" << i + 1 << ": " << "Bad magician!" << endl;
        }
        else
        {
            cout << "Case #" << i + 1 << ": " << "Volunteer cheated!" << endl;
        }
    }
    
    
    return 0;
}
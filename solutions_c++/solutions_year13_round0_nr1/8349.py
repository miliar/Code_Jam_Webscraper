#include <iostream>
#include <vector>

using namespace std;

#define pb push_back
int main() 
{
    int T;
    cin >> T;

    for (int i = 0; i < T; i++) 
    {
        string board[4];
        vector<string> pos;

        for (int j = 0; j < 4; j++)
        {
            cin >> board[j];
            pos.pb(board[j]);
        }

        string xWin[2] = {"XXXX", "XXXT"},
               yWin[2] = {"OOOO", "OOOT"};

        bool isdraw = true;

        string diag1 = "", diag2 = "";
        for (int j = 0; j < 4; j++) 
        {
            string temp = "";
            for (int k = 0; k < 4; k++)
            {
                if (board[j][k] == '.' && isdraw)
                    isdraw = false;
                if (k == j) 
                    diag1 += board[j][k];
                if (k == 4-j-1)
                    diag2 += board[j][k];
                temp += board[k][j];
            }
            pos.pb(temp);
        }

        pos.pb(diag1);
        pos.pb(diag2);

        bool X = false, Y = false;
        for (int j = 0; j < pos.size(); j++)
        {
            if (pos[j] == xWin[0] || pos[j] == xWin[1])
            {    
                X = true;
                break;
            }
            else if (pos[j] == yWin[0] || pos[j] == yWin[1])
            {
                Y = true;
                break;
            }
        }

        cout << "Case #" << i+1 << ": ";
        if (X) 
            cout << "X won" << endl;
        else if (Y) 
            cout << "O won" << endl;
        else if (isdraw)
            cout << "Draw" << endl;
        else
            cout << "Game has not completed" << endl;
    }
    
    return 0;
}

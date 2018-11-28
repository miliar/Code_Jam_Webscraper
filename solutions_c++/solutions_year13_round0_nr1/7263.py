#include <iostream>
#include <string>
using namespace std;

string check(string board[4])
{
    int sum1;
    int sum2;

    sum1 = (int)board[0][0] + (int)board[1][1] + (int)board[2][2] + (int)board[3][3];
    sum2 = (int)board[0][3] + (int)board[1][2] + (int)board[2][1] + (int)board[3][0];

    if (sum1 == 352 || sum1 == 348 || sum2 == 352 || sum2 == 348)
        return "X won";

    if (sum1 == 316 || sum1 == 321 || sum2 == 316 || sum2 == 321)
        return "O won";

    for (int i = 0; i < 4; i++)
    {
        sum1 = 0;
        sum2 = 0;
        for (int j = 0; j < 4; j++)
        {
            sum1 += (int)board[i][j];
            sum2 += (int)board[j][i];

            if (sum1 == 352 || sum1 == 348 || sum2 == 352 || sum2 == 348)
                return "X won";
            if (sum1 == 316 || sum1 == 321 || sum2 == 316 || sum2 == 321)
                return "O won";
        }
    }

    for (int i = 0; i < 4; i++)
        if (board[i].find('.') != string::npos)
            return "Game has not completed";

    return "Draw";
}

int main()
{
    int cases;
    string board[4];

    cin >> cases;

    for (int i = 0; i < cases; i++)
    {
        cin >> board[0] >> board[1] >> board[2] >> board[3];
        cout << "Case #" << i + 1 << ": " << check(board) << endl;
    }
    
    return 0;
}

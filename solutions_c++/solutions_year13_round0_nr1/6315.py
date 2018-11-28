#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
    int numGames;
    cin >> numGames;

    for(int game = 0; game < numGames; ++game)
    {
        const int BOARD_SIZE = 4;
        vector<string> board(4);

        // We need to read in all lines even if we know the game is incomplete
        bool complete = true;
        for(int i = 0; i < BOARD_SIZE; ++i)
        {
            cin >> board[i];
            if (string::npos != board[i].find('.')) {
                complete = false;
            }
        }

        // check horizontal
        char winner = '.';
        for(int i = 0; i < BOARD_SIZE; ++i)
        {
            string& line = board[i];

            if (line[0] == '.' || line[1] == '.') {
                continue;
            }

            char firstChar = line[0];
            if (firstChar == 'T') {
                firstChar = line[1];
            }

            bool homo = true;
            for (int j = 1; j < BOARD_SIZE; ++j)
            {

                if (line[j] != firstChar && line[j] != 'T') {
                    homo = false;
                    break;
                }
            }

            if (homo) {
                winner = firstChar;
            }
        }

        if (winner != '.') {
            cout << "Case #" << game+1
                 << ": " << winner << " won"
                 << endl;
            continue;
        }

        // check vertical
        for(int i = 0; i < BOARD_SIZE; ++i)
        {
            if (board[0][i] == '.' || board[1][i] == '.') {
                continue;
            }

            char firstChar = board[0][i];
            if (firstChar == 'T') {
                firstChar = board[1][i];
            }

            bool homo = true;
            for (int j = 1; j < BOARD_SIZE; ++j)
            {

                if (board[j][i] != firstChar && board[j][i] != 'T') {
                    homo = false;
                    break;
                }
            }

            if (homo) {
                winner = firstChar;
            }
        }

        if (winner != '.') {
            cout << "Case #" << game+1
                 << ": " << winner << " won"
                 << endl;
            continue;
        }

        // check good and easy diagonal
        char firstChar = board[0][0];
        if (firstChar == 'T') {
            firstChar = board[1][1];
        }

        bool homo = true;
        for(int i = 1; i < BOARD_SIZE; ++i) {
            if (board[i][i] != firstChar && board[i][i] != 'T') {
                homo = false;
                break;
            }
        }

        if (homo && firstChar != '.') {
            cout << "Case #" << game+1
                 << ": " << firstChar << " won"
                 << endl;
            continue;
        }

        // check bad and hard diagonal
        firstChar = board[0][BOARD_SIZE-1];
        if (firstChar == 'T') {
            firstChar = board[1][BOARD_SIZE-2];
        }

        homo = true;
        for(int i = 1; i < BOARD_SIZE; ++i) {
            if (board[i][BOARD_SIZE-i-1] != firstChar
             && board[i][BOARD_SIZE-i-1] != 'T')
            {
                homo = false;
                break;
            }
        }

        if (homo && firstChar != '.') {
            cout << "Case #" << game+1
                 << ": " << firstChar << " won"
                 << endl;
            continue;
        }

        if (!complete) {
            cout << "Case #" << game+1
                 << ": Game has not completed"
                 << endl;
            continue;
        }

        cout << "Case #" << game+1
             << ": Draw"
             << endl;
    }
}

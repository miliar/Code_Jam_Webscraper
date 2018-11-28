#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

void determineWinner(const vector<vector<char> >& board, int testNum) {
    // check each row
    int x_count, o_count, t_count, dot_count;
    dot_count = 0;
    for(int i = 0; i < 4; i++) {
        x_count = o_count = t_count = 0;
        for(int j = 0; j < 4; j++) {
            if( board[i][j] == 'X' )
                x_count++;
            else if(board[i][j] == 'O' )
                o_count++;
            else if(board[i][j] == 'T' )
                t_count++;
            else
                dot_count++;
        }

        if(x_count == 4 || x_count ==3 && t_count == 1) {
            cout << "Case #" << testNum << ": X won" << endl;
            return;
        }
        else if(o_count == 4 || o_count == 3 && t_count == 1) {
            cout << "Case #" << testNum << ": O won" << endl;
            return;
        }
    }

    // check each column
    for(int j = 0; j < 4; j++) {
        x_count = o_count = t_count = 0;
        for(int i = 0; i < 4; i++) {
            if( board[i][j] == 'X' )
                x_count++;
            else if(board[i][j] == 'O' )
                o_count++;
            else if(board[i][j] == 'T' )
                t_count++;
            else
                dot_count++;
        }

        if(x_count == 4 || x_count ==3 && t_count == 1) {
            cout << "Case #" << testNum << ": X won" << endl;
            return;
        }
        else if(o_count == 4 || o_count == 3 && t_count == 1) {
            cout << "Case #" << testNum << ": O won" << endl;
            return;
        }
    }

    // check diagonal
    x_count = o_count = t_count = 0;
    for(int i = 0; i < 4; i++) {
        if( board[i][i] == 'X' )
            x_count++;
        else if(board[i][i] == 'O' )
            o_count++;
        else if(board[i][i] == 'T' )
            t_count++;
        else
            dot_count++;

        if(x_count == 4 || x_count ==3 && t_count == 1) {
            cout << "Case #" << testNum << ": X won" << endl;
            return;
        }
        else if(o_count == 4 || o_count == 3 && t_count == 1) {
            cout << "Case #" << testNum << ": O won" << endl;
            return;
        }
    }

    x_count = o_count = t_count = 0;
    for(int i = 0; i < 4; i++) {
        if( board[i][3-i] == 'X' )
            x_count++;
        else if(board[i][3-i] == 'O' )
            o_count++;
        else if(board[i][3-i] == 'T' )
            t_count++;
        else
            dot_count++;

        if(x_count == 4 || x_count ==3 && t_count == 1) {
            cout << "Case #" << testNum << ": X won" << endl;
            return;
        }
        else if(o_count == 4 || o_count == 3 && t_count == 1) {
            cout << "Case #" << testNum << ": O won" << endl;
            return;
        }
    }

    if( dot_count == 0 )
        cout << "Case #" << testNum << ": Draw" << endl;
    else
        cout << "Case #" << testNum << ": Game has not completed" << endl;

}

int main()
{
    ifstream input("A-large.in");
    cin.rdbuf(input.rdbuf());


    ofstream output("A-large.out");
    cout.rdbuf(output.rdbuf());

    int T;

    cin >> T;

    for(int i = 0; i < T; i++) {
        vector<vector<char> > board;
        board.resize(4);

        for(int j = 0; j < 4; j++) {
            for(int k = 0; k < 4; k++) {
                char c;
                cin >> c;
                board[j].push_back(c);
            }
        }

        determineWinner(board, i+1);

    }

    input.close();
    output.close();

    return 0;
}

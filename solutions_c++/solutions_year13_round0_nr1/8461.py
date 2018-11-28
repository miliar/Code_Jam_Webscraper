#include <cstdio>
#include <iostream>

using namespace std;

const char PLAYER1 = 'X';
const char PLAYER2 = 'O';
const char EMPTY = '.';

int BOARD_WIDTH = 4;
int BOARD_SIZE = 16;

int moveCount = 0;
int movePos;
bool player = true;

int askForMove(char board[], char turn);
bool makeMove(char board[], char turn, int move);
bool isWinner(char board[], char turn, int arraySize);
bool isTie();
bool checkForWin(char board[], char turn, int spaceCount, int iStart, int iEnd);

int main(void)
{
    freopen("A-small-attempt0.in", "r", stdin);
    int T, N, cases=0, i=0;
    bool first = true;
    char userInput;
    cin >> T;
    while(T--) {
        moveCount = 0;

        char board[BOARD_SIZE];
        bool userTurn = false;

        if(first) first = false;
        else cout << endl;

        for (int i = 0; i < BOARD_SIZE; i++) {
              cin >> userInput;
              board[i] = userInput;
              if(userInput != EMPTY) moveCount += 1;
              if(userInput == 'T') {
                  movePos = i;
                  userTurn = true;
              }
        }

        bool win = false;

        while (win == false)
        {
            if(userTurn==true && player==true) {
                askForMove(board, PLAYER1);
                player = false;
                userTurn = false;
            }

            if(userTurn==true && player==false) {
                askForMove(board, PLAYER2);
                player = true;
                userTurn = false;
            }

            win = false;
            win = isWinner(board, PLAYER1, BOARD_SIZE);
            if (win == true)
            {
                cout << "Case #" << ++cases <<": X won" << endl;
                break;
            }

            if (isTie())
            {
                cout << "Case #" << ++cases <<": Draw" << endl;
                break;
            }

            win = false;
            win = isWinner(board, PLAYER2, BOARD_SIZE);
            if (win == true)
            {
                cout << "Case #" << ++cases <<": O won" << endl;
                break;
            }

            if (isTie())
            {
                cout << "Case #" << ++cases <<": Draw" << endl;
                break;
            }

            cout << "Case #" << ++cases <<": Game has not completed" << endl;
            break;
        }
    }
    return(0);
}

int askForMove(char board[], char turn)
{
    int userInput;

    userInput = movePos;

    while (true)
    {
        bool validMove = makeMove(board, turn, userInput);
        if (validMove == false)
        {

        }
        else
            break;
    }

    return userInput;
}

bool makeMove(char board[], char turn, int move)
{
    if (move < 0 || move > BOARD_SIZE - 1)
    {
        return false;
    }

    if (board[move] == 'T')
    {
        board[move] = turn;
        return true;
    }
    else
    {
        return false;
    }
}

bool isWinner(char board[], char turn, int arraySize)
{
    for (int i = 0; i < BOARD_SIZE; i += BOARD_WIDTH)
    {
        if (checkForWin(board, turn, 1, i, i + BOARD_WIDTH) == true)
        {
            return true;
        }
    }

    int diagRight = 2 + (BOARD_WIDTH - 3);
    if (checkForWin(board, turn, diagRight, (BOARD_WIDTH - 1), (diagRight * BOARD_WIDTH) + 1) == true)
    {
        return true;
    }

    for (int i = 0; i < BOARD_WIDTH; i++)
    {
        if (checkForWin(board, turn, 3 + (BOARD_WIDTH - 3), i, ((BOARD_WIDTH * 2) + i + 4) + 1) == true)
        {
            return true;
        }
    }

    if (checkForWin(board, turn, 4 + (BOARD_WIDTH - 3), 0, BOARD_SIZE) == true)
    {
       return true;
    }

    return false;
}

bool isTie()
{
    if (moveCount >= BOARD_SIZE)
        return true;

    return false;
}

bool checkForWin(char board[], char turn, int spaceCount, int iStart, int iEnd)
{
    int tileCount = 0;

    for (int i = iStart; i < iEnd; i += spaceCount)
    {
        if (board[i] == turn)
        {
            tileCount += 1;
        }

        if (tileCount == BOARD_WIDTH)
        {
            return true;
        }
    }

    return false;
}

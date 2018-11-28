#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

bool checkLine(const vector<char>& line, char chess) {
    for (int i = 0; i < line.size(); ++i)
        if (line[i] != chess && line[i] != 'T')
            return false;
    return true;
}

bool checkColumn(const vector<vector<char>>& board, int col, char chess) {
    for (int i = 0; i < board.size(); ++i)
        if (board[i][col] != chess && board[i][col] != 'T')
            return false;
    return true;
}

bool checkDiagonal(const vector<vector<char>>& board, char chess) {
    for (int i = 0; i < board.size(); ++i)
        if (board[i][i] != chess && board[i][i] != 'T')
            return false;
    return true;
}

bool checkDiagonal2(const vector<vector<char>>& board, char chess) {
    int n = board.size();
    for (int i = 0; i < board.size(); ++i)
        if (board[i][n-i-1] != chess && board[i][n-i-1] != 'T')
            return false;
    return true;
}

bool judge(const vector<vector<char>>& board, char chess) {
    for (int i = 0; i < board.size(); ++i)
        if (checkLine(board[i], chess))
            return true;
    for (int j = 0; j < board[0].size(); ++j)
        if (checkColumn(board, j, chess))
            return true;
    if (checkDiagonal(board, chess) || checkDiagonal2(board, chess))
        return true;
    return false;
}

bool checkEmpty(const vector<vector<char>>& board) {
    for (int i = 0; i < board.size(); ++i)
        for (int j = 0; j < board[0].size(); ++j)
            if (board[i][j] == '.')
                return true;
    return false;
}

int main()
{
    int T;
    scanf("%d", &T);
    for (int z = 1; z <= T; ++z) {
        vector<vector<char>> board(4, vector<char>(4));
        for (int i = 0; i < 4; ++i)
            for (int j = 0; j < 4; ++j)
                scanf(" %c", &board[i][j]);
        if (judge(board, 'X'))
            printf("Case #%d: X won\n", z);
        else if (judge(board, 'O'))
            printf("Case #%d: O won\n", z);
        else if (checkEmpty(board))
            printf("Case #%d: Game has not completed\n", z);
        else
            printf("Case #%d: Draw\n", z);

    }
    return 0;
}

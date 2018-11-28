#include <cstdio>
#include <cstdlib>
#include <string>

using namespace std;

enum Status {Incomplete, Draw, O,X};

class board
{
    Status _status;

    Status check(string line) {
        Status s = Draw;
        for (size_t i=0; i<4; i++) {
            if (line[i] == '.')
                return Incomplete;
            else if (line[i] == 'X' && s == O)
                return Draw;
            else if (line[i] == 'O' && s == X)
                return Draw;
            else if (line[i] == 'X')
                s = X;
            else if (line[i] == 'O')
                s = O;
        }
        return s;
    }

    Status merge(Status s1, Status s2)
    {
        if (s1 == X || s2 == X)
            return X;
        else if (s1 == O || s2 == O)
            return O;
        else if (s1 == Incomplete || s2 == Incomplete)
            return Incomplete;
        return Draw;
    }
public:
    board() {
        char board[4][5];
        scanf("%4s %4s %4s %4s", board[0], board[1], board[2], board[3]);

        _status = Draw;

        char line[5] = "....";
        for (size_t row = 0; row<4; row++) {
            line[0] = board[row][0];
            line[1] = board[row][1];
            line[2] = board[row][2];
            line[3] = board[row][3];
            _status = merge(check(line), _status);
        }
        for (size_t col = 0; col<4; col++) {
            line[0] = board[0][col];
            line[1] = board[1][col];
            line[2] = board[2][col];
            line[3] = board[3][col];
            _status = merge(check(line), _status);
        }
        line[0] = board[0][0];
        line[1] = board[1][1];
        line[2] = board[2][2];
        line[3] = board[3][3];
        _status = merge(check(line), _status);

        line[0] = board[0][3];
        line[1] = board[1][2];
        line[2] = board[2][1];
        line[3] = board[3][0];
        _status = merge(check(line), _status);
    }

    const char *status() const {
        switch (_status) {
            case Incomplete:
                return "Game has not completed";
            case Draw:
                return "Draw";
            case O:
                return "O won";
            case X:
                return "X won";
        }
    }
};

int main()
{
    unsigned int T;
    scanf("%u", &T);
    for (size_t caseNo=1; caseNo<=T; caseNo++) {
        board b;
        printf("Case #%u: %s\n", caseNo, b.status());
    }
    return 0;
}

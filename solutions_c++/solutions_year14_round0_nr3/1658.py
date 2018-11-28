#include <iostream>
#include <list>
#include <algorithm>

using namespace std;

class Board
{
public:
    Board(int r, int c) : r(r), c(c)
    {
        data = new char[r*c];
        for(int i=0; i<r*c; i++)
        {
            data[i] = '*';
        }
    }

    Board(const Board &other) : r(other.r), c(other.c)
    {
        data = new char[r*c];
        for(int i=0; i<r*c; i++)
            data[i] = other.data[i];
    }

    ~Board()
    {
        delete[] data;
    }

    int numbombs()
    {
        int result=0;
        for(int i=0; i<r*c; i++)
        {
            if(data[i] == '*')
                result++;
        }
        return result;
    }

    void setStart(int i, int j)
    {
        data[i*c+j] = 'c';
    }

    bool isBoundary(int i, int j)
    {
        if(data[i*c+j] == '*')
            return false;

        for(int row = max(0, i-1); row <= min(r-1, i+1); row++)
        {
            for(int col = max(0, j-1); col <= min(c-1, j+1); col++)
            {
                if(data[row*c+col] == '*')
                    return true;
            }
        }
        return false;
    }

    void clear(int i, int j)
    {
        for(int row = max(0, i-1); row <= min(r-1, i+1); row++)
        {
            for(int col = max(0, j-1); col <= min(c-1, j+1); col++)
            {
                if(data[row*c+col] == '*')
                    data[row*c+col] = '.';
            }
        }
    }

    void print()
    {
        for(int i=0; i<r; i++)
        {
            for(int j=0; j<c; j++)
            {
                cout << data[i*c+j];
            }
            cout << endl;
        }
    }

    int rows()
    {
        return r;
    }

    int cols()
    {
        return c;
    }

private:
    int r, c;
    char *data;
};

bool solveBoard(Board &board, int mines)
{
    int minesremaining = board.numbombs();
    if(minesremaining < mines)
        return false;
    else if(minesremaining == mines)
    {
        board.print();
        return true;
    }

    for(int i=0; i<board.rows(); i++)
    {
        for(int j=0; j<board.cols(); j++)
        {
            if(board.isBoundary(i,j))
            {
                Board next(board);
                next.clear(i,j);
                if(solveBoard(next, mines))
                {
                    return true;
                }
            }
        }
    }

    return false;
}

void testCase()
{
    cout << endl;
    int r, c, m;
    cin >> r >> c >> m;

    Board board(r,c);
    for(int i=0; i<r; i++)
    {
        for(int j=0; j<c; j++)
        {
            Board attempt(board);
            attempt.setStart(i, j);
            if(solveBoard(attempt, m))
            {
                return;
            }
        }
    }

    cout << "Impossible" << endl;
}

int main()
{
    int t;
    cin >> t;
    for(int i=0; i<t; i++)
    {
        cout << "Case #" << i+1 << ":";
        testCase();
    }
}



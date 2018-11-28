#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <iomanip>
using namespace std;
const double INF = 1e12;

char board[55][55];

void printBoard(int R, int C)
{
    for(int i = 0; i < R; ++i)
    {
        for(int j = 0; j < C; ++j)
            cout<<board[i][j];
        cout<<endl;
    }
}

int main()
{
    int T;
    int R, C, M;
    cin>>T;
    
    for(int tt = 1; tt <= T; ++tt)
    {
        cin>>R>>C>>M;
        memset(board, '*', sizeof(board));

        cout<<"Case #"<<tt<<": "<<endl;
        int blank = R * C - M;

        if(R == 1 || C == 1 || blank == 1)
        {
            for(int i = 0; i < R && blank; ++i)
            {
                for(int j = 0; j < C && blank; ++j, --blank)
                {
                    board[i][j] = '.';
                }
            }
            board[0][0] = 'c';
            printBoard(R, C);
        }
        else if(blank > 2)
        {

        }
        else 
        {
            cout<<"Impossible"<<endl;
        }
    }

    return 0;
}

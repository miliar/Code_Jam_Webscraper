#include <iostream>
#define MAX_SIZE 200

using namespace std;

int board[MAX_SIZE][MAX_SIZE];
int M, N;

bool theresAWayOut(int p, int q)
{
    int i, j;

    for(i=q-1; i >= 0; --i)
        if(board[p][i] > board[p][q])
            break;
    if(i < 0)
    {
        for(i=q+1; i < N; ++i)
            if(board[p][i] > board[p][q])
                break;
        if(i == N)
            return true;
    }

    for(i=p-1; i >= 0; --i)
        if(board[i][q] > board[p][q])
            break;
    if(i < 0)
    {
        for(i=p+1; i < M; ++i)
            if(board[i][q] > board[p][q])
                break;
        if(i == M)
            return true;
    }

    return false;
}

int main()
{
    int T;
    int i, j, k;

    cin >> T;
    for(i=1; i <= T; ++i)
    {
        cin >> M >> N;
        for(j=0; j < M; ++j)
        {
            for(k=0; k < N; ++k)
            {
                cin >> board[j][k];
            }
        }

        for(j=0; j < M; ++j)
        {
            for(k=0; k < N; ++k)
            {
                if(!theresAWayOut(j, k))
                    break;
            }
            if(k < N)
                break;
        }
        cout << "Case #" << i << ": ";
        if(j < M)
            cout << "NO" << endl;
        else
            cout << "YES" << endl;
        
    }

    return 0;
}

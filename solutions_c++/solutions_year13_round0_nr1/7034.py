#include <iostream>
#include <fstream>
using namespace std;
int main()
{
    ifstream cin("in.txt");
    ofstream cout("out.txt");
    int t;
    cin>>t;
    for (int T=0;T<t;T++)
    {
        int N = 4;
        int pooint = 0;
        char maze[5][5];
        for (int i=0;i<N;i++)
        for (int j=0;j<N;j++)
        {
            char cc;
            cin>>cc;
            if (cc == '.') pooint = 1;
            maze[i][j] = cc;
        }
        cout<<"Case #"<<T+1<<": ";
        int result = 0;
        for (int i=0;i<N;i++)
        {
            int X = 0, O = 0, add = 0;
            for (int j=0;j<N;j++)
                if (maze[i][j] == 'X') X++;
                else if (maze[i][j] == 'O') O++;
                else if (maze[i][j] == 'T') add=1;
            if (X+add == N) result = 1;
            if (O+add == N) result = 2;
        }
        for (int j=0;j<N;j++)
        {
            int X = 0, O = 0, add = 0;
            for (int i=0;i<N;i++)
                if (maze[i][j] == 'X') X++;
                else if (maze[i][j] == 'O') O++;
                else if (maze[i][j] == 'T') add=1;
            if (X+add == N) result = 1;
            if (O+add == N) result = 2;
        }
        int X = 0, O = 0, add = 0;
        for (int i=0;i<N;i++)
            if (maze[i][i] == 'X') X++;
            else if (maze[i][i] == 'O') O++;
            else if (maze[i][i] == 'T') add=1;
        if (X+add == N) result = 1;
        if (O+add == N) result = 2;
        X = 0, O = 0, add = 0;
        for (int i=0;i<N;i++)
            if (maze[i][N-i-1] == 'X') X++;
            else if (maze[i][N-i-1] == 'O') O++;
            else if (maze[i][N-i-1] == 'T') add=1;
        if (X+add == N) result = 1;
        if (O+add == N) result = 2;
        if (result == 1)
            cout<<"X won\n";
        if (result == 2)
            cout<<"O won\n";
        if (result == 0 && !pooint)
            cout<<"Draw\n";
        if (result == 0 && pooint)
            cout<<"Game has not completed\n";
    }
    return 0;
}

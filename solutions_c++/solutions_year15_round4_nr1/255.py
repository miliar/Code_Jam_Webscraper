#include <iostream>
#include <fstream>

using namespace std;
const int MAXN = 110;

ifstream fin ("A.in");
ofstream fout ("A.out");

int N, M;
char board[MAXN][MAXN];

pair <int, int> next (pair <int, int> cur, char ch)
{
    int x = cur.first, y = cur.second;
    if (ch == '^')
        return make_pair (x-1, y);
    else if (ch == 'v')
        return make_pair (x+1, y);
    else if (ch == '<')
        return make_pair (x, y-1);
    else if (ch == '>')
        return make_pair (x, y+1);
    else
        return make_pair (x, y);
}

int main()
{
    int T; fin >> T;
    for (int test = 1; test <= T; test++)
    {
        fin >> N >> M;
        for (int i = 0; i < N; i++)
            for (int j = 0; j < M; j++)
                fin >> board[i][j];
        
        int res = 0;
        bool bad = false;
        for (int i = 0; i < N; i++)
            for (int j = 0; j < M; j++)
            {
                if (board[i][j] == '.') continue;
                int x = 0;
                for (int k = 0; k < N; k++)
                    if (i != k && board[k][j] != '.') x++;
                for (int k = 0; k < M; k++)
                    if (j != k && board[i][k] != '.') x++;
                if (x == 0) bad = true;
                
                int a = i, b = j;
                while (true)
                {
                    if (a < 0 || a >= N || b < 0 || b >= M)
                    {
                        res++;
                        break;
                    }
                    
                    if ((a != i || b != j) && (board[a][b] != '.'))
                        break;
                    
                    pair <int, int> nval = next (make_pair (a, b), board[i][j]);
                    a = nval.first;
                    b = nval.second;
                }
            }
        
        fout << "Case #" << test << ": ";
        if (bad)
            fout << "IMPOSSIBLE\n";
        else
            fout << res << "\n";
    }
    return 0;
}

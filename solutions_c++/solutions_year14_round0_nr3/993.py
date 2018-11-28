#include <cstdio>
#include <fstream>
#include <iostream>
#include <map>

using namespace std;

ifstream fin("c.in");
ofstream fout("c.out");

bool Found = false, Vis[10][10];
char F[10][10];
int R, C, M, T;

void print()
{
    for(int i = 1; i <= R; i++)
    {
        for(int j = 1; j <= C; j++)
        {
            if(F[i][j] == 'c')
                fout << "c";
            else if(F[i][j] == '*')
                fout << "*";
            else
                fout << ".";
        }

        fout << "\n";
    }
}

void dfs(int i, int j)
{
    if(i > R || i < 1 || j < 1 || j > C)
        return;
    if(F[i][j] == '*')
        return;
    if(Vis[i][j])
        return;

    Vis[i][j] = true;

    if(F[i][j] == '0')
    {
        dfs(i-1,j);
        dfs(i+1,j);
        dfs(i,j-1);
        dfs(i,j+1);
        dfs(i-1,j+1);
        dfs(i-1,j-1);
        dfs(i+1,j+1);
        dfs(i+1,j-1);
    }
}

void see()
{
    for(int i = 1; i <= R; i++)
        for(int j = 1; j <= C; j++)
            if(F[i][j] != '*')
            {
                F[i][j] = '0';

                for(int x = i-1; x <= i+1; x++)
                    for(int y = j-1; y <= j+1; y++)
                        if(x != i || y != j)
                            if(F[x][y] == '*')
                                F[i][j]++;
            }

    for(int i = 1; i <= R && !Found; i++)
        for(int j = 1; j <= C && !Found; j++)
            if(F[i][j] == '0')
            {
                for(int x = 1; x <= R; x++)
                    for(int y = 1; y <= C; y++)
                        Vis[x][y] = false;

                dfs(i,j);

                bool good = true;

                for(int x = 1; x <= R; x++)
                    for(int y = 1; y <= C; y++)
                        if(F[x][y] != '*' && !Vis[x][y])
                            good = false;

                if(good)
                {
                    Found = true;
                    F[i][j] = 'c';
                    print();
                    return;
                }
            }
}

void process(int r, int c, int m)
{
    if(m == 0)
    {
        if(!Found)
            see();

        return;
    }

    if(c > C)
        r++, c = 1;
    if(r > R)
        return;

    F[r][c] = '*';
    process(r, c+1, m-1);
    F[r][c] = '.';
    process(r, c+1, m);
}

int main()
{
    fin >> T;

    for(int t = 1; t <= T; t++)
    {
        fin >> R >> C >> M;
        Found = false;

        for(int i = 0; i < 10; i++)
            for(int j = 0; j < 10; j++)
                F[i][j] = '.';

        fout << "Case #" << t << ":\n";
        if(M < R*C - 1)
            process(1,1,M);
        else
        {
            Found = true;

            for(int i = 1; i <= R; i++)
            {
                for(int j = 1; j <= C; j++)
                {
                    if(i < R || j < C)
                        fout << "*";
                    else
                        fout << "c";
                }

                fout << "\n";
            }
        }
        if(!Found)
            fout << "Impossible\n";
    }
}

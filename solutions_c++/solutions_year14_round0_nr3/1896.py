#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <utility>
#include <queue>

#define INF ~(1 << 31)
#define MAXL 11

using namespace std;

typedef pair<int, int> pii;

char grid[MAXL][MAXL];
int mine_count[MAXL][MAXL];
bool visited[MAXL][MAXL];

bool noMineSurround(int r, int c, int R, int C)
{
    for (int dy = -1; dy <= 1; dy++)
        for (int dx = -1; dx <= 1; dx++)
            if (r + dy < R && r + dy >= 0)
                if (c + dx < C && c + dx >= 0)
                    if (grid[r+dy][c+dx] == '*')
                        return false;
    return true;
}

//count includes if grid[r][c] is a mine...
void count_mines(int R, int C)
{
    for (int r = 0; r < R; r++)
        for (int c = 0; c < C; c++)
            mine_count[r][c] = 0;
    
    for (int r = 0; r < R; r++)
        for (int c = 0; c < C; c++)
            for (int dr = -1; dr <= 1; dr++)
                for (int dc = -1; dc <= 1; dc++)
                    if (r+dr >= 0 && r+dr < R)
                        if (c+dc >= 0 && c+dc < C)
                            if (grid[r+dr][c+dc] == '*')
                                mine_count[r][c]++;
}

int countReachable(int r, int c, int R, int C)
{
    if (mine_count[r][c] > 0)
        return 1;
        
    for (int i = 0; i < R; i++)
        for (int j = 0; j < C; j++)
            visited[i][j] = false;
    
    queue<pii> q;
    q.push(pii(r, c));
    visited[r][c] = true;
    int reachable = 1;
    
    while (!q.empty())
    {
        pii p = q.front();
        q.pop();
        
        //add all possible neighbors
        for (int dr = -1; dr <= 1; dr++)
            for (int dc = -1; dc <= 1; dc++)
                if (p.first + dr < R && p.first + dr >= 0)
                    if (p.second + dc < C && p.second + dc >= 0)
                        if (grid[p.first+dr][p.second+dc] == '.')
                            if (!visited[p.first+dr][p.second+dc])
                            {
                                visited[p.first+dr][p.second+dc] = true;
                                reachable++;
                                if (mine_count[p.first+dr][p.second+dc] == 0)
                                    q.push(pii(p.first+dr, p.second+dc));
                            }
                    
    }
        
    
    return reachable;
    
}

bool checkGrid(int R, int C, int M)
{
    
    count_mines(R, C);
    for (int r = 0; r < R; r++)
        for (int c = 0; c < C; c++)
            if (grid[r][c] == '.')
                if (countReachable(r, c, R, C) == (R*C)-M)
                {
                    grid[r][c] = 'c';
                    return true;
                }
    return false;
}

bool find(int R, int C, int M, int m_placed, int r, int c)
{
    if (m_placed == M)
        return checkGrid(R, C, M);
    
    if (r >= R || c >= C)
        return false;
    //check at each position, try to put a mine there, and dont put a mine there
    
    //try placing a mine
    int next_r = r, next_c = c;
    next_c = (c+1 >= C) ? 0 : c+1;
    next_r = (c+1 >= C) ? r+1 : r;
    grid[r][c] = '*';
    if (find(R, C, M, m_placed+1, next_r, next_c))
        return true;
    grid[r][c] = '.';
    return (find(R, C, M, m_placed, next_r, next_c));
}

int main(int argc, char *argv[]) {
    
    ifstream fin("minesweep.in");
    ofstream fout("minesweep.out");
    
    int T; fin >> T;
    int R, C, M;
    for (int c = 1; c <= T; c++)
    {
        fin >> R >> C >> M;
        for (int i = 0; i < R; i++)
            for (int j = 0; j < C; j++)
                grid[i][j] = '.';
            
        fout << "Case #" << c << ":\n";
        if (find(R, C, M, 0, 0, 0))
        {
            for (int i = 0; i < R; i++)
            {
                for (int j = 0; j < C; j++)
                    fout << grid[i][j];
                fout << "\n";
            }
        }
        else fout << "Impossible\n";
        
    }
    fin.close();
    fout.close();
    return 0;
}
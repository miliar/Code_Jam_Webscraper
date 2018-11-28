#include <algorithm>
#include <cassert>
#include <iostream>
#include <fstream>
#include <queue>

using namespace std;

int T;
int R, C, M, E;
bool transpose = false;
bool impossible = false;

char a[60][60];
const char empty = '.';
const char bomb = '*';
const char click = 'c';

void Init()
{
    for (int i = 0; i < 60; ++i)
    {
        for (int j = 0; j < 60; ++j)
        {
            a[i][j] = bomb;
        }
    }
}

void Solve0()
{
    a[0][0] = click;
}

void Solve1()
{
    if (E >= 2)
    {
        for (int i = 0; i < E; ++i)
        {
            a[0][i] = empty;
        }
        a[0][0] = click;
    }
    else
    {
        impossible = true;
    }
}

void Solve2()
{
    if (E >= 4 && E % 2 == 0)
    {
        for (int i = 0; i < E / 2; ++i)
        {
            a[0][i] = a[1][i] = empty;
        }
        a[0][0] = click;
    }
    else
    {
        impossible = true;
    }
}

void Solve3()
{    
    if (E >= 4 && E != 5 && E != 7)
    {
        switch (E)
        {
        case 4:
            a[0][0] = a[0][1] = a[1][0] = a[1][1] = empty;
            a[0][0] = click;
            break;
        case 6:
            a[0][0] = a[0][1] = a[0][2] = empty;
            a[1][0] = a[1][1] = a[1][2] = empty;
            a[0][1] = click;
            break;
        case 8:
            a[0][0] = a[0][1] = a[0][2] = empty;
            a[1][0] = a[1][1] = a[1][2] = empty;
            a[2][0] = a[2][1] = empty;
            a[0][1] = click;
            break;
        case 9:
            a[0][0] = a[0][1] = a[0][2] = empty;
            a[1][0] = a[1][1] = a[1][2] = empty;
            a[2][0] = a[2][1] = a[2][2] = empty;
            a[1][1] = click;
            break;
        case 10:
            a[0][0] = a[0][1] = a[0][2] = a[0][3] = empty;
            a[1][0] = a[1][1] = a[1][2] = a[1][3] = empty;
            a[2][0] = a[2][1] = empty;
            a[0][1] = click;
            break;
        default: // E >= 11
            if (E % 3 == 0)
            {
                int i = 0;
                for (; i < E / 3; ++i)
                {
                    a[0][i] = a[1][i] = a[2][i] = empty;
                }
                a[1][i - 2] = click;
            }
            else if (E % 3 == 1)
            {
                int i = 0;
                for (; i < E / 3 - 1; ++i)
                {
                    a[0][i] = a[1][i] = a[2][i] = empty;
                }
                a[0][i] = a[1][i] = empty;
                ++i;
                a[0][i] = a[1][i] = empty;
                a[1][i - 3] = click;
            }
            else if (E % 3 == 2)
            {
                int i = 0;
                for (; i < E / 3; ++i)
                {
                    a[0][i] = a[1][i] = a[2][i] = empty;
                }
                a[0][i] = a[1][i] = empty;
                a[1][i - 2] = click;
            }
            break;
        };
    }
    else
    {
        impossible = true;
    }
}

void Solve4()
{
    if (E >= 4 && E != 5 && E != 7)
    {
        if (E <= 12)
        {
            Solve3();
        }
        else if (E >= 13 && E <= 16)
        {
            for (int i = 0; i < 4; ++i)
            {
                a[0][i] = a[1][i] = a[2][i] = a[3][i] = empty;
            }
            if (E == 13)
            {
                a[2][3] = a[3][3] = a[3][2] = bomb;
                a[1][1] = click;
            }
            else if (E == 14)
            {
                a[2][3] = a[3][3] = bomb;
                a[1][1] = click;
            }
            else if (E == 15)
            {
                a[3][3] = bomb;
                a[1][1] = click;
            }
            else if (E == 16)
            {
                a[1][2] = click;
            }
        }
        else if (E == 17)
        {
            for (int i = 0; i < 5; ++i)
            {
                a[0][i] = a[1][i] = a[2][i] = a[3][i] = empty;
            }
            a[2][4] = a[3][4] = bomb;
            a[0][0] = bomb;
            a[1][2] = click;
        }
        else // E >= 18
        {
            if (E % 4 == 0)
            {
                int i = 0;
                for (; i < E / 4; ++i)
                {
                    a[0][i] = a[1][i] = a[2][i] = a[3][i] = empty;
                }
                a[1][i - 2] = click;
            }
            else
            {
                int i = 0;
                for (; i < E / 4 - 1; ++i)
                {
                    a[0][i] = a[1][i] = a[2][i] = a[3][i] = empty;
                }
                if (E % 4 == 1)
                {
                    a[0][i] = a[1][i] = a[2][i] = empty;
                    ++i;
                    a[0][i] = a[1][i] = empty;
                    a[1][i - 2] = click;
                }
                else if (E % 4 == 2)
                {                    
                    a[0][i] = a[1][i] = a[2][i] = a[3][i] = empty;
                    ++i;
                    a[0][i] = a[1][i] = empty;                    
                    a[1][i - 2] = click;
                }
                else if (E % 4 == 3)
                {
                    a[0][i] = a[1][i] = a[2][i] = a[3][i] = empty;
                    ++i;
                    a[0][i] = a[1][i] = a[2][i] = empty;
                    a[1][i - 1] = click;
                }
            }
        }
    }
    else
    {
        impossible = true;
    }
}

void Solve5()
{
    if (E <= 20)
    {
        Solve4();
    }
    else
    {
        int m = R;
        int n = E / m;
        if (m * n < E)
        {
            ++n;
        }
        for (int i = 0; i < n; ++i)
        {
            a[0][i] = a[1][i] = a[2][i] = empty;
        }
        for (int i = 0; i < m; ++i)
        {
            a[i][0] = a[i][1] = a[i][2] = empty;
        }        
        int rest = E - (m * n - (m - 3) * (n - 3));        
        int row = 3;
        int col = 3;
        while (rest-- > 0)
        {
            a[row][col] = empty;            
            ++col;
            if (col >= n)
            {
                ++row;
                col = 3;
            }
        }
        a[1][1] = click;
    }
}

void Check()
{
    int count = 0;
    if (!transpose)
    {
        for (int i = 0; i < R; ++i)
        {
            for (int j = 0; j < C; ++j)
            {
                if (a[i][j] == empty || a[i][j] == click)
                    ++count;
            }
        }
    }
    else
    {
        for (int i = 0; i < C; ++i)
        {
            for (int j = 0; j < R; ++j)
            {
                if (a[j][i] == empty || a[j][i] == click)
                    ++count;
            }
        }
    }
    assert(count == E);
}

bool visited[60][60];
void Check2()
{
    int count = 0;
    int r = -1;
    int c = -1;
    // find the start
    for (int i = 0; i < R; ++i)
    {
        for (int j = 0; j < C; ++j)
        {
            if (a[i][j] == click)
            {
                r = i;
                c = j;
                break;
            }
        }
        if (r != -1)
        {
            break;
        }
    }
    
    for (int i = 0; i < R; ++i)
    {
        for (int j = 0; j < C; ++j)
        {
            visited[i][j] = false;
        }
    }

    int emptyCount = 0;
    queue<pair<int, int>> q;
    q.push(make_pair(r, c));
    visited[r][c] = true;
    while (!q.empty())
    {
        auto p = q.front();
        q.pop();
        ++emptyCount;
        int bombCount = 0;
        for (int i = -1; i <= 1; ++i)
        {
            for (int j = -1; j <= 1; ++j)
            {
                if (i == 0 && j == 0) continue;
                int rr = p.first + i;
                int cc = p.second + j;
                if (rr >= 0 && rr < R && cc >= 0 && cc < C)
                {
                    if (a[rr][cc] == bomb)
                    {
                        ++bombCount;
                    }
                }
            }
        }
        if (bombCount == 0)
        {
            for (int i = -1; i <= 1; ++i)
            {
                for (int j = -1; j <= 1; ++j)
                {
                    if (i == 0 && j == 0) continue;
                    int rr = p.first + i;
                    int cc = p.second + j;
                    if (rr >= 0 && rr < R && cc >= 0 && cc < C && !visited[rr][cc])
                    {
                        q.push(make_pair(rr, cc));
                        visited[rr][cc] = true;
                    }
                }
            }
        }
    }
    assert(emptyCount == E);
}

void Print()
{
    if (impossible)
    {
        cout << "Impossible" << endl;
    }
    else
    {
        if (!transpose)
        {
            for (int i = 0; i < R; ++i)
            {
                for (int j = 0; j < C; ++j)
                {
                    cout << a[i][j];
                }
                cout << endl;
            }
        }
        else
        {
            for (int i = 0; i < C; ++i)
            {
                for (int j = 0; j < R; ++j)
                {
                    cout << a[j][i];                    
                }
                cout << endl;
            }
        }
        Check();
        Check2();
    }
}

void Solve(int t)
{
    Init();
    impossible = false;
    transpose = false;
    if (R > C)
    {
        transpose = true;
        swap(R, C);
    }
    if (E == 1)
    {
        Solve0();
    }
    else
    {
        switch (R)
        {
        case 1: Solve1(); break;
        case 2: Solve2(); break;
        case 3: Solve3(); break;
        case 4: Solve4(); break;
        default: Solve5(); break;
        };
    }
    cout << "Case #" << t << ":" << endl;
    Print();    
}

int main()
{        
    cin >> T;
    for (int t = 1; t <= T; ++t)
    {
        cin >> R >> C >> M;
        E = R * C - M;
        Solve(t);
    }
}
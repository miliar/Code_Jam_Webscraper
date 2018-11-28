#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <map>
#include <algorithm>
#include <queue>
#define pb push_back
using namespace std;

bool A[5][5];
int C[5][5];
int sol[6][6][30], click[6][6][30];
int dx[] = {-1, 0, 0, 1, -1, 1, -1, 1};
int dy[] = {0, -1, 1, 0, -1, -1, 1, 1};
bool used[25];

queue<int> q;

bool rch(int v, int r, int c)
{
    int i, j, t, x, y, nx, ny, u;
    for(i = 0; i < 25; ++i) used[i] = false;
    while(!q.empty()) q.pop();
    q.push(v);
    used[v] = true;
    while(!q.empty())
    {
        t = q.front(); q.pop();
        x = t / c;
        y = t % c;
        for(i = 0; i < 8; ++i)
        {
            nx = x + dx[i];
            ny = y + dy[i];
            if(nx < 0 || nx >= r || ny < 0 || ny >= c || A[nx][ny]) continue;
            u = nx * c + ny;
            if(!used[u])
            {
                used[u] = true;
                if(C[nx][ny] == 0) q.push(u);
            }
        }
    }
    for(i = 0; i < r; ++i)
        for(j = 0; j < c; ++j)
        {
            if(C[i][j] != -1 && !used[i * c + j])
            {
                return false;
            }
        }
    //for(i = 0; i < r; ++i)
        //for(j = 0; j < c; ++j) cout << i << ' ' << j << ' ' << C[i][j] << ' ' << used[i * r + j] << '\n';
    return true;
}

void bf(int r, int c, int m)
{
    //cout << "solve for " << r << ' ' << c << ' ' << m <<'\n';
    sol[r][c][m] = -1;
    int i, j, k, mask, x, y;
    int na = (1 << (r * c)), v;
    for(i = 0; i < 5; ++i)
        for(j = 0; j < 5; ++j)
    {
        A[i][j] = false;
        C[i][j] = 0;
    }
    for(mask = 0; mask < na; ++mask)
    {
        if(__builtin_popcount(mask) != m) continue;
        for(i = 0; i < r * c; ++i)
        {
            A[i / c][i % c] = ((mask & (1 << i)) > 0);
        }
        for(i = 0; i < r; ++i)
            for(j = 0; j < c; ++j)
            {
                C[i][j] = 0;
                if(A[i][j])
                {
                    C[i][j] = -1;
                    continue;
                }
                for(k = 0; k < 8; ++k)
                {
                    x = i + dx[k];
                    y = j + dy[k];
                    if(x < 0 || x >= r || y < 0 || y >=c) continue;
                    if(A[x][y]) ++C[i][j];
                }
            }
        for(i = 0; i < r; ++i)
            for(j = 0; j < c; ++j)
            {
                if(C[i][j] == 0 && rch(i * c + j, r, c))
                {
                    sol[r][c][m] = mask;
                    click[r][c][m] = i * c + j;
                    //cout << mask << '\n';
                    return;
                }
            }
    }
}

void print(int r, int c, int m)
{
    int i, j;
    for(i = 0; i < r; ++i, cout << '\n')
        for(j = 0; j < c; ++j)
        {
            if(i * c + j == click[r][c][m]) cout << 'c';
            else cout << (A[i][j] ? '*' : '.');
        }
}

void solve(int tc)
{
    cout << "Case #" << tc << ":\n";
    int r, c, m;
    cin >> r >> c >> m;
    int i, j, s = sol[r][c][m];
    if(m == r * c - 1)
    {
        for(i = 0; i < r; ++i, cout <<'\n')
            for(j = 0; j < c; ++j)
        {
            if(i == 0 && j == 0) cout << 'c';
            else cout << '*';
        }
        return;
    }
    if(s == -1)
    {
        cout << "Impossible\n";
        return;
    }
    for(i = 0; i < r * c; ++i)
    {
        A[i / c][i % c] = ((s & (1 << i)) > 0);
    }
    print(r, c, m);
}

int main()
{
    int r, c, m;
    for(r = 1; r < 6; ++r)
        for(c = 1; c < 6; ++c)
            for(m = 0; m < r * c; ++m) bf(r, c, m);
    int tc, t;
    cin >> t;
    for(tc = 1; tc <= t; ++tc) solve(tc);
}



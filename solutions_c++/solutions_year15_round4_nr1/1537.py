#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
#include <algorithm>
#include <queue>
#include <list>
#include <map>
#include <set>

using namespace std;


const int MAX = 110;
const int MAX2 = 11000;
const int MAXT = 400;
const int INF = 2e9 + 1000;
const long long INFl = 2e18;
const int MOD = 1000000007;
const double EPS = 1e-10;

int T;

int R, C;
char st[MAX][MAX];
int c[MAX][MAX];

int get_dir(int x, int y)
{
    if(st[x][y] == '^')
        return 0;
    if(st[x][y] == 'v')
        return 1;
    if(st[x][y] == '<')
        return 2;
    return 3;
}

pair<int, int> search(int x, int y, int dir)
{
    switch(dir)
    {
        case 0:
            --x;
            while(x >= 0)
            {
                if(st[x][y] != '.')
                    return make_pair(x, y);
                --x;
            }
            break;
        case 1:
            ++x;
            while(x < R)
            {
                if(st[x][y] != '.')
                    return make_pair(x, y);
                ++x;
            }
            break;
        case 2:
            --y;
            while(y >= 0)
            {
                if(st[x][y] != '.')
                    return make_pair(x, y);
                --y;
            }
            break;
        case 3:
            ++y;
            while(y < C)
            {
                if(st[x][y] != '.')
                    return make_pair(x, y);
                ++y;
            }
            break;
    }
    return make_pair(-1, -1);
}

bool search(int x, int y)
{
    for(int i = 0; i < 4; ++i)
    {
        pair<int, int> r = search(x, y, i);
        if(r.first >= 0)
            return true;
    }
    return false;
}

void check(int x, int y)
{
    pair<int, int> st[MAX2];
    int cnt = 0;
    st[cnt++] = make_pair(x, y);
    c[x][y] = -1;
    int dir = get_dir(x, y);
    pair<int, int> ct;
    while(true)
    {
        pair<int, int> next = search(x, y, dir);
        //cout << next.first << ' '  << next.second << ' ' << endl;
        if(next.first == -1)
        {
            ct = st[--cnt];
            c[ct.first][ct.second] = 3;
            while(cnt > 0)
            {
                ct = st[--cnt];
                c[ct.first][ct.second] = 1;
            }
            return;
        }
        if(c[next.first][next.second] == 1 || c[next.first][next.second] == 3)
        {
            while(cnt > 0)
            {
                ct = st[--cnt];
                c[ct.first][ct.second] = 1;
            }
            return;
        }
        if(c[next.first][next.second] == 2 || c[next.first][next.second] == -1)
        {
            while(cnt > 0)
            {
                ct = st[--cnt];
                c[ct.first][ct.second] = 2;
            }
            return;
        }
        x = next.first;
        y = next.second;
        st[cnt++] = make_pair(x, y);
        c[x][y] = -1;
        dir = get_dir(x, y);
    }    
}

void print()
{
    int out = 0;
    for(int i = 0; i < R; ++i)
    {
        for(int j = 0; j < C; ++j)
            cout << c[i][j];
        cout << endl;
    }
    cout << endl;
}

int solve()
{
    cin >> R >> C;
    for(int i = 0; i < MAX; ++i)
        for(int j = 0; j < MAX; ++j)
            c[i][j] = 0;
        
    for(int i = 0; i < R; ++i)
        for(int j = 0; j < C; ++j)
            cin >> st[i][j];
        
    for(int i = 0; i < R; ++i)
    {
        for(int j = 0; j < C; ++j)
        {
            if(st[i][j] != '.' && c[i][j] == 0)
            {
                check(i, j);
               //print();
            }
        }
        
    }

    int out = 0;
    for(int i = 0; i < R; ++i)
    {
        for(int j = 0; j < C; ++j)
        {
            if(c[i][j] == 3)
            {
                if(search(i, j))
                    ++out;
                else
                    return -1;
            }
        }
    }
        
    return out;
}

int main()
{  
    freopen("./in.txt", "r", stdin);
    freopen("./out.txt", "w", stdout);
    cin >> T;
    for(int Ti = 0; Ti < T; ++Ti)
    {
        int t = solve();
        if(t < 0)
            cout << "Case #" << Ti + 1 << ": IMPOSSIBLE\n";
        else
            cout << "Case #" << Ti + 1 << ": " << t << "\n";
    }    
}

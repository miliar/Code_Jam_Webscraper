#include<algorithm>
#include<cmath>
#include<cstdio>
#include<cstring>
#include<iostream>
#include<map>
#include<queue>
#include<set>
#include<sstream>

#define forn(i,n) for(int i=0;i<n;i++)
#define all(v) v.begin(),v.end()

using namespace std;

int r,c,m;

char board[5][5];
char board2[5][5];

bool calc()
{
    int m2 = m;
    if(r==1&&c==1)
    {
        board[0][0] = 'c';
        return true;
    }
    if(c==1)
    {
        forn(i,r)
            board[i][0] = '.';
        board[0][0] = 'c';
        int pos = r-1;
        while(m2>0)
        {
            board[pos][0] = '*';
            m2--;
            pos--;
        }
        return true;
    }
    if(r==1)
    {
        forn(i,c)
            board[0][i] = '.';
        board[0][0] = 'c';
        int pos = c-1;
        while(m2>0)
        {
            board[0][pos] = '*';
            m2--;
            pos--;
        }
        return true;
    }
    int sz = r*c;
    if(m == sz-1)
    {
        forn(i,r)
        forn(j,c)
            board[i][j] = '*';
        board[0][0] = 'c';
        return true;
    }
    if(m == sz-2 || m == sz-3 || m == sz-5 || m == sz-7)
        return false;
    if((sz-m)%2 == 0)
    {
        forn(i,r)
        forn(j,c)
            board[i][j] = '.';
        board[0][0] = 'c';
        int posx = r-1, posy = c-1;
        while(m2>0)
        {
            board[posx][posy] = '*';
            m2--;
            if(posx == 1 && m > 0)
            {
                board[posx-1][posy] = '*';
                m2--;
            }
            posy--;
            if(posy==-1)
            {
                posx--;
                posy = c-1;
            }
        }
        return true;
    }
    else
    {
        if(r==2||c==2)
            return false;
        forn(i,r)
        forn(j,c)
            board[i][j] = '.';
        board[0][0] = 'c';
        int posx = r-1, posy = c-1;
        while(m2>0)
        {
            board[posx][posy] = '*';
            m2--;
            if(posx == 2 && m2 > 1)
            {
                board[posx-1][posy] = '*';
                board[posx-2][posy] = '*';
                m2-=2;
            }
            posy--;
            if(posy==-1)
            {
                posx--;
                posy = c-1;
            }
        }
        return true;
    }
}
bool bb;
int tablero[5][5];

bool sinVecinos(int i, int j)
{
    for(int ii=max(i-1,0);ii<=min(r-1,i+1);ii++)
    for(int jj=max(j-1,0);jj<=min(j+1,c-1);jj++)
    if(board2[ii][jj]== '*')
        return false;
    return true;
}

void dfs(int i, int j)
{
    tablero[i][j] = -2;
    for(int ii=max(i-1,0);ii<=min(i+1,r-1);ii++)
    for(int jj=max(j-1,0);jj<=min(j+1,c-1);jj++)
    {
        if(tablero[ii][jj] == 0)
            dfs(ii,jj);
        else if(tablero[ii][jj] != -1)
            tablero[ii][jj] = -2;
    }
    return;
}

bool check()
{
    int a,b;
    forn(i,r)
    forn(j,c)
    {
        if(board2[i][j] == '*')
            tablero[i][j] = -1;
        else if(sinVecinos(i,j)==true)
            tablero[i][j] = 0;
        else
            tablero[i][j] = 1;
        if(board2[i][j] == 'c')
        {
            a=i;
            b=j;
        }
    }
    if(tablero[a][b] == 0)
        dfs(a,b);
    else
        tablero[a][b] = -1;
    forn(i,r)
    forn(j,c)
    if(tablero[i][j] >= 0)
        return false;
    return true;

}

void go(int row, int col, int mines, int start)
{
    if(bb==true)
        return;
    if(row == r)
    {
        if(start == 1 && mines == m && check()==true)
        {
            forn(i,r)
            forn(j,c)
                board[i][j] = board2[i][j];
            bb = true;
        }
        return;
    }
    int row2 = row, col2 = col+1;
    if(col2==c)
    {
        col2 = 0;
        row2++;
    }
    board2[row][col] = '.';
    go(row2,col2,mines,start);
    if(mines<m)
    {
        board2[row][col] = '*';
        go(row2,col2,mines+1,start);
    }
    if(start==0)
    {
        board2[row][col] = 'c';
        go(row2,col2,mines,1);
    }
    return;
}



bool calc2()
{
    bb = false;
    go(0,0,0,0);
    return bb;
}

int main()
{
	freopen("C-small.in","r",stdin);
	freopen("C-small.out","w",stdout);
    int casos;
	cin >> casos;
	forn(casito,casos)
	{
        cout << "Case #" << casito+1 <<":" << endl;
        cin >> r >> c >> m;
        if(calc2()==false)
            cout << "Impossible" << endl;
        else
        {
            forn(i,r)
            {
                forn(j,c)
                    cout << board[i][j];
                cout << endl;
            }
        }
	}
}

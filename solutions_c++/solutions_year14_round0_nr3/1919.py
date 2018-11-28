#include <cstdio>
#include <iostream>
 
using namespace std;
 
 
int a[100][100];
int used[100][100];
 
int dx[] = {1, 1, -1, -1, 0, 0, -1, 1};
int dy[] = {1, -1, 1, -1, 1, -1, 0, 0};
 
/*
void qwe (int r, int c)
{
        for ( int i = 0; i < r; i++)
        {      
                for ( int j = 0; j < c; j++)
                        cout  << a[i][j];
                cout  <<  "\n";
        }
        cout  << endl;
}
     
void qwe_used (int r, int c)
{
        for ( int i = 0; i < r; i++)
        {      
                for ( int j = 0; j < c; j++)
                        cout  << used[i][j];
                cout  <<  "\n";
        }
        cout  << endl;
}
*/
 
void dfs ( int x, int y, int r, int c)
{
        int fl = 0;
        for ( int i = 0; i < 8; i++)
        {
                if ( 0 <= x + dx[i] && x + dx[i] < r && 0 <= y + dy[i] && y + dy[i] < c)
                {
                        if ( a[x + dx[i]][y + dy[i]] == '*')
                        {
                                fl = 1;
 
                        }
                }
        }      
        if ( fl == 1)
                return;
        used[x][y] = 1;
        for ( int i = 0; i < 8; i++)
        {
                if ( 0 <= x + dx[i] && x + dx[i] < r && 0 <= y + dy[i] && y + dy[i] < c)
                        if ( a[x + dx[i]][y + dy[i]] != '*' && used[x + dx[i]][y + dy[i]] == 0)
                                dfs(x + dx[i], y + dy[i], r, c);
        }
}
 
 
 
int chek ( int r, int c, int col)
{      
        //qwe(r, c);
        int flag = 0;
 
        for ( int i = 0; i < r; i++)
                for ( int j = 0; j < c; j++)
                        used[i][j] = 0;
 
 
        for ( int i = 0; i < r; i++)
                for ( int j = 0; j < c; j++)
                        if ( a[i][j] == 'c')
                        {
                                dfs(i, j, r, c);
                                if ( used[i][j] == 0)
                                        flag = 1;
                        }
 
        //cerr << flag << " " << r * c - 1 << "  && "<< col << endl;
        if ( flag == 1 && r * c - 1 != col)
        {
               
                return -1;
        }
               
        //qwe_used(r, c);
        for ( int i = 0; i < r; i++)
                for ( int j = 0; j < c; j++)
                {
                       
                        if ( used[i][j] == 0 && a[i][j] == '.')
                        {
                                int fl = 0;
                                for ( int q = 0; q < 8; q++)
                                {
                                        if ( 0 <= i + dx[q] && i + dx[q] < r && 0 <= j + dy[q] && j + dy[q] < c)
                                        {
                                                if ( used[i +dx[q]][j + dy[q]] == 1)
                                                        fl = 1;
                                        }
                                }
                                if ( fl == 0)
                                {      
                                        //qwe(r, c);
                                        return -1;
                                }
                        }
                }
 
    return 0;  
}
 
             
 
int foo ( int r, int c, int m, int x, int y, int col)
{
       
        if ( x == 0 && y == 0)
        {
                a[x][y] = 'c';
                y++;
        }
               
        if ( col == m)
        {
                //cerr << col << " " << m << endl;
                //qwe(r, c);
                return chek(r, c, m);
        }
        if ( c == y)
        {
                y = 0;
                x++;
        }
        if ( x == r)
                return -1;
        //cerr << x << " " << y << endl;
        //cout << x << " " << y << endl;
       
        if ( x == 0 && y == 0)
        {
                a[x][y] = 'c';
                return foo(r, c, m, x, y + 1, col);
        }
        a[x][y] = '.';
        int o = foo(r, c, m, x, y + 1, col);
        if ( o == 0)
                return 0;
        a[x][y] = '*';
        o = foo(r, c, m, x, y + 1, col + 1);
       
        if ( o != 0)
                a[x][y] = '.';
        return o;      
}
 
void solv (int r, int c, int m)
{
        for ( int i = 0; i < r; i++)
                for ( int j = 0; j < c; j++)
                        a[i][j] = '.';
        int fl = foo(r, c, m, 0, 0, 0);
        if ( fl == -1)
        {
                printf("Impossible\n");
        }
        else
        {
                for ( int i = 0; i < r; i++)
                {      
                        for ( int j = 0; j < c; j++)
                                printf("%c", a[i][j]);
                        printf("\n");
                }
        }
 
}
 
int main()
{
        int col;
        scanf("%d", &col);
        for ( int ii = 0; ii < col; ii++)
        {
                int r, c, m;
                scanf("%d%d%d", &r, &c, &m);
                //cerr << r << " " << c << " " << m << endl;   
                printf("Case #%d:\n", ii + 1);
                //printf("Case #%d: %d %d %d\n", ii + 1, r, c, m);
                solv(r, c, m);
        }
 
        return 0;
}

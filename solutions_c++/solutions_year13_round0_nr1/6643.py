//{ Template
using namespace std;
//{ C-headers
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <climits>
#include <cfloat>
#include <cctype>
#include <cassert>
#include <ctime>
#include<sstream>
//}
//{ C++-headers
#include <iostream>
#include <iomanip>
#include <sstream>
#include <algorithm>
#include <utility>
#include <string>
#include <stack>
#include <queue>
#include <vector>
#include <set>
#include <map>
//}
//{ Loops
#define forab(i,a,b) for (__typeof(b) i = (a); i <= (b); ++i)
#define rep(i,n) forab (i, 0, (n) - 1)
#define For(i,n) forab (i, 1, n)
#define rofba(i,a,b) for (__typeof(b) i = (b); i >= (a); --i)
#define per(i,n) rofba (i, 0, (n) - 1)
#define rof(i,n) rofba (i, 1, n)
#define forstl(i,s) for (__typeof ((s).end ()) i = (s).begin (); i != (s).end (); ++i)
//}
//{ Floating-points
#define EPS DBL_EPSILON
#define abs(x) (((x) < 0) ? - (x) : (x))
#define zero(x) (abs (x) < EPS)
#define equal(a,b) (zero ((a) - (b)))
#define PI 2 * acos (0.0)
//}
//}

char mat[10][10];
int valid()
{
    rep(i,4)
        rep(j,4)
            if( mat[i][j] == '.' ) return 0;
    return 1;
}
int f1(char c)
{
    int cnt ,T ;
    rep(i,4){
        cnt = T = 0 ;
        rep(j,4) {
            if(mat[i][j] == c )cnt++;else if( mat[i][j] == 'T' )T++;
        }
        if(( cnt == 3 && T == 1) ||(cnt == 4) )return 1;
    }
    return 0;
}
int f2(char c)
{
    int cnt ,T   ;
    rep(j,4){
        cnt = T = 0 ;
        rep(i,4) {
            if(mat[i][j] == c )cnt++;else if( mat[i][j] == 'T' )T++;
        }
        if( (cnt == 3 && T == 1) || (cnt == 4) )return 1;
    }
    return 0;
}
int f3(char c)
{
    int cnt = 0  ,T = 0;
    rep(i,4)if(mat[i][i] == c )cnt++; else if( mat[i][i] == 'T' )T++;
    if(cnt == 4 || (cnt == 3 && T == 1) )return 1;
    cnt = T = 0 ;
    if(mat[0][3] == c) cnt++;
    else if(mat[0][3] == 'T')T++;
    if(mat[1][2] == c) cnt++;
    else if(mat[1][2] == 'T')T++;
    if(mat[2][1] == c) cnt++ ;
    else if(mat[2][1] == 'T')T++;
    if(   mat[3][0] == c ) cnt++ ;
    else if(   mat[3][0] == 'T' )T++;
    if(cnt == 4 || (cnt == 3 && T == 1) )return 1;
    return 0;
}
int main()
{
    /*freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);*/
    int t , cs = 1;
    cin >>t;
    while(t--)
    {
        rep(i,4)scanf("%s",mat[i]);
        bool ok = valid();
        printf("Case #%d: ",cs++);
        int X = f1('X') + f2('X') + f3('X');
        if( X > 0 )puts("X won");
        else
        {
             int O = f1('O') + f2('O') + f3('O');
             if(O > 0) puts("O won");
             else
             {
                 if(ok)puts("Draw");
                  else puts("Game has not completed");
             }
        }
    }
}


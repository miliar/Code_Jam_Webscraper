#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>
#include <bitset>
#include <climits>
#include <stack>
#include <cctype>
#include <sstream>
#include <iomanip>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<ii> vii;

int p[] = {1 , 1 , 1, 0 , 0 , -1 , -1 , -1 } ;
int q[] = {1, -1  ,0 , -1 , 1 , 1, 0 , -1  } ;
char arr[55][55] ;
int g[55][55] ;
int remaining ;
int  C , R , X ;
int lefti ;

int bfs(int x , int y  )
{
    int noofspace  ;
    if(g[x][y] == 0 )
        noofspace = 1 ;
    else
        noofspace = 0 ;

    if( noofspace == lefti )
    {
        g[x][y] = 1 ;
        return 0 ;
    }

     for(int i =0 ; i < 8 ; i++ )
    {
         if(g[x+p[i]][y+q[i]] == 0)
             noofspace++ ;
    }

    if(lefti >= noofspace && noofspace > 0  )
    {
        g[x][y] = 1 ;
        for(int i =0 ; i < 8 ; i++ )
            {
                if(g[x+p[i]][y+q[i]] == 0)
                    g[x+p[i]][y+q[i]] = 1 ;
            }

        lefti -= noofspace ;

        if(left == 0)
            return 0 ;

        for(int i =0 ; i < 8 ; i++ )
            {
                if(g[x+p[i]][y+q[i]] == 1)
                    {

                        int res  = bfs( x+p[i] , y+ q[i]   )  ;
                        if(res == 0 )
                            return  0 ;
                    }
            }
        return  -1   ;
    }
    else
        return -1 ;
}

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    int T ;
    cin>>T ;
    int cnt = 1;
    while(T--)
    {

        cin>>C>>R>>X ;
        memset( g , 0 , sizeof(g)) ;
        remaining = C*R - X ;
        int done = 0 ;
        for(int i= 0 ; i <= C+1 ;  i++ )
        {
            for(int j=0 ; j <= R+1 ; j++ )
            {
                if(i == 0 || j == 0 || i == C+1 || j ==R+1)
                    g[i][j] = -1 ;
                else
                    g[i][j] = 0 ;
            }
        }

        for(int i= 1 ; i <= C ;  i++ )
        {
            for(int j=1 ; j <= R ; j++ )
            {
                lefti = remaining ;
                if(  done == 0  && bfs(i , j ) == 0)
                    {
                        //cout<<"Possible"<<endl ;
                        done = 1 ;
                        g[i][j] = 2 ;
                        break ;
                    }
                else
                {
                    for(int i= 0 ; i <= C+1 ;  i++ )
                    {
                        for(int j=0 ; j <= R+1 ; j++ )
                        {
                            if(i == 0 || j == 0 || i == C+1 || j ==R+1)
                                g[i][j] = -1 ;
                            else
                                g[i][j] = 0 ;
                        }
                    }
                }
            }
            if(done == 1 )
                break ;
        }
        cout<<"Case #"<<cnt++<<":"<<endl ;
        if(done == 1)
        for(int i= 1 ; i <= C ;  i++ )
        {
            for(int j=1 ; j <= R ; j++ )
            {
                if(  g[i][j] == 0 )
                    cout<<'*' ;
                else if(g[i][j] == 2)
                    cout<<'c' ;
                else if(g[i][j] == 1)
                    cout<<'.' ;
            }
            cout<<endl ;
        }

        if(done == 0 )
            cout<<"Impossible"<<endl ;

    }
    return 0 ;
}

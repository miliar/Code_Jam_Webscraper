/*
 * Author:  vawait
 * Created Time:  2015/5/30 22:14:04
 * Problem: test.cpp
 */
#include<cstdio>
#include<iostream>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<string>
#include<map>
#include<set>
#include<vector>
#include<queue>
#include<stack>
#include<ctime>
using namespace std;
#define rep(i, a, b) for (int i = (a); i <= (b); ++i)
#define red(i, a, b) for (int i = (a); i >= (b); --i)
#define clr( x , y ) memset(x,y,sizeof(x))
#define mp make_pair
#define pb push_back
#define x first
#define y second
#define sqr(x) ((x) * (x))
#define num( x , y ) ( ( x - 1 ) * m + y )
typedef long long lint;
const int maxn = 20010;
int n , m , f[maxn] , vis[maxn] , dx[200] , dy[200] , aa[maxn];
char a[110][100];
vector < int > g[maxn];

bool ok(int x,int y)
{
    return ( x >= 1 && x <= n && y <= m && y >= 1 );
}

int find(int t)
{
    return f[t] == t ? t : f[t] = find( f[t] );
}

void init()
{
    scanf("%d%d",&n,&m);
    rep(i,1,n) scanf("%s",a[i]+1);
    clr( dx , 0 ); clr( dy , 0 );
    rep(i,1,n*m) f[i] = i , g[i].clear();
    rep(i,1,n)
        rep(j,1,m) if ( a[i][j] != '.' ) {
            dx[i] ++;
            dy[j] ++;
            int x = i , y = j , xx , yy;
            if ( a[i][j] == '>' ) xx = 0 , yy = 1;
            if ( a[i][j] == '<' ) xx = 0 , yy = -1;
            if ( a[i][j] == '^' ) xx = -1 , yy = 0;
            if ( a[i][j] == 'v' ) xx = 1 , yy = 0;
            x += xx; 
            y += yy;
            while ( ok( x , y ) ) {
                if ( a[x][y] != '.' ) {
                    g[num(i,j)].pb( num( x , y ) );
                    f[find(num(i,j))] = find( num( x , y ) ); 
                    break;
                }
                x += xx; y += yy;
            }
        }
    clr( vis , 0 );
    clr( aa , 0 );
}

int dfs(int t)
{
    vis[t] = 1;
    red(i,g[t].size()-1,0) {
        int y = g[t][i];
        if ( vis[y] ) return 1;
        if ( !vis[y] && dfs( y ) ) return 1;
    }
    return 0;
}

void work()
{
    rep(i,1,n)
        rep(j,1,m) if ( a[i][j] != '.' && dx[i] == 1 && dy[j] == 1 ) {
            puts("IMPOSSIBLE");
            return;
        }
    int ans = 0;
    rep(i,1,n)
       rep(j,1,m) if ( a[i][j] != '.' && find( num( i , j ) ) == num( i , j ) ) ans ++;
    rep(i,1,n)
       rep(j,1,m) if ( a[i][j] != '.' && find( num( i , j ) ) == num( i , j ) && dfs( num( i , j ) ) )
         ans --;
    printf("%d\n",ans);
}

int main()
{
    freopen("1.out","w",stdout);
    int t;
    cin >> t;
    rep(i,1,t) {
        printf("Case #%d: ",i);
        init();
        work();
    }
    return 0;
}

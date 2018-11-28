/*
 * Author:  vawait
 * Created Time:  2016/5/28 23:45:10
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
typedef long long lint;
int n , m , sum , a[100][100] , b[10][10];
pair < int , int > q[100];
char c[100];

void init()
{
    scanf("%d",&n);
    rep(i,1,n) {
        scanf("%s",c+1);
        rep(j,1,n) a[i][j] = ( c[j] == '1' );
    }
    sum = 0;
    m = 0;
    rep(i,1,n)
        rep(j,1,n) if ( !a[i][j] ) {
            q[++sum] = mp( i ,j );
        }
}

bool ok(int nn,int x,int y) {
    if ( nn > n ) return 1;
    rep(i,1,n) if ( ( x >> i & 1 ) == 0 ) {
        int p = 0;
        rep(j,1,n) if ( ( y >> j & 1 ) == 0 && b[i][j] ) {
            p = 1;
            if ( !ok( nn + 1 , x | ( 1 << i ) , y | ( 1 << j ) ) )
                return 0;
        }
        if ( !p ) return 0;
    }
    return 1;
}


void work()
{
    int ans = 100;
    m = ( 1 << sum ) - 1;
    rep(i,0,m) {
        rep(j,1,n)
            rep(k,1,n) b[j][k] = a[j][k];
        int as = 0;
        rep(j,0,sum-1) if ( i >> j & 1 ) {
            int x = j + 1;
            b[q[x].x][q[x].y] = 1;
            as ++;
        }
        if ( ok( 1 , 0 , 0 ) ) ans = min( ans , as );
    }
    printf("%d\n",ans);
}

int main()
{
    freopen("a.out","w",stdout);
    int t;
    cin >> t;
    rep(i,1,t ) {
        printf("Case #%d: ",i);
        init();
        work();
    }
    return 0;
}

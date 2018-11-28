/*
 * Author:  vawait
 * Created Time:  2016/5/28 22:55:06
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
int a[30][10] ,n , m , f[2][1<<14] , now = 0 , nex = 1;

int vs[4][4] = {
    -1 , -1 , 1 , 0 ,
    -1 , -1 , 1 , 0 ,
    -1 , 0 , -1 , 1 ,
    -1 , 1 , 0 , -1 ,
};

bool sm(int l,int r,int n ) {
    rep(i,0,n-1) {
        if ( f[now][l+i] < f[now][r+i] ) return 0;
        if ( f[now][l+i] > f[now][r+i] ) return 1;
    }
    return 0;
}

void big(int l,int r,int n) {
    if ( sm( l , r , n ) ) {
        rep(i,0,n-1) swap( f[now][l+i] , f[now][r+i] ); 
    }
}

void init()
{
    cin >> n;
    scanf("%d%d%d",&a[0][2],&a[0][1],&a[0][3]);
    m = ( 1 << n );
    rep(i,1,n) {
        int sum = 0 , k = 0;
        rep(j,1,3) sum += a[i-1][j];
        if ( sum & 1 ) {
            puts("IMPOSSIBLE");
            return;
        }
        sum >>= 1;
        a[i][2] = sum - a[i-1][1];  
        a[i][3] = sum - a[i-1][2];
        a[i][1] = sum - a[i-1][3];
        rep(j,1,3) if ( a[i][j] < 0 || a[i][j] > sum ) {
            puts("IMPOSSIBLE");
            return;
        }
        rep(j,1,3) k += a[i][j];
        if ( k != sum ) {
            puts("IMPOSSIBLE");
            return;
        }
    }
    
    rep(i,1,3) if ( a[n][i] ) f[now][1] = i;
    int k = 1;
    rep(i,1,n) {
        swap( now , nex );
        int sum = 0;
        rep(j,1,k) {
            if ( f[nex][j] == 1 ) {
                f[now][++sum] = 1;
                f[now][++sum] = 2;
            }
            if ( f[nex][j] == 2 ) {
                f[now][++sum] = 2;
                f[now][++sum] = 3;
            }
            if ( f[nex][j] == 3 ) {
                f[now][++sum] = 1;
                f[now][++sum] = 3;
            }
        }
        k <<= 1;
    }
    
    k = 1 << n;
    for ( int i = 1; i <= k; i *= 2 ) {
        for ( int j = 1; j + i <= k; j += i * 2 ) {
            big( j , j + i , i );
        }
    }
    rep(i,1,k) {
        if ( f[now][i] == 1 ) printf("P");
        if ( f[now][i] == 2 ) printf("R");
        if ( f[now][i] == 3 ) printf("S");
    }
    puts("");
}

void work()
{
}

int main()
{
    int t;
    cin >> t;
    freopen("a.out","w",stdout);
    rep(i,1,t) {
        printf("Case #%d: ",i);
        init();
        work();
    }
    return 0;
}

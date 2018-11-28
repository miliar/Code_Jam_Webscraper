/*
 * Author:  vawait
 * Created Time:  2015/4/11 11:47:34
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
int sum[1100];

void init()
{
    int x , n;
    clr( sum , 0 );
    scanf("%d",&n);
    rep(i,1,n) scanf("%d",&x) , sum[x] ++;
}

int deal(int y,int m)
{
    rep(i,m+1,1000) if ( sum[i] )
        y -= sum[i] * ( ( i + m - 1 ) / m - 1 );
    return y >= 0;
}

int ok(int k)
{
    rep(i,0,k-1) if ( deal( i , k - i ) ) return 1;
    return 0;
}

void work()
{
    int l = 0 , r = 2000 , k;
    while ( l < r ) {
        k = ( l + r ) >> 1;
        if ( ok( k ) ) r = k; else l = k + 1;
    }
    printf("%d\n",l);
}

int main()
{
    freopen("1.out","w",stdout);
    int t;
    scanf("%d",&t);
    rep(i,1,t) {
        printf("Case #%d: ",i);
        init();
        work();
    }
    return 0;
}

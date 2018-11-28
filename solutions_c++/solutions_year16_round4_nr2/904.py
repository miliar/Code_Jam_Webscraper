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
int n , m ;
double a[100] , b[100] , f[100][100] , ans;

void init()
{
    double x;
    scanf("%d%d",&n,&m);
    rep(i,1,n) {
        scanf("%lf",&b[i]);
    }
    ans = 0;
}

void kk()
{
    clr( f , 0 );
    f[0][0] = 1;
    rep(i,1,m) {
        rep(j,0,m) {
            f[i][j] = f[i-1][j] * ( 1 - a[i] );
            if ( j ) f[i][j] += f[i-1][j-1] * a[i];
        }
        /*
        red(j,m,0)
            red(k,m,0) {
                f[j+1][k] += f[j][k] * a[i];
                f[j][k+1] += f[j][k] * ( 1 - a[i] );
            }
            */
    }
    ans = max( ans , f[m][m/2] );
}

void work()
{
    int k = 1 << n;
    rep(i,1,k-1) {
        int sum = 0;
        rep(j,0,n-1) if ( i >> j & 1 ) {
            a[++sum] = b[j+1];
        }
        if ( sum == m ) kk();
    }
    printf("%.7f\n",ans);
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

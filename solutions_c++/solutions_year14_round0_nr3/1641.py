/*
 * Author:  vawait
 * Created Time:  2014年04月12日 星期六 23时30分07秒
 * File Name: 1.cpp
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
using namespace std;
#define rep(i, a, b) for (int i = (a); i <= (b); ++i)
#define red(i, a, b) for (int i = (a); i >= (b); --i)
#define clr( x , y ) memset(x,y,sizeof(x))
#define sqr(x) ((x) * (x))
#define mp make_pair
#define pb push_back
typedef long long lint;
int x , y , t , a[60][60];

void init()
{
	cin >> x >> y >> t;
	clr( a , 0 );
	t = x * y - t;
	//printf("%d %d %d\n",x,y,t);
}

int ok(int x,int y)
{
	if ( t == 1 ) return 1;
	if ( x == 1 ) {
		rep(i,2,t) a[1][i] = 2;
		return 1;
	}
	if ( t < 4 ) return 0;
	int i = 1 , j = 1;
	while ( t && i < x ) {
		if ( t < 4 && j == 1 ) break;
		if ( t == 1 && i == 1 ) break;
		t --; a[i][j] = 2;
		if ( t ) t -- , a[i+1][j] = 2;
		j ++;
		if ( j > y ) j = 1 , i += 2;
	}
	if ( !t ) return 1;
	if ( j > 1 ) i += 2;
	if ( i > x ) return 0;
	if ( t > 1 ) {
		rep(k,1,t) a[i][k] = 2;
		return 1;
	}
	if ( !t ) return 1;
	if ( j == 1 ) j = y + 1;
	if ( j > 4 ) {
		a[i-1][j-1] = a[i-2][j-1] = 0;
		rep(k,1,3) a[i][k] = 2;
		return 1;
	}
	if ( i > 3 ) {
		a[i][1] = a[i][2] = 2;
		a[i-1][y-1] = 0;
		return 1;
	} return 0;
}

void cheak(int t)
{
	if ( t == 0 ) printf("*");
	if ( t == 1 ) printf("c");
	if ( t == 2 ) printf(".");
}

void work()
{
	int b = x <= y ? ok(x,y) :ok(y,x);
	a[1][1] = 1;
	if ( b ) {
		rep(i,1,x) {
			rep(j,1,y) cheak( x <= y ? a[i][j] : a[j][i] );
			puts("");
		}
	} else puts("Impossible");
}

int main()
{
	freopen("1.out","w",stdout);
	int t;
	cin >> t;
	rep(i,1,t) {
		printf("Case #%d:\n",i);
		init();
		work();
	}
    return 0;
}

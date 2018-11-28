/*
 * Author:  vawait
 * Created Time:  2014年04月12日 星期六 21时24分43秒
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
double x , y , z , k , ans , p , t;

void init()
{
	ans = 1100;
	cin >> x >> y >> z;
	k = 0;
	p = 2;
	t = 0;
}

void work()
{
	int w;
	while ( 1 ) {
		if ( t > ans || k > z ) break;
		ans = min( ans , t + ( z - k ) / p );
		if ( k < x ) {
			t += ( x - k ) / p;
			k = x;
		}
		w = k / x;
		k -= x * w;
		p += y;
	}
	printf("%.7lf\n",ans);
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

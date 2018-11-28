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
int a[17] , n , m;

void init()
{
	int x;
	clr( a , 0 );
	cin >> n;
	rep(i,1,4)
		rep(j,1,4) {
			scanf("%d",&x);
			if ( i == n ) a[x] ++;
		}
	cin >> n;
	rep(i,1,4)
		rep(j,1,4) {
			scanf("%d",&x);
			if ( i == n ) a[x] ++;
		}
}

void work()
{
	int x = 0 , y;
	rep(i,1,16) if ( a[i] == 2 ) y = i , x ++;
	if ( x == 1 ) printf("%d\n",y);
	else if ( x ) puts("Bad magician!");
	else puts("Volunteer cheated!");
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

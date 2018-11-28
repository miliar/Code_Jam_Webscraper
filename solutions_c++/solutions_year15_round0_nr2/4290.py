#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <cstring>

using namespace std;

#define MAXN 1010

int p[ MAXN ];
int n, maxp, ans;

void init(){
	cin >> n;
	maxp = -1;
	for ( int i = 1; i <= n; i ++ ){
		scanf( "%d", &p[i] );
		if ( maxp == -1 || p[i] > maxp )
			maxp = p[i];
	}
}

int try_eat( int eat ){
	int i, pi, time, s, total = 0;
	for ( i = 1; i <= n; i ++ ){
		pi = p[i];
		time = 0;
		while ( pi > eat ){
			time ++;
			pi -= eat;
		}
		total += time;
	}
	return eat+total; 
}

void cal(){
	ans = maxp;
	int time_i;
	for ( int i = 1; i <= maxp; i ++ ){
		time_i = try_eat(i);
		if ( time_i < ans )
			ans = time_i;
	}
	cout << ans << endl;
}

int main()
{
	freopen( "i.txt", "r", stdin );
	freopen( "out.txt", "w", stdout );
	int t, i;
	scanf( "%d\n", &t );
	for ( i = 1; i <= t; i ++ ){
		init();
		cout << "Case #" << i << ": ";
		cal();
	}
	return 0;
}


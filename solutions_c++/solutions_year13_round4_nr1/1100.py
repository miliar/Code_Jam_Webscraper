// A.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <cstring>

using namespace std;

#define MAXL 200
#define MAXN 200
#define MOD 1000002013

int n, m;
long long cost, ans;
int t[MAXL];

void init(){
	cin >> n >> m;
	int i, j, o, e, p, h;
	memset( t, 0, sizeof(t) );
	cost = 0;
	for ( i = 1; i <= m; i ++ ){
		cin >> o >> e >> p;
		for ( j = o; j <= e-1; j ++ )
			t[j] += p;
		h = e-o;
		cost += (n+n+1-h)*h/2*p;
	}
	/*
	for ( j = 1; j <= n; j ++ )
		cout << t[j] << " ";
	cout << endl;
	*/
}

void cal(){
	int i, j, k, c, min_;
	ans = 0;

	for ( i = n-1; i >= 1; i -- ){
		for ( j = 1; j <= n-i+1; j ++ ){
			min_ = t[j];
			for ( k = j; k <= j+i-1; k ++ )
				min_ = min( t[k], min_ );
			if ( min_ > 0 ){
				ans += min_*(n+n+1-i)*i/2;
				for ( k = j; k <= j+i-1; k ++ )
					t[k] = t[k]-min_;
			}
		}
	}

	//cout << cost << " " << ans << endl;
	cout << (cost-ans) % MOD << endl;
}

int _tmain(int argc, _TCHAR* argv[])
{
	freopen( "A-small-attempt1.in", "r", stdin );
	freopen( "out.txt", "w", stdout );
	int T, i;
	scanf( "%d\n", &T );
	for ( i = 1; i <= T; i ++ ){
		init();
		cout << "Case #" << i << ": ";
		cal();
	}
	return 0;
}


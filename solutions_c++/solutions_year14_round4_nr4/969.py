#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <string>
#include <iostream>
#include <functional>

using namespace std;

typedef pair <int, int> ii;
//typedef pair <long long, long long> ii;
const long long INF = 1000000007;
long long gcd( long long b, long long s ){
	return (s!=0) ? gcd( s, b%s ) : b;
}
long long Pow( long long a, long long b, long long A, long long C ){
	if( b > 1 ) {
		a = Pow( a, b/2, A, C );
		a = (a*a) % C;
		if( b&1 ) a = (a*A) % C;
	}
	return a % C;
}

typedef pair <int, int> ii;

char s[15][15];
int l[15];
int c[5][15];
long long ans = 0, way = 0;

void go(int it, int n, int m){

	if( it == m ){
		/*
		for(int i=0; i<n; i++){
			for(int j=0; j<m; j++)
				printf("%d ", c[i][j]);
			puts("");
		}
		puts("");*/
		for(int i=0; i<n; i++){
			bool ok = 0;
			for(int j=0; j<m; j++){
				if( c[i][j] ){
					ok = 1; 
					break;
				}
			}
			if( !ok ) return;
		}
		//puts("check");
		
		long long res = 0;
		for(int i=0; i<n; i++){

			map <string, bool> mp;
			for(int j=0; j<m; j++){
				if( c[i][j] ){
					string t = "";
					mp[t] = 1;
					for(int k=0; k<l[j]; k++){
						t = t + s[j][k];
						mp[t] = 1;
					}
				}
				
			}
			res += mp.size();
		}
		if( ans < res ){
			ans = res;
			way = 1; 
		}
		else if( ans == res )
			++way;
		//printf("%lld\n", way);

	}
	else{
		for(int i=0; i<n; i++){
			c[i][it] = 1;
			go( it+1, n, m );
			c[i][it] = 0;
		}
	}
	
}

int main(){ 
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int R=1; R<=T; R++){
		int m, n;
		scanf("%d %d", &m, &n);

		for(int i=0; i<m; i++){
			scanf("%s", s[i]);
			l[i] = strlen( s[i] );
		}
		ans = -1;
		way = 1;
		
		for(int j=0; j<n; j++)
			for(int i=0; i<=m; i++)
				c[j][i] = 0;
		go( 0, n, m );

		printf("Case #%d: ", R);
		printf("%lld %lld\n", ans, way);
	}

}
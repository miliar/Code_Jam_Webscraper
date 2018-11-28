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


int a[10005];
typedef pair <int, int> ii;

int main(){ 
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int R=1; R<=T; R++){
		int n, x;
		scanf("%d %d", &n, &x);


		for(int i=0; i<n; i++)
			scanf("%lld", a+i);


		sort( a, a+n );

		set <ii> s;
		set <ii> ::iterator it;

		for(int i=0; i<n; i++)
			s.insert( ii(x-a[i], i) );

		int ans = 0;
		for(int i=0; i<n; i++){
			if( s.count( ii(x-a[i], i ) ) > 0 ){
				s.erase( ii(x-a[i], i) );
				
				it = s.lower_bound( ii( a[i], -1 ) );

				if( it != s.end() )
					s.erase( it );
				++ans;
			}
		}

	
		printf("Case #%d: ", R);
		printf("%d\n", ans);
	}

}
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


int a[1005], b[1005], c[1005];
typedef pair <int, int> ii;

int main(){ 
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int R=1; R<=T; R++){
		int n;
		scanf("%d", &n);
		for(int i=0; i<n; i++){
			scanf("%d", a+i);
			b[i] = i;
		}
		int ans = n*n*n;

		do{
			int cc = 0 ;
			for(int i=1; i<n-1; i++)
				if( a[b[i-1]] < a[b[i]] && a[b[i]] > a[b[i+1]] )
					++cc;
				else if( a[b[i-1]] > a[b[i]] && a[b[i]] < a[b[i+1]] )
					cc = 3;

			if( cc <= 1 ){
				for(int i=0; i<n; i++)
					c[i] = a[i];
				int res = 0;
				for(int i=0; i<n; i++){
					if( a[b[i]] != c[i] ){
						int pos = -1;
						for(int j=0; j<n; j++)
							if( c[j] == a[b[i]] )
								pos = j;

						for(int j=pos; j>=1; j--){
							swap( c[j], c[j-1] );
							++res;
							if( a[b[j-1]] == c[j-1] )
								break;
						}
						
					}
				}
				
				ans = min ( ans, res );
			}

			
		}while( next_permutation( b, b+n ) );
		
		printf("Case #%d: ", R);
		printf("%d\n", ans);
	}

}
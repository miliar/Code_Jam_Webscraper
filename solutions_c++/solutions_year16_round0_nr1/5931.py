#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/detail/standard_policies.hpp>

#define FORN( i , s , n ) for( int i = (s) ; i < (n) ; i++ )
#define FOR( i , n ) FORN( i , 0 , n )
#define pb push_back
#define mp make_pair
#define fst first
#define snd second
#define sz size()
#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define clr(a, v) memset( a , v , sizeof(a) )
#define FORIT( i , x ) for( typeof x.begin() i = x.begin() ; i != x.end() ; i++ )
#define trace(x)    cout << #x << ": " << x << endl;
#define trace2(x, y) cout << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z) cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
#define read ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

using namespace std;
using namespace __gnu_pbds;

typedef long long int64;
typedef vector <int> vi;
typedef pair <int,int> ii;
typedef vector <string> vs;
typedef vector <ii> vii;

int64 solve( int64 N ){
	if( N == 0 ) return -1;
	int a[10]; clr( a , 0 );
	
	int64 cur = N, tmp;
	while(1){
		tmp = cur;
		while( tmp ){
			a[ tmp%10 ] = 1;
			tmp /= 10;
		}
		int complete = 0;
		FOR( i , 10 ){
			complete += a[i];
		}
		if( complete == 10 ) return cur;
		else cur += N;
	}
	return -1;
}

int main(){
	int T; int64 N;
	cin >> T;
	FOR( caso , T ){
		scanf("%lld", &N);
		int64 ans = solve(N);
		if( ans != -1 ) printf("Case #%d: %lld\n", caso+1, ans);
		else printf("Case #%d: INSOMNIA\n", caso+1);
	}
	return 0;
}





























#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/detail/standard_policies.hpp>

#define FORN( i , s , n ) for( int64 i = (s) ; i < (n) ; i++ )
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
typedef vector <int64> vi;
typedef pair <int64,int64> ii;
typedef vector <string> vs;
typedef vector <ii> vii;

int64 prime( int64 n ){
	for( int64 i = 2 ; i*i <= n ; i++ ){
		if( n % i == 0 ) return i;
	}
	return -1;
}

int main(){
	int64 T, N, J; 
	cin >> T;
	FOR( caso , T ){
		cin >> N >> J;
		pair < int64 , vector<int64> > ans[J]; 
		int64 cnt = 0;
		FOR( mask , 1LL<<N ){
			bool a = mask & 1, b = mask & (1LL<<(N-1));
			if( (a == false) or (b == false) ) continue;
			vi div(9);
			bool cagao = 0;
			
			FORN( b , 2 , 11 ){
				int64 tmp = 0;
				FOR(i,N) if( mask & (1<<i) ) tmp += pow(b,i);
				
				int64 prm = prime(tmp);
				if( prm == -1 ){ cagao = 1; break; }
				else div[b-2] = prm;
			}
			if( !cagao ) ans[cnt++] = mp( mask , div );
			if( cnt == J ) break;
			
		}
		
		printf("Case #%lld:\n", caso+1);
		FOR( i , J ){
			for( int64 j = N-1; j >= 0; j-- ){
				if( ans[i].fst & (1<<j) ) cout << "1";
				else cout << "0";
			}
			FOR( j , 9 ){
				cout << " " << ans[i].snd[j];
			}
			cout << endl;
		}
		
	}
	return 0;
}





























//In the name of Allah    
#include <bits/stdc++.h>    
using namespace std;    

#define __sz(x) ((int)(x).size())    
typedef long long ll;    

const int maxN = 100 + 10; 
string a[maxN];
int r[maxN],c[maxN]; 

int n,m;

inline bool inrange( int i , int n ) { return i >= 0 && i < n ;  }
map<char,int> to = { {'^',0} , {'>',1} , {'v',2} , {'<',3} };
int dx[] = { -1 , 0 , 1 , 0 } ; 
int dy[] = { 0 , 1 , 0 , -1 } ; 

void solve() { 
	cin >> n>> m; 
	memset( r , 0 , sizeof r ) ; 
	memset( c , 0 , sizeof c ); 
	for( int i = 0 ; i < n ; i++ ) {
		cin >> a[i];
		for( int j = 0 ; j < m ; j++ ) 
			if( a[i][j] != '.' ) 
				r[i]++, c[j]++; 
	}
	int ans = 0;
	for( int i = 0 ; i < n ; i++ ) 
		for( int j = 0 ; j < m;  j++ ) if( a[i][j] != '.' ) {
			int xx = dx[to[a[i][j]]];
			int yy = dy[to[a[i][j]]];
			int x = i + xx;
			int y = j + yy; 
			bool ch = false;
			while( inrange(x,n) && inrange(y,m) ) {
				if( a[x][y] != '.' ) { 
					ch = true;
					break;
				}
				x += xx;
				y += yy;
			}
			if( !ch ) {
				ans++;
				if( max(r[i],c[j]) == 1 ) {
					cout << "IMPOSSIBLE" << endl;
					return;
				}
			}
		}
	cout<< ans << endl;
}

int main() { 
	int t; cin >> t; 
	for( int i = 1 ; i <= t ; i++ ) {
		cout << "Case #" << i << ": ";
		solve();
	}
}


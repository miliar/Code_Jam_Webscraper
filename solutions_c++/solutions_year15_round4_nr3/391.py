//In the name of Allah    
#include <bits/stdc++.h>    
using namespace std;    

#define __sz(x) ((int)(x).size())    
typedef long long ll;    
const int maxN = 3000*10 + 100; 

int cnt ; 
int nex[maxN][26];
bitset<3000> is[2];
map<int,int> to;
vector<string> a[300];
vector<int> b[300];

void solve() { 
	memset( nex , -1 , sizeof nex ) ; 
	fill( a , a + 300 , vector<string>());
	fill( b , b + 300 , vector<int>());
	cnt = 1; 
	int n; 
	cin >> n; 
	string s; getline( cin , s ) ; 
	
	for( int i = 0 ; i < n ; i++ ) {
		getline( cin , s ) ; 
		stringstream ss; ss << s; 
		string t;
		while( ss >> t ) 
			a[i].push_back( t ) ; 
	}
	to.clear();
	int toc = 1 ;
	for( int i = 0 ; i < n ; i++ ) for( auto s : a[i] ) {
		int curr = 0; 
		for( auto x : s ) {
			if( nex[curr][x-'a'] == -1 ) 
				nex[curr][x-'a'] = cnt++;
			curr = nex[curr][x-'a'];
		}
		if( to[curr] == 0 ) 
			to[curr] = toc++;
		b[i].push_back( to[curr] ) ; 
	}
	int ans = 100000;
	for( int i = 2 ; i < (1<<n) ; i += 4 ) {
		is[0] = is[1] = 0;
		for( int j = 0 ; j < n; j++ ) 
			for( auto s : b[j] )
				is[(i>>j)&1][s] = 1;
			
		ans = min(ans,(int)(is[0]&is[1]).count());
	}
	cout << ans << endl;
}

int main() { 
	int t; 
	cin >> t;
	for( int i = 1 ; i <= t ; i++) { 
		cerr << i << endl;
		cout << "Case #" << i << ": " ;
		solve(); 
	}
}

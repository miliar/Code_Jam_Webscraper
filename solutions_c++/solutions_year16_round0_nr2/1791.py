#include <bits/stdc++.h>
#include <tr1/unordered_map>

using namespace std;
using namespace tr1;

typedef long long int64;
typedef unsigned long long uint64;

char inv[500];

int main(){
	ios::sync_with_stdio(false);
	int t,  k = 1;
	inv['-'] = '+';
	inv['+'] = '-';
	cin >> t;
	string str;
	while( t-- ){
		cin >> str;
		int ans = 0;
		while( true ){
			int pos = -1;
			for( int i = 0; i < str.size(); i++ ){
				if( str[i] == '-' ) pos = i;
			}
			if( pos == -1 ) break;
			for( int i = 0; i <= pos; i++ ){
				str[i] = inv[str[i]];
			}
			ans++;
		}
		cout << "Case #" << k++ << ": " << ans << "\n";
	}
	return 0;
}
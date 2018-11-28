#include <bits/stdc++.h>
#include <tr1/unordered_map>

using namespace std;
using namespace tr1;

typedef long long int64;
typedef unsigned long long uint64;

int main(){
	ios::sync_with_stdio(false);
	int t, k = 1;
	cin >> t;
	while( t-- ){
		string str;
		cin >> str;
		string aux = "";
		for( int i = 0; i < str.size(); i++ ){
			if( !i ) aux += str[i];
			else{
				if( str[i] >= aux[0] ){
					string tt = "";
					tt += str[i];
					tt += aux;
					aux = tt;
				}
				else aux += str[i];
			}
		}
		cout << "Case #" << k++ << ": " << aux << '\n';
	}
	return 0;
}
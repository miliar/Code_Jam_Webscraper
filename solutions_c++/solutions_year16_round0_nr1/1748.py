#include <bits/stdc++.h>
#include <tr1/unordered_map>

using namespace std;
using namespace tr1;

typedef long long int64;
typedef unsigned long long uint64;

int main(){
	ios::sync_with_stdio(false);
	int t,  k = 1;

	cin >> t;
	long long q = 2, n;
	while( t-- ){
		cin >> n;
		unordered_map < int, int > mapa, used;

		char str[10000];
		sprintf(str, "%ld", n);
		for( int i = 0; i < strlen(str); i++ ){
			mapa[str[i]-'0']++;
		}
		q = 2;
		while(mapa.size() < 10 && !used.count(n*q)){
			used[n*q]++;
			sprintf(str, "%ld", (n*q));
			for( int i = 0; i < strlen(str); i++ ){
				mapa[str[i]-'0']++;
			}
			q++;
		}
		if( mapa.size() != 10 ) cout << "Case #" << k++ << ": INSOMNIA\n";
		else cout << "Case #" << k++ << ": " << n*(q-1) << '\n';
	}
	return 0;
}
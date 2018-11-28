#include <bits/stdc++.h>

using namespace std;

int T, N, nCase;

int solve(){
	int goal = (1 << 10) - 1;
	int cur = 0;
	int ans = 0;
	int aux;
	while( cur != goal ){
		ans += N;
		aux = ans;
		while( aux ){
			cur = cur | (1 << (aux % 10));
			aux /= 10;
		}
	}
	return ans;
}

int main(){

	cin >> T;

	while( T-- ){
		cin >> N;
		if( N == 0 ) cout << "Case #" << ++nCase << ": INSOMNIA\n";
		else cout << "Case #" << ++nCase << ": " << solve() << endl;
	}

	return 0;
}
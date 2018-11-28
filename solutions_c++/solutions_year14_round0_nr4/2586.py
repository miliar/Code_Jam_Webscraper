#include<iostream>
#include<algorithm>
#include<cmath>
#include<vector>
using namespace std;

int main() {
	float na[1003], ke[1003];
	float a;
	int t, T, i, j, n;
	int ansdw, answ;
	int kw, nw, kl, nl;
	cin >> T;
	for( t = 1; t <= T; ++t ) {
		cin >> n;
		na[0] = ke[0] = 0;
		for( i = 1; i <= n; ++i ) cin >> na[i];
		for( i = 1; i <= n; ++i ) cin >> ke[i];
		sort( na, na+n+1 );
		sort( ke, ke+n+1 );
		
		kw = n; kl = 0;
		for( nw = n; nw > 0; --nw ) {
			if( na[nw] > ke[kw] ) ++kl;
			else --kw;
		}
		answ = kl;
		
		nw = n; nl = 0;
		for( kw = n; kw > 0; --kw ) {
			if( ke[kw] > na[nw] ) ++nl;
			else --nw;
		}
		ansdw = n - nl;
		
		cout << "Case #" << t << ": " << ansdw << " " << answ << endl;
	}
	return 0;
}


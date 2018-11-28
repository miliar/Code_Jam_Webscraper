//In the name of Allah    
#include <bits/stdc++.h>    
using namespace std;    

#define __sz(x) ((int)(x).size())    
typedef long long ll;    
typedef long double ld;
const ld eps = 1e-15;

void solve() { 
	int n;
	cin >> n;
	ld v,x,r1,c1,r2,c2;
	cin >> v >> x >> r1 >> c1;
	if( n == 1 ) { 
		ld t = v / r1; 
		if( abs( x - c1 ) < eps ) 
			cout << t << endl;
		else
			cout << "IMPOSSIBLE" << endl;
		return;
	}
	cin >> r2 >> c2; 
	if( abs(c1-c2) < eps ) { 
		if( abs(c1-x) > eps ) 
			cout << "IMPOSSIBLE" << endl;
		else
			cout << v / (r1 + r2) << endl;
		return;
	}
	ld t1 = v * ( x - c2 ) / ( r1 * (c1 - c2) ) ; 
	ld t2 = ( v - t1 * r1 ) / r2 ; 
//	cerr << t1 << ' ' << t2 << endl;
	if( t1 < -eps || t2 < -eps ) 
		cout << "IMPOSSIBLE" << endl;
	else
		cout << max(t1,t2) << endl;
}

int main() { 
	cout << fixed << setprecision(9);
	int t; 
	cin >> t; 
	for( int i = 1 ; i <= t ; i++ ) { 
		cout << "Case #" << i << ": " ; 
		solve(); 
	}
}

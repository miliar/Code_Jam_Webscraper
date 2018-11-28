#include <cstdio>
#include <iostream>
using namespace std;

int tab[105];
int tests, x, n;
string ciag;

int main() {
	ios_base::sync_with_stdio(0);
	
	cin >> tests;
	for(int t = 1; t<=tests; t++) {
		
		cin >> ciag;
		n = ciag.length();
		for(int i = 1; i<=n; i++) {
			if(ciag[i-1] == '+') tab[i] = 1;
			else tab[i] = 0;
		}
		
		x = 0;
		for(int i = n; i >= 1; i--) {
			if((x+tab[i])%2 == 0) x++;
		}
		
		cout << "Case #" << t << ": " << x << "\n";	
	}
	
	return 0;
}

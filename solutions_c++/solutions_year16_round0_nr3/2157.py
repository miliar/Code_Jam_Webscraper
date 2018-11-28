#include <cstdio>
#include <iostream>
using namespace std;

long long int tab[16];
long long int pow[11][16];
long long int tests, x, n;

long long int policz(long long int a) {
	long long int liczba = 0;
	for(long long int g = 0; g <= 15; g++) {
		if(tab[g] == 1) liczba += pow[a][15-g];
	}
	for(long long int g = 2; g <= 10; g++) {
		if(liczba % g == 0) return g;
	}
	return 0;
}


int main() {
	ios_base::sync_with_stdio(0);
	
	for(int i = 2; i <= 10; i++) {
		pow[i][0] = 1;
		for(int j = 1; j <= 15; j++) {
			pow[i][j] = pow[i][j-1] * i;
		}
	}
	
	
	cin >> tests;
	for(int t = 1; t<=tests; t++) {
		cin >> n >> x;
		cout << "Case #" << t << ":\n";	
		
		tab[0] = 1;
		tab[15] = 1;
		for(int i = 1; i <= x; i++) {
			tab[15]++;
			for(int j = 15; j >= 1; j--) {
				if(tab[j] == 2) {
					tab[j] = 0;
					tab[j-1]++;
				}
			}
			tab[15]++;
			
			int ok = 1;
			for(int b = 2; b <= 10; b++) {
				int dziel = policz(b);
				if(dziel == 0) ok = 0;
			}
			
			
			if(ok)
			{
				for(int b = 0; b <= 15; b++) cout << tab[b]; 
				for(int b = 0; b <= 15; b++) cout << tab[b]; 
				cout << " ";
				for(int b = 2; b <= 10; b++) {
					int dziel = policz(b);
					cout << dziel << " ";
				}
				cout << endl;
			}
			else i--;
		}
	}
	
	return 0;
}

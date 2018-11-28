#include <cstdio>
#include <iostream>
using namespace std;

int tab[10];
long long int tests, n, suma;

void update(int a) {
	while(a > 0) {
		int b = a%10;
		if(tab[b] == 0) {
			tab[b] = 1;
			suma++;
		}
		a/=10;
	}
}

int main() {
	ios_base::sync_with_stdio(0);
	
	cin >> tests;
	for(int t = 1; t<=tests; t++) {
		cin >> n;
		
		
		cout << "Case #" << t << ": ";
		if(n == 0) cout << "INSOMNIA\n";
		else {
			for(int i = 0; i <= 9; i++) tab[i] = 0;
			suma = 0;
			for(long long int i = 1; i <= 100; i++) {
				update(i*n);
				if(suma == 10) {
					cout << i*n << endl; 
					break;
				}
			}
		}
		
	}
	
	return 0;
}

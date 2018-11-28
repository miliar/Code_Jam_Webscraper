#include <iostream>
#include <cstdio>
using namespace std;

bool digitos[10];

int actualizarDigitos(int num) {
	while(num > 0) {
		digitos[num%10] = true;
		num /= 10;
	}
	
	int result = 0;
	for (int i = 0; i < 10; i++)
		result += (int) digitos[i];
	return result;
}
int main () {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	
	int T;
	cin >> T;
	for (int tc = 1; tc <= T; tc++) {
		int N;
		cin >> N;
		
		if (N == 0) {
			cout << "Case #" << tc << ": INSOMNIA" << endl;
			continue;
		}
		
		for (int i = 0; i < 10; i++)
			digitos[i] = false;
			
		int cantDigitos = 0, i = 0;
		for (i = 0; cantDigitos < 10; i++) {
			cantDigitos = actualizarDigitos(i*N);
		}
		
		cout << "Case #" << tc << ": " << (i-1) * N << endl;
	}
	return 0;
}

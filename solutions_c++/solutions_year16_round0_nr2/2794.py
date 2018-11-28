#include <cstdint>
#include <iostream>
#include <string>
#include <cstdlib>
using namespace std;

void virar(bool panquecas[], int u) {
	for (int i = 0; i <= u; ++i)
		panquecas[i] = !panquecas[i];
}

void resolver(bool panquecas[], int tam) {
	int u = tam-1;
	int n = 0;

	while (u >= 0 && panquecas[u]) --u;

	while(u >= 0) {
		++n;
		virar(panquecas, u);

		while (u >= 0 && panquecas[u]) --u;
	}
	cout << n << "\n";
}

int main () {
	string P;
	int T, tam;
	bool panquecas[100];
	cin >> T;
	for (int i = 1; i <= T; ++i) {
		cin >> P;
		tam = P.length();
		for (int i = 0; i < tam; ++i) {
			panquecas[i] = P[i] == '+' ? true : false;
		}
		cout << "Case #" << i << ": ";
		resolver(panquecas, tam);
	}
}
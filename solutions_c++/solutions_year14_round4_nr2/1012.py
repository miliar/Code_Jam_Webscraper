#include <iostream>
#include <algorithm> 

using namespace std;

int main(void){
	int T;
	cin >> T;
	for (int k = 0; k < T; ++k){
		int N;
		cin >> N;
		vector<int> vet(N);
		for (int i = 0; i < N; ++i){
			cin >> vet[i];
		}
		if (N <= 2){
			cout << "Case #" << k+1 << ": " << 0 << endl;
			continue;
		}
		int ini = 0;
		int fim = N;
		int cont = 0;
		while (ini < fim){
			int min = vet[ini];
			int p = ini;
			for (int i = ini+1; i < fim; ++i){
				if (vet[i] < min) {
					min = vet[i];
					p = i;
				}
			}
			if (p - ini < fim - p - 1){
				for (int i = p-1; i >= ini; --i){
					vet[i] ^= vet[i+1];
					vet[i+1] ^= vet[i];
					vet[i] ^= vet[i+1];
				}
				cont += p-ini;
				ini++;
			} else {
				for (int i = p; i < fim-1; ++i){
					vet[i] ^= vet[i+1];
					vet[i+1] ^= vet[i];
					vet[i] ^= vet[i+1];
				}
				cont += fim - p - 1;
				fim--;
			}
		}
		cout << "Case #" << k+1 << ": " << cont << endl;
	}
	return 0;
}

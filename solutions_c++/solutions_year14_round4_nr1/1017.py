#include <iostream>
#include <algorithm> 

using namespace std;

int main(void){
	int T;
	cin >> T;
	for (int k = 0; k < T; ++k){
		int N, X;
		cin >> N >> X;
		vector<int> vet(N);
		for (int i = 0; i < N; ++i){
			cin >> vet[i];
		}
		sort(vet.begin(), vet.end());
		int j = 0;
		int cont = 0;
		for (int i = N-1; i >= j; --i){
			if (vet[i] + vet[j] <= X) j++;
			cont++;
		}
		cout << "Case #" << k+1 << ": " << cont <<endl;
	}
	return 0;
}

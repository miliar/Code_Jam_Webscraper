#include <iostream>
#include <cstring>

using namespace std;

int main () {

	ios::sync_with_stdio(0);

	int A, B, K;
	int T;
	int N;
	int cont;

	cin >> T;

	for (int z = 0; z < T; z++) {

		cin >> A >> B >> K;

		cont = 0;

		for (int i = 0; i < A; i++) {
			for (int j = 0; j < B; j++) {
				
				N = (i & j);
			//	cout << i << " " << j << " " << N << '\n';
				if (N < K)
					cont++;
			}
		}

		cout << "Case #" << z + 1 << ": " << cont << '\n';

	}

	return 0;
}
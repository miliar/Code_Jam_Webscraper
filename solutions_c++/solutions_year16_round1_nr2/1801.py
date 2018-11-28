#include <iostream>
#include <cstdio>
using namespace std;

int main () {
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	
	int apariciones[2502];
	int T, N, num;
	cin >> T;
	
	for (int t = 1; t <= T; t++) {
		cin >> N;

		for (int i = 0; i <= 2500; i++) {
			apariciones[i] = 0;
		}
	
		for (int i = 1; i <= 2 * N - 1; i++) {
			for (int j = 0; j < N; j++) {
				cin >> num;
				apariciones[num]++;
			}
		}
		
		cout << "Case #" << t << ":";
		for (int i = 1; i <= 2500; i++) {
			if (apariciones[i] % 2 == 1)
				cout << " " << i;
		}
		cout << endl;
	}
}

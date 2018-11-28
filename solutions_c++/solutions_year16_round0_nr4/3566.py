#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cmath>

using namespace std;

//	This logic will work when S == K
int main() {
	int T, K, C, S;
	cin >> T;

	for(int t=0; t<T; t++) {
		cin >> K >> C >> S;

		cout << "Case #" << (t+1) << ": ";
		for(int i=0; i<K; i++) {
			cout << (i+1) << " ";
		}
		cout << endl;
	}

	return 0;
}

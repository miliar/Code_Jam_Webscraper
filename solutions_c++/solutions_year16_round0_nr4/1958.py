#include <iostream>
#include <cassert>
using namespace std;

int main() {
	int T;
	cin >> T;
	for(int t = 0; t < T; t++) {
		int K, C, S;
		cin >> K >> C >> S;
		assert(K==S);
		cout << "Case #" << t+1 << ":";
		for(int i = 0; i < K; i++) {
			cout << " " << i+1;
		}
		cout << endl;
	}
}

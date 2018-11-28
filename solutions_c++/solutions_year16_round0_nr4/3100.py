#include <iostream>
using namespace std;

int main() {
	int T,K,C,S;
	cin >> T;
	for(int i = 0; i < T; i++) {
		cin >> K;
		cin >> C;
		cin >> S;
		cout << "Case #" << i+1 << ":";
		for(int j = 1; j <= K; j++) {
			cout << " " << j;
		}
		cout << endl;
	}
	return 0;
}
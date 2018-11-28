#include <iostream>
#include <string>
using namespace std;

int main() {
	int T;
	cin >> T;
	char b = cin.get();
	for (int i = 0; i < T; i++) {
		char *S = new char[1000];
		char c = 'Z';
		for (int j = 0; (c != '\0') && (c != '\n'); j++) {
			c = cin.get();
			if (c < S[0]) {
				S[j] = c;
			}
			else {
				for (int k = j; k >= 0; k--) {
					S[k] = S[k-1];
				}
				S[0] = c;
			}
		}
		cout << "Case #" << i+1 << ": " << S;


	} 



	return 0;
}

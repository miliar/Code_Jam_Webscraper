#include <iostream>
using namespace std;

int main(void) {
	int numCases;
	
	cin >> numCases;
	for (int numCase = 1; numCase <= numCases; numCase++) {
		int A, B, K;
		int result = 0;
		
		cin >> A >> B >> K;
		
		for (int i = 0; i < A; i++) {
			for (int j = 0; j < B; j++) {
				if ((i & j) < K) result++;
			}
		}
		
		cout << "Case #" << numCase << ": " << result << endl;
	}
}

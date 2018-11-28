#include <stdio.h>

#include <iostream>
using namespace std;

int main() {
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int T;
	unsigned long A = 0;
	unsigned long B = 0;
	unsigned long K = 0;
	cin >> T;
	int z;
	for (z = 0; z < T; z++) {
		cin >> A;
		cin >> B;
		cin >> K;
		unsigned long i, j;
		int count = 0;
		for (i = 0; i < A; i++)
		for (j = 0; j < B; j++) {
			if ((i&j) < K)
				count++;
		}
		cout << "Case #"<< z+1 << ": " << count << endl;
	}
	
	return 0;
}
#include <iostream>

using namespace std;

int main() {
	unsigned int A, B, K, T, k, temp;
	unsigned long long int count;
	cin >> T;
	k = 1;
	while(T--) {
		count = 0;
		cin >> A >> B >> K;
		for(int i=0;i<A;i++) {
			for(int j=0;j<B;j++) {
				temp = i&j;
				if(temp < K)
					count++;
			}
		}
		cout << "Case #" << k <<": " << count << "\n";
		k++;
	}
	return 0;
}
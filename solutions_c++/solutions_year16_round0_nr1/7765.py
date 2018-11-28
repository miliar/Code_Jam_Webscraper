#include <iostream>
#include <fstream>
using namespace std;
int main() {

	int T = 0,N=0;
	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> N;
		cout << "Case #" << i + 1 << ": ";
		if (!N)
			cout << "INSOMNIA";
		else {
			int uniq = 10,orig = N;
			bool digits[10] = { 0 };
			int f = 1;
			while(true){
				int d = 1,n=N;
				while (n) {
					d = n % 10;
					n /= 10;
					if (!digits[d]) {
						uniq--;
						digits[d] = true;
					}
				}
				if (!uniq)
					break;
				f++;
				N = orig * f;
			}
			cout << N;
		}
		cout << endl;
	}
	return 0;
}
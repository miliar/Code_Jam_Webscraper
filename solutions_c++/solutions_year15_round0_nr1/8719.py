#include <iostream>
using namespace std;

int solve() {
	int sm, n = 0, sum = 0;
	cin >> sm;

	for(int i=0;i<=sm;i++) {
		if(i > sum) {
			n++;
			sum++;
		}

		char a;
		cin >> a;
		sum += (a - '0');
		
	}

	return n;
}

int main() {
	int T;
	cin >> T;
	for(int i=1;i<=T;i++) {
		cout << "Case #" << i << ": " << solve() << endl;
	}
}
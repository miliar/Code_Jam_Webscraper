#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

vector<long long> sf;
char num[32];
bool isPalin(long long n) {
	int i=0;
	while(n != 0) {
		num[i++] = n%10;
		n /= 10;
	}

	i--;
	for(int j=0; j<i; j++,i--) {
		if(num[i] != num[j]) {
			return false;
		}
	}

	return true;
}

void init() {
	sf.push_back(1);
	long long sq;
	for(long long i=2; i<10000001; i++) {
		if(isPalin(i)) {
			sq = i*i;
			if(isPalin(sq)) {
				sf.push_back(sq);
			}
		}
	}
}

long long solve_case() {
	long long A, B;
	cin >> A >> B;
	vector<long long>::iterator low, up;
	low = lower_bound (sf.begin(), sf.end(), A);
	up = upper_bound (sf.begin(), sf.end(), B);
	return (up-low);
}


int main() {
	init();

	int T;
	cin >> T;

	for(int i=1; i<=T; i++) {
		long long ans = solve_case();
		cout << "Case #" << i << ": " << ans << endl;
	}
}
#include <iostream>
#include <cmath>
using namespace std;

bool ispalindrome(long long num) {
	char s[20];
	const int n = sprintf(s, "%lld", num);
	for(int i = 0; i < n/2; i++)
		if(s[i] != s[n - i - 1])
			return false;
	return true;
}

#define M 10000001
// #define M 1001
unsigned table[M];

int main() {
	unsigned count = 0;
	for(long long i = 0; i <= M; i++) {
		bool is = ispalindrome(i) && ispalindrome(i*i);
		count += is;
		table[i] = count;
		// if(is)
		// 	cout << i << " -- " << table[i] << endl;
	}
	int T; cin >> T;
	for(int t = 1; t <= T; t++) {
		long double A, B; cin >> A >> B;
		int a = ceil(sqrt(A)) - 1, b = sqrt(B);
		// cout << "a " << a << " b " << b << endl;
		cout << "Case #" << t << ": " << table[b] - table[a] << "\n";
	}
}

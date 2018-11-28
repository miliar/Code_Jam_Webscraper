#include <iostream>
using namespace std;

long long gcd(long long a, long long b) {
  return b != 0 ? gcd(b, a % b) : a;
}

int main() {
	int T;
	cin >> T;
	
	for(int t = 1; t <= T; ++t) {
		cout << "Case #" << t << ": ";
	
		long long int P, Q;
		char trash;
		cin >> P >> trash >> Q;
		
		int ans = 0;
		bool flag = false;
		
		long long int a = gcd(P, Q);
		P /= a;
		Q /= a;
		
		int cnt = 0;
		for(int i = 0; i < 64; ++i) {
			if((Q >> i) & 1) cnt++;
		}
		
		if(cnt != 1) {
			cout << "impossible" << endl;
			continue;
		}
		
		int p;
		for(int i = 0; i < 64; ++i) {
			if((P >> i) & 1) p = i;
		}
		
		int q;
		for(int i = 0; i < 64; ++i) {
			if((Q >> i) & 1) q = i;
		}
	
		cout << q - p << endl;
	
	}
	return 0;
}
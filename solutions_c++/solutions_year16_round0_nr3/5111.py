#include <iostream>

using namespace std;
typedef long long int Z;

int main() {
	Z T;
	cin >> T;
	
	for(Z te = 0; te < T; ++te) {
		Z N, J;
		cin >> N >> J;
		
		cout << "Case #" << te + 1 << ":\n";
		for(Z j = 0; j < J; ++j) {
			Z x = 2 * j + 3;
			Z y = x;
			while(!(y & ((Z)1 << (N - 1)))) y <<= 1;
			y |= x;
			
			for(Z i = N - 1; i >= 0; --i) {
				cout << ((y >> i) & 1);
			}
			
			for(Z d = 2; d <= 10; ++d) {
				Z v = x;
				Z k = 1;
				Z gaa = 0;
				while(v) {
					if(v & 1) gaa += k;
					v >>= 1;
					k *= d;
				}
				cout << ' ' << gaa;
			}
			
			cout << '\n';
		}
	}
	
	return 0;
}

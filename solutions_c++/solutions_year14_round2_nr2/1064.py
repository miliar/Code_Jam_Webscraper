#include <iostream>
using namespace std;
typedef unsigned long long ull;
int T;
ull A, B, K, count;
int main() {
	ios_base::sync_with_stdio(false);
	cin >> T;
	for (int caso=1; caso<=T; caso++) {
		cout << "Case #" << caso << ": ";
		count = 0;
		cin >> A >> B >> K;
		for (ull a=0; a < A; a++)
			for (ull b=0; b<B; b++)
				count += ((ull)(a&b) < K);
					
			

		cout << count << "\n";
	}
}
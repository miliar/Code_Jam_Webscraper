#include <iostream>

using std::cin;
using std::cout;
using std::endl;

int main(){
	int N;
	cin >> N;
	for (int n = 1; n <= N; n++) {
		int sMax;
		char c;

		cin >> sMax;
		cin.get(c);
		
		int levels[sMax + 1];
		for (unsigned int i = 0; i < sMax + 1 && cin.get(c); ++i) {
		  	levels[i] = c - '0';
		}

		int ans = 0;
		int total = 0;
		for (unsigned int i = 0; i < sMax + 1; ++i) {
			if (total < i) {
				ans += i - total;
				total += i - total;
			}
			total += levels[i];
		}
		cout << "Case #" << n << ": " << ans << endl;
	}
	return 0;
}

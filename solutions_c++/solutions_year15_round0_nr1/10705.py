#include <iostream>
#include <vector>
using namespace std;

int main() {
	// your code goes here
	size_t N;
	cin >> N;

	for (size_t i=1; i<=N; ++i) {
		cin.ignore(256, '\n');
		size_t smax;
		cin >> smax;
		size_t up = 0, needed=0;
		size_t sc; char ch;
		cin.ignore(1, ' ');
		for (size_t j=0; j<=smax; ++j) {
			cin >> ch; sc = ch-'0';
			if (sc > 0) {
				if (up < j) {
					needed += j - up;
					up += needed;
				}
				up += sc;
			}
		}
		cout << "Case #" << i << ": " << needed << endl;
	}
	
	return 0;
}
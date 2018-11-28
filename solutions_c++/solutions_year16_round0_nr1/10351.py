#include <iostream>

using namespace std;

int main() {
	int T;
	cin >> T;
	for(int i=1; i<=T; ++i) {
		unsigned long long N;
		cin >> N;
		if (N == 0)
			cout << "Case #" << i << ": INSOMNIA" << endl;
		else
		{
			unsigned int seen = 0;
			unsigned long long temp;
			unsigned long long y = 0;
			while (seen != 1023) {
				y += N;
				temp = y;
				do {
					seen |= 1 << temp % 10;
					temp /= 10;
				} while (temp > 0);
			} 
			cout << "Case #" << i << ": " << y << endl;
		}
	}
}

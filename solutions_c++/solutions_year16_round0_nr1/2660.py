#include <iostream>
#include <bitset>
#include <cmath>

using namespace std;

#define ull unsigned long long

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	int T;
	cin >> T;
	for(int t = 1; t <= T; t++) {
		ull N;
		cin >> N;

		if(N == 0) {
			cout << "Case #" << t << ": INSOMNIA" << endl;
			continue;
		}

		ull num = N;
		bitset<10> numbers;
		do {
			ull n = num;
			while(n != 0) {
				int digit = n % 10;
				numbers[digit] = true;
				n /= 10;
			}
			if(!numbers.all()) {
				num += N;
			} else {
				break;
			}
		} while(true);

		cout << "Case #" << t << ": " << num << endl;
	}
}

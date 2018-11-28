#include <iostream>
using namespace std;

int main () {
	int turn;
	cin >> turn;

	for (int round = 1; round <= turn; ++ round) {
		int Smax = 0;
		cin >> Smax;
		
		int acc = 0;
		char tmp;
		int audi = 0;
		int add = 0;
		for (int i = 0; i < Smax + 1; ++i) {
			cin >> tmp;
			audi = tmp - '0';
			if (i > acc) {
				add += i - acc;
				audi += (i - acc);
			}
			acc += audi;
		}
		cout << "Case #" << round << ": " << add << endl;
	}

	return 0;
}

#include <iostream>

using namespace std;

int main()
{

	int tests;
	unsigned long long num, hold, temp;
	
	cin >> tests;
	
	for (int t = 1; t <= tests; ++t) {
		bool digs[10] = {0};
		cin >> num;
		for (unsigned long long i = 1; i < 100000; ++i) {
			hold = num * i;
			temp = hold;
			while (temp > 0) {
				int ind = temp % 10;
				digs[ind] = 1;
				temp /= 10;
			}
			bool test = true;
			for (int j = 0; j < 10; ++j) {
				if (digs[j] == 0) {
					test = false;
					break;
				}	
			}
			if (test == true) {
				cout << "Case #" << t << ": " << hold << endl;
				break;
			}
			if (i == 999) cout << "Case #" << t << ": INSOMNIA" << endl;
		}
		
	
	}
	
	return 0;

}

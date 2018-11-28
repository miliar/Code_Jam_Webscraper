#include <iostream>
using namespace std;

int main ()
{
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		int Smax, sol = 0, sum = 0;
		cin >> Smax;
		for (int j = 0; j <= Smax; j++) {
			if (sum < j) {
				sol += j - sum;
				sum = j;
			}
			char c;
			int n;
			cin >> c;
			n = c - '0';
			sum += n;
		}
		cout << "Case #" << i + 1 << ": " << sol << endl;
	}
	return 0;
}

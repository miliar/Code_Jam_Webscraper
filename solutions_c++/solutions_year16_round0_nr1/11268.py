#include <iostream>
#include <vector>
using namespace std;

vector<int> getDigits(long long int in) {
	int div = 10;
	vector<int> result;
	while (in != 0) {
		result.push_back(in % div);
		in /= div;
	}
	return result;
}

int main() {
	int noCases, n;
	cin >> noCases;
	for (int cs = 1; cs <= noCases; ++cs)
	{
		cin >> n;
		if (n == 0)		cout << "Case #" << cs << ": " << "INSOMNIA" << endl;
		else {
			int map = 0, i = 1;
			vector<int> digits;
			while (map != 1023) {
				digits = getDigits(n*i);
				for (int j = 0; j < digits.size(); j++) {
					map = map | (1 << (digits[j]));
				}
				++i;
			}
			cout << "Case #" << cs << ": " << n*(i - 1) << endl;
		}
	}
}
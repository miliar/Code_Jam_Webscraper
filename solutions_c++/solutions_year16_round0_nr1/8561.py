#include <iostream>
using namespace std;

int solve(int sheep)
{
	int value = 0;
	int i = 1;
	int base = sheep;
	int target = 0x3ff;
	while (value != target) {
		sheep = base * i;
		while (sheep) {
			value |= (1 << (sheep % 10));
			sheep /= 10;
		}
		i++;
	}
	return base * (i - 1);
}

int main() {
	int cases;
	int sheep;
	int i, res;
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	cin >> cases;
	for (i = 1; i <= cases; ++i) {
		cin >> sheep;
		cout << "Case #" << i << ": ";
		if (sheep == 0)
			cout << "INSOMNIA" << endl;
		else {
			res = solve(sheep);
			cout << res << endl;
		}
	}
	return 0;
}
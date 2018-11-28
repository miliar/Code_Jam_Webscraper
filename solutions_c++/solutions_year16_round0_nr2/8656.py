#include <iostream>
using namespace std;

int main() {
	int cases;
	char cakes[110];
	char current;
	int i, j, S, res;
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	cin >> cases;
	for (i = 1; i <= cases; ++i) {
		cin >> cakes;
		res = 0;
		cout << "Case #" << i << ": ";
		S = strlen(cakes);
		current = cakes[0];
		for (j = 0; j < S; j++) {
			if (current != cakes[j]) {
				res++;
				current = cakes[j];
			}
		}
		if (current != '+')
			res++;
		cout << res << endl;
	}
	return 0;
}
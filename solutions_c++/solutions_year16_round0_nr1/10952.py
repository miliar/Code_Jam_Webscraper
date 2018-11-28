#include <iostream>
#include <map>

using namespace std;

int main() {

	int tc, n, j, aux;

	cin >> tc;
	for (int i = 0; i < tc;) {
		map<int, bool> digits;
		cin >> n;
		cout << "Case #" << ++i;
		if (n == 0) {
			cout << ": INSOMNIA\n";
			continue;
		}

		j = 0;
		while (digits.size() < 10) {
			j++;
			aux = j*n;
			while (aux > 0) {
				digits[aux%10] = true;
				aux /= 10;
			}
		}

		cout << ": " << n*j << "\n";
	}

	return (0);
}
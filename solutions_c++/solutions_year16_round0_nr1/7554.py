#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int t, cnt, j;
long long n, num;
vector <bool> b;

int main() {
	freopen("A-large.in", "r", stdin); freopen("output.out", "w", stdout);
	cin >> t;

	for (int i = 1; i <= t; ++i) {

		cin >> n;
		if (n == 0) {
			cout << "Case #" << i << ": " << "INSOMNIA" << endl;
			continue;
		}

		b.clear();
		b.resize(10);
		cnt = 0;

		for (j = 1; true; ++j) {
			num = n * j;
			while (num > 0) {
				if (!b[num % 10]) {
					++cnt;
					b[num % 10] = true;
				}
				num /= 10;
			}
				if (cnt == 10)
					break;
		}

		cout << "Case #" << i << ": " << j * n << endl;
	}

    return 0;
}
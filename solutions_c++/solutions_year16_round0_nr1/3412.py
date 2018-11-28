#include <iostream>
#include <vector>

using namespace std;

void main() {

	FILE *str, *abc;
	freopen_s(&str, "input.txt", "r", stdin);
	freopen_s(&abc, "out.txt", "w", stdout);

	int t;
	cin >> t;

	for (int i = 0; i < t; i++) {
		long long n;
		cin >> n;

		if (!n) cout << "CASE #" << i + 1 << ": INSOMNIA" << endl;
		else {
			int nums = 0, p=1;
			vector<int> dig(10, 0);
			while (nums != 10) {
				long long x = n*p;
				while (x) {
					if (!dig[x % 10]) {
						dig[x % 10] = 1;
						nums++;
					}
					x /= 10;
				}
				p++;
			}
			cout << "CASE #" << i + 1 << ": " << n*(p-1) << endl;
		}
	}
	

}
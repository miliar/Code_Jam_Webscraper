#include <iostream>

using namespace std;

int main()
{
	int t = 0, n = 0, *ns = NULL, jn = 0, jn_bkup = 0, digit = 0, digits = 0x3ff;
	bool is_last = false;

	cin >> t;
	ns = new int[t];

	for (int i = 0; i < t; ++i) {
		cin >> ns[i];
	}

	for (int i = 0; i < t; ++i) {
		n = ns[i];

		cout << "Case #" << (i+1) << ": ";

		if (n == 0) {
			cout << "INSOMNIA" << endl;
			continue;
		}

		if (n < 0) {
			n = -n;
		}

		digits = 0x3ff;
		is_last = false;
		for (int j = 1; !is_last; ++j) {
			jn_bkup = jn = j * n;
			while (jn > 0) {
				digit = jn % 10;
				jn = jn / 10;
				digits = digits & (~(1 << digit));
				if (digits == 0) {
					cout << jn_bkup << endl;
					is_last = true;
					break;
				}
			}
		}
	}

	delete ns;

	return 0;
}

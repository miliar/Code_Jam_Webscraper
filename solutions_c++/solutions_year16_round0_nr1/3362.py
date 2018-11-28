#include <iostream>

using namespace std;

typedef std::bitset<10> bmask;

bmask mask_of(int i) {
	bmask r(0);
	do {
		r[i % 10] = 1;
		i /= 10;
	} while (i != 0);
	return r;
}

int main() {
	int t; cin >> t;

	bmask all("1111111111");

	for (int i = 0; i < t; ++i)
	{
		bmask mask(0);
		int n; cin >> n;

		if (n == 0) {
			cout << "Case #" << i+1 << ": " << "INSOMNIA" << endl;	
		} else {
			mask |= mask_of(n);

			int c = 1;

			while (mask != all) {
				c++;
				auto new_mask = mask_of(c * n);
				mask |= new_mask;
			}

			cout << "Case #" << i+1 << ": " << n*c << endl;	
		}
	}

	return 0;
}
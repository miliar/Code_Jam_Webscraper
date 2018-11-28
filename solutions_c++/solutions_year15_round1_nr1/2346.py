#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

int main() {
	int cases, num = 1;
	std::cin >> cases;

	while (num <= cases) {
		int n, t;
		std::cin >> n;
		std::vector<int> m;
		for (int i = 0; i < n; ++i) {
			std::cin >> t;
			m.push_back(t);
		}

		int i = 1;
		int y = 0;
		while (i < n) {
			if (m[i-1]-m[i] > 0)
				y += m[i-1]-m[i];
			++i;
		}

		int max = *std::max_element(m.begin(), m.end());
		int z = INT_MAX;
		for (int rate = max; rate >= 0; --rate) {
			int tz = 0;
			int remain = 0;
			for (int j = 0; j < n-1; ++j) {
				if (rate >= m[j]) {
					remain = 0;
					tz += m[j];
				} else {
					remain = m[j]-rate;
					if (remain > m[j+1])
						goto end;
					tz += rate;
				}
			}

			if (tz < z)
				z = tz;
		}

end:	std::cout << "Case #" << num << ": " << y << ' ' << z << std::endl;
		++num;
	}
}
#include <bits/stdc++.h>

int T, D;

std::map<std::vector<int>, int> c;

int f(std::vector<int> v, int d = 0) {
	if (d < 11) {
		std::sort(v.begin(), v.end());
		std::reverse(v.begin(), v.end());
		bool z = false;
		int t = 0;
		// for (int i = 0; i < d; ++i) {
		// 	std::cerr << "  ";
		// }
		for (int i : v) {
			// std::cerr << i << ' ';
			t = std::max(t, i);
			if (i > 0) z = true;
		}
		// std::cerr << '\n';
		if (z && c[v] == 0) {
			// Eat
			std::vector<int> r(v.begin(), v.end());
			for (int& i : r) {
				i = std::max(0, i - 1);
			}
			c[v] = f(r, d + 1) + 1;
			// Move
			if (t > 2 && v.size() < 10) {
				std::vector<int> w(v.begin(), v.end());
				w.push_back(0);
				for (int j = 2; j < w[0] - 1; ++j) {
					w[0] -= j;
					w.back() = j;
					c[v] = std::min(c[v], f(w, d + 1) + 1);
					w[0] += j;
				}
				// int m = 0;
				// for (int i = 1; i < (int)v.size(); ++i) {
				// 	if (v[i] > v[m]) {
				// 		m = i;
				// 	}
				// }
				// std::vector<int> w(v.begin(), v.end());
				// w.push_back(0);
				// for (int i = 1; i < v[m] - 1; ++i) {
				// 	w[m] -= i;
				// 	w.back() = i;
				// 	w[m] += i;
				// 	c[v] = std::min(c[v], f(w, d + 1) + 1);
				// }
				// auto m = std::max_element(w.begin(), w.end());
				// int n = *m - (*m / 2);
				// *m /= 2;
				// w.push_back(n);
				// c[v] = std::min(c[v], f(w, d + 1) + 1);
			}
		}
	}
	return c[v];
}

int main() {
	std::cin >> T;
	for (int i = 0; i < T; ++i) {
		std::cerr << "Case " << i << " ----------------------------\n";
		std::cin >> D;
		std::vector<int> v;
		for (int j = 0; j < D; ++j) {
			int p;
			std::cin >> p;
			v.push_back(p);
		}
		int x = f(v);
		std::cout << "Case #" << i + 1 << ": " << x << "\n";
	}
}
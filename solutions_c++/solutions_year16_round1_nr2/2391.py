#include <iostream>
#include <map>
#include <set>
#include <deque>
#include <vector>
#include <cmath>
#include <cassert>
#include <climits>

int main() { int cases; std::cin >> cases; std::cin.get(); // skip endline
	for (int n = 1; n <= cases; ++n) { std::cout << "Case #" << n << ":"; {
		int n; std::cin >> n;
		std::set<std::string> exists;
		std::multimap<int, std::set<int>> rows;
		for (int i = 0; i < 2*n - 1; ++i) {
			std::set<int> row;
			std::string exist;
			for (int k = 0; k < n; ++k) {
				int v; std::cin >> v;
				row.insert(v);
				// std::cout << " :" << v;
			}
			// std::cout << std::endl;
			rows.insert(std::make_pair(*row.begin(), row));
		}

		for (int i = 0; i < (int) pow(2,2*n-1); ++i) {
			int nrows = 0, ncols = 0;
			for (int k = 0; k < n*2-1; ++k)
				++(i & (1 << k) ? nrows : ncols);
			if (nrows - ncols < -1 || nrows - ncols > 1)
				continue;
			// std::cout << "XXX " << i << " " << nrows << " " << ncols << std::endl;

			std::vector<int> field;
			std::map<int,int> hasRows, hasCols;
			field.resize(n*n);
			for (int k = 0; k < n*n; ++k)
				field[k] = INT_MAX;

			bool failed = false;
			auto rowIt = rows.begin();
			for (int k = 0; k < 2*n-1; ++k, ++rowIt) {
				if (i & (1 << k)) { // rows
					// std::cout << "row" << std::endl;
					int pos = 0;
					while (pos < n && field[pos + 0*n] < *(rowIt->second.begin()))
						++pos;
					if (pos == n || hasRows[pos]) { //  || field[pos + 0*n] == *(rowIt->second.begin())) {
						// std::cout << "FAIL A1 : " << pos << " " << field[pos + 0*n]
						//           << " " << *(rowIt->second.begin()) << std::endl;
						failed = true;
						break;
					}
					hasRows[pos] = 1;
					// assert(field[pos + 0*n] == INT_MAX);
					int idx = pos;
					for (auto x : rowIt->second) {
						if (field[idx] != INT_MAX && field[idx] != x) {
							// std::cout << "FAIL A2 : " << idx << " " << field[idx] << std::endl;
							failed = true;
							break;
						}
						field[idx] = x;
						idx += n;
					}
					if (failed) break;
				} else { // columns
					// std::cout << "col" << std::endl;
					int pos = 0;
					while (pos < n && field[0 + pos*n] < *(rowIt->second.begin()))
						pos += 1;
					if (pos == n || hasCols[pos]) { //  || field[0 + pos*n] == *(rowIt->second.begin())) {
						// std::cout << "FAIL B1 : " << pos << " " << field[pos]
						//           << " " << *(rowIt->second.begin()) << std::endl;
						failed = true;
						break;
					}
					hasCols[pos] = 1;
					// assert(field[0 + pos*n] == INT_MAX || field[0 + pos*n] == );
					int idx = pos * n;
					for (auto x : rowIt->second) {
						if (field[idx] != INT_MAX && field[idx] != x) {
							// std::cout << "FAIL B2 : " << idx << " " << field[idx] << std::endl;
							failed = true;
							break;
						}
						field[idx] = x;
						idx += 1;
					}
					if (failed) break;
				}
			}

			if (failed) continue;

			if (hasCols.size() > hasRows.size()) {
				int sum = 0;
				for (auto x : hasRows)
					sum += x.first;
				int num = n * (n-1) / 2 - sum;
				for (int i = 0; i < n; ++i)
					std::cout << " " << field[num + i*n];
			} else {
				int sum = 0;
				for (auto x : hasCols)
					sum += x.first;
				int num = n * (n-1) / 2 - sum;
				for (int i = 0; i < n; ++i)
					std::cout << " " << field[i + num*n];
			}

			break;

			// std::cout << std::endl;
			// for (int x = 0; x < n; ++x) {
			// for (int y = 0; y < n; ++y) {
			// 	std::cout << "\t" << field[x + y * n];
			// } std::cout << std::endl; }
		}
	}	std::cout << std::endl; }
}

#include <iostream>
#include <vector>

typedef std::vector< std::vector<int> > Matrix;

int main() {

	int t;
	std::cin >> t;

	for (int iter = 0; iter < t; ++iter) {
		int n, m;
		std::cin >> n >> m;
		Matrix mat(n, std::vector<int>(m));
		Matrix g(n, std::vector<int>(m));

		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) {
				std::cin >> mat[i][j];
				g[i][j] = 100;
			}
		}

		int h = 0;
		for (int i = 0; i < n; ++i) {
			int cut = 0;
			for (int j = 0; j < m; ++j) {
				cut = std::max(cut, mat[i][j]);
			}
			for (int j = 0; j < m; ++j) {
				g[i][j] = std::min(g[i][j], cut);
			}
		}

		for (int j = 0; j < m; ++j) {
			int cut = 0;
			for (int i = 0; i < n; ++i) {
				cut = std::max(cut, mat[i][j]);
			}
			for (int i = 0; i < n; ++i) {
				g[i][j] = std::min(g[i][j], cut);
			}
		}

		bool ok = true;
		for (int i = 0; ok && i < n; ++i) {
			for (int j = 0; ok && j < m; ++j) {
				ok = g[i][j] == mat[i][j];
			}
		}

		std::cout << "Case #" << (iter+1) << ": " << (ok ? "YES" : "NO") << "\n";
	}

	return 0;
}

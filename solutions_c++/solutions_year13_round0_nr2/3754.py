#include <cstdio>
#include <vector>

bool canMow(std::vector<std::vector<int> > &lawn, int n, int m) {
	// Tell if we can mow the lawn
	std::vector<int> max_in_row(n, 0), max_in_col(m, 0);
	for (int i = 0; i < n; i++) {
		max_in_row[i] = lawn[i][0];
		for (int j = 1; j < m; j++) {
			if (lawn[i][j] > max_in_row[i]) {
				max_in_row[i] = lawn[i][j];
			}
		}
	}
	for (int j = 0; j < m; j++) {
		max_in_col[j] = lawn[0][j];
		for (int i = 1; i < n; i++) {
			if (lawn[i][j] > max_in_col[j]) {
				max_in_col[j] = lawn[i][j];
			}
		}
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (lawn[i][j] < max_in_row[i] && lawn[i][j] < max_in_col[j]) {
				return false;
			}
		}
	}
	return true;
}

int main() {
	int T, n, m;
	FILE *fin = fopen("B-large.in", "r");
	FILE *fout = fopen("output.txt", "w");
	std::vector<std::vector<int> > lawn;
	fscanf(fin, "%d", &T);
	for (int test_case = 0; test_case < T; test_case++) {
		fscanf(fin, "%d%d", &n, &m);
		lawn.resize(n);
		for (int i = 0; i < n; i++) {
			lawn[i].resize(m);
			for (int j = 0; j < m; j++) {
				fscanf(fin, "%d", &lawn[i][j]);
			}
		}

		fprintf(fout, "Case #%d: ", test_case + 1);
		if (canMow(lawn, n, m)) {
			fprintf(fout, "YES\n");
		} else {
			fprintf(fout, "NO\n");
		}
	}

	return 0;
}
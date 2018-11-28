#include <fstream>
#define MAX_SIZE 101
#define MIN 1
#define NON_MIN 2
#define UNCHECKED 3
using namespace std;

int lawn[MAX_SIZE][MAX_SIZE];
int n, m, second_min;

int row_type[MAX_SIZE], col_type[MAX_SIZE];

ifstream in("input_b.txt");
ofstream out("output_b.txt");

bool done() {
	int first = lawn[0][0];

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (lawn[i][j] != first) {
				return false;
			}
		}
	}
	return true;
}

bool check_row(int row) {
	if (row_type[row] == UNCHECKED) {
		int value = lawn[row][0];

		for (int j = 1; j < m; j++) {
			if (lawn[row][j] != value) {
				row_type[row] = NON_MIN;
				return false;
			}
		}
		row_type[row] = MIN;
		return true;
	}
	return row_type[row] == MIN;
}

bool check_col(int col) {
	if (col_type[col] == UNCHECKED) {
		int value = lawn[0][col];

		for (int i = 1; i < n; i++) {
			if (lawn[i][col] != value) {
				col_type[col] = NON_MIN;
				return false;
			}
		}
		col_type[col] = MIN;
		return true;
	}
	return col_type[col] == MIN;
}

bool get_lowest() {
	int min = second_min;
	second_min = 101;

	for (int i = 0; i < n; i++) {
		row_type[i] = UNCHECKED;
	}
	for (int j = 0; j < m; j++) {
		col_type[j] = UNCHECKED;
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (lawn[i][j] == min) {
				if (!check_row(i) && !check_col(j)) {
					return false;
				}
			}
			else if (lawn[i][j] < second_min) {
				second_min = lawn[i][j];
			}
		}
	}
	return true;
}

void grow_grass() {
	for (int i = 0; i < n; i++) {
		if (row_type[i] == MIN) {
			for (int j = 0; j < m; j++) {
				lawn[i][j] = second_min;
			}
		}
	}
	
	for (int j = 0; j < m; j++) {
		if (col_type[j] == MIN) {
			for (int i = 0; i < n; i++) {
				lawn[i][j] = second_min;
			}
		}
	}
}

bool compute() {
	second_min = 101;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (lawn[i][j] < second_min) {
				second_min = lawn[i][j];
			}
		}
	}

	while (!done()) {
		if (get_lowest()) {
			grow_grass();
		}
		else {
			return false;
		}
	}
	return true;
}

int main() {
	int t;
	in >> t;
	
	for (int i = 0; i < t; i++) {
		in >> n >> m;
		for (int j = 0; j < n; j++) {
			for (int k = 0; k < m; k++) {
				in >> lawn[j][k];
			}
		}
		out << "Case #" << (i + 1) << ": " << (compute() ? "YES" : "NO") << endl;
	}
	return 0;
}

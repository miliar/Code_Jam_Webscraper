#include <iostream>
#include <fstream>

const char* solvePuzzle(int N, int M, int* grid) {
	const char* yes = "YES";
	const char* no = "NO";

	std::cout << "Solve an " << N << "x" << M << " grid." << std::endl;

	// Iterate over all squares.
	for (int i = 0, j = 0; i < N && j < M; (j + 1 == M) ? j = 0, i++ : j++) {
		// Check that for each square, it is greater than or equal to all entries
		// in either its row or its column.
		int value = grid[M * i + j];

		// Row.
		bool valid = true;
		for (int k = 0; k < M; k++) {
			if (grid[M * i + k] > value) {
				valid = false;
			}
		}

		if (valid) continue;

		// Column.
		valid = true;
		for (int k = 0; k < N; k++) {
			if (grid[M * k + j] > value) {
				valid = false;
			}
		}

		if (valid) continue;

		// Otherwise invalid so impossible.
		return no;
	}

	// Gets here on success.
	return yes;
}

int main() {
	// Sorry for the lack of error checking.
	std::ifstream in("input.txt");
	std::ofstream out("output.txt");

	int num_tests;

	in >> num_tests;

	std::cout << num_tests << " test cases." << std::endl;

	for (int i = 0; i < num_tests; i++) {
		int M, N;
		in >> N >> M;
		int* data = new int[N * M];
		int* iter = data;
		for (int j = 0; j < N; j++) {
			for (int k = 0; k < M; k++) in >> iter[0], iter++;
		}
		const char* test = solvePuzzle(N, M, data);
		std::cout << "Case #" << (i + 1) << ": " << test << std::endl;
		out << "Case #" << (i + 1) << ": " << test << std::endl;
		delete[] data;
	}

	// All done.
	return 0;
}

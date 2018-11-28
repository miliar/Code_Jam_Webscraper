#include <iostream>

const short MAX_N = 100;
const short MAX_M = 100;
short N;
short M;
short board[MAX_N][MAX_M];

bool validColumn(const short& col, const short& val) {
	for (short i(0); i < N; i++)
		if (board[i][col] > val)
			return false;

	return true;
}

bool validLine(const short& line, const short& val) {
	for (short j(0); j < M; j++)
		if (board[line][j] > val)
			return false;

	return true;
}

bool runTest() {
	for (short i(0); i < N; i++)
		for (short j(0); j < M; j++)
			if (! (validLine(i, board[i][j]) || validColumn(j, board[i][j])))
				return false;

	return true;
}

/**
 * I have a column and line verifier
 * Start by position 0,0
 * For each position, validate if column and line are lower or equal
 */

int main() {
	short num_test;
	std::cin >> num_test;

	for (short test(0); test < num_test; test++) {
		std::cin >> N >> M;

		for (short i(0); i < N; i++)
			for (short j(0); j < M; j++)
				std::cin >> board[i][j];

		std::cout << "Case #" << (test + 1) << ": ";
		std::cout << (runTest() ? "YES" : "NO") << std::endl;
	}
}

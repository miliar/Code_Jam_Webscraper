
#include <iostream>

int main() {
	unsigned N;
	std::cin >> N;
	for (unsigned c = 1; c <= N; ++c) {
		unsigned R, C, M, F;
		bool swap = false, impossible = false;
		std::cin >> R >> C >> M;
		F = C * R - M;
		if (R > C) {
			std::swap(R, C);
			swap = true;
		}
		char board[R][C];
		for (unsigned r = 0; r < R; ++r)
			for (unsigned c = 0; c < C; ++c)
				board[r][c] = '*';
		if (F == 1)
			;
		else if (R == 1)
			for (unsigned i = 0; i < F; ++i)
				board[0][i] = '.';
		else if (R == 2) {
			if (F == 2 || M & 1)
				impossible = true;
			else
				for (unsigned i = 0; i < F / 2; ++i)
					board[0][i] = board[1][i] = '.';
		} else if (F < 4 || F == 5 || F == 7)
			impossible = true;
		else {
			unsigned remaining = F;
			for (unsigned i = 0; i < C && remaining >= 2 && remaining != 3; ++i) {
				board[0][i] = board[1][i] = '.';
				remaining -= 2;
			}
			if (remaining == 3) {
				board[2][0] = board[2][1] = board[2][2] = '.';
			} else {
				for (unsigned i = 2; i < R && remaining >= 2; ++i) {
					board[i][0] = board[i][1] = '.';
					remaining -= 2;
				}
				for (unsigned r = 2; r < R && remaining > 0; ++r)
					for (unsigned c = 2; c < C && remaining > 0; ++c) {
						board[r][c] = '.';
						--remaining;
					}
			}
		}
		board[0][0] = 'c';
		std::cout << "Case #" << c << ":" << std::endl;
		if (impossible)
			std::cout << "Impossible" << std::endl;
		else if (swap) {
			for (unsigned c = 0; c < C; ++c) {
				for (unsigned r = 0; r < R; ++r)
					std::cout << board[r][c];
				std::cout << std::endl;
			}
		} else {
			for (unsigned r = 0; r < R; ++r) {
				for (unsigned c = 0; c < C; ++c)
					std::cout << board[r][c];
				std::cout << std::endl;
			}
		}
	}
	return 0;
}

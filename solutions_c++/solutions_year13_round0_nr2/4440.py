#include <iostream>
#include <vector>

int main(int argc, char* argv[]) {

	bool done;
	unsigned int T, N, M, x;
	std::vector<unsigned int> max_col;
	std::vector<unsigned int> max_row;
	std::vector< std::vector<unsigned int> > lawn(100, std::vector<unsigned int>(100));
	
	std::cin >> T;

	for( unsigned int t = 0; t < T; t++ ) {
		std::cin >> N >> M;

		max_col.clear();
		max_col.resize(N);
		max_row.clear();
		max_row.resize(M);

		for( unsigned int c = 0; c < N; c++ ) {
			for( unsigned int r = 0; r < M; r++ ) {
				std::cin >> x;
				if(max_col[c] < x) max_col[c] = x;
				if(max_row[r] < x) max_row[r] = x;
				lawn[c][r] = x;
			}
		}

		std::cout << "Case #" << (t+1) << ": ";

		done = false;
		for( unsigned int c = 0; c < N && !done; c++ ) {
			for( unsigned int r = 0; r < M && !done; r++ ) {
				if(lawn[c][r] < max_col[c] && lawn[c][r] < max_row[r]) {
					std::cout << "NO" << std::endl;
					done = true;
				}
			}
		}

		if( !done ) std::cout << "YES" << std::endl;
	}

	return 0;
}
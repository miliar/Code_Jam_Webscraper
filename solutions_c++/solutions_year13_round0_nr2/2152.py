#include <iostream>
#include <vector>
using namespace std;

typedef unsigned int uint;
typedef vector<uint> vu;
typedef vector<vu> vvu;

bool is_largest_in_row(vvu const & lawn, uint row, uint column)
{
	uint N = lawn.size(), M = lawn[0].size();
	for (uint j = 0; j < M; ++j) {
		if (lawn[row][column] < lawn[row][j]) return false;
	}
	return true;
}

bool is_largest_in_column(vvu const & lawn, uint row, uint column)
{
	uint N = lawn.size(), M = lawn[0].size();
	for (uint i = 0; i < N; ++i) {
		if (lawn[row][column] < lawn[i][column]) return false;
	}
	return true;
}

bool solve(vvu const & lawn)
{
	uint N = lawn.size(), M = lawn[0].size();
	// for each pos, check that it is >= then the rest of the row or the rest of the column
	for (uint i = 0; i < N; ++i) {
		for (uint j = 0; j < M; ++j) {
			if (!is_largest_in_row(lawn, i, j) && !is_largest_in_column(lawn, i, j)) return false;
		}
	}
	return true;
}


int main()
{
	uint T;
	cin >> T;
	for (uint t = 0; t < T; ++t) {
		uint N, M;
		cin >> N >> M;
		vvu lawn(N, vu(M));
		for (uint i = 0; i < N; ++i) {
			for (uint j = 0; j < M; ++j) {
				cin >> lawn[i][j];
			}
		}
		cout << "Case #" << t+1 << ": " << (solve(lawn) ? "YES" : "NO") << endl;
	}
	return 0;
}

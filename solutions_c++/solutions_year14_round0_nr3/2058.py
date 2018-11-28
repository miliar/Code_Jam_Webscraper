#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
using namespace std;


void print_board(vector<vector<char>>& grid) 
{
	for (auto line : grid) {
		for (auto c : line) {
			cout << c;
		}
		cout << endl;
	}

	cout << endl;

}

vector<pair<int,int>> markFreeCells(vector<vector<char>>& grid, int pos_i, int pos_j)
{
	int max_i = grid.size()-1;
	int max_j = grid[0].size() - 1;
	vector<pair<int, int>> result{};

	for (int i = max(pos_i - 1, 0); i <= min(pos_i + 1, max_i); ++i) {
		for (int j = max(pos_j - 1, 0); j <= min(pos_j + 1, max_j); ++j) {
			if ((i != pos_i || j != pos_j) && grid[i][j] == '*') {
				grid[i][j] = '.';
				result.push_back(make_pair(i,j));
			}
		}
	}

	return result;
}

bool solveRecurse(vector<vector<char>>& grid, int m, int current_m, int pos_i, int pos_j)
{
	auto markedCells = markFreeCells(grid, pos_i, pos_j);
	current_m -= markedCells.size();

	//print_board(grid);

	if (current_m == m) return true;
	else if (current_m > m) {
		for (auto cell : markedCells) {
			if (solveRecurse(grid, m, current_m, cell.first, cell.second)) return true;
		}
	}

	for (auto cell : markedCells) {
		grid[cell.first][cell.second] = '*';
	}

	return false;
}

vector<vector<char>> solve(int r, int c, int m)
{
	vector<vector<char>> grid;
	for (int i = 0; i < r; ++i) {
		grid.push_back(vector<char>(c, '*'));
	}

	grid[r - 1][c - 1] = 'c';
	if (!solveRecurse(grid, m, r*c-1, r - 1, c - 1) && m != r*c-1) {
		return vector<vector<char>>{};
	}

	return grid;
}

void main()
{
	ifstream input_file("input.txt");
	ofstream output_file("output.txt");

	int nbCases;
	input_file >> nbCases;

	for (int i = 1; i <= nbCases; ++i) {

		int r;
		input_file >> r;

		int c;
		input_file >> c;

		int m;
		input_file >> m;

		output_file << "Case #" << i << ":" << endl;
		auto result = solve(r, c, m);
		if (result.empty()) {
			output_file << "Impossible" << endl;
		}
		else{
			for (auto line : solve(r, c, m)) {
				for (auto c : line) {
					output_file << c;
				}
				output_file << endl;
			}
		}

		//cout << "------------------------" << endl << endl;
		
	}

}
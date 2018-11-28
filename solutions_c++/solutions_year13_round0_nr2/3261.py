#include<iostream>
#include<fstream>
#include<vector>

using namespace std;

bool check_lawn(vector<vector<int> > grid) {
	int y_max, x_max;
	y_max = grid.size();
	x_max = grid[0].size();
	for(int y = 0; y < y_max; y++) {
		for(int x = 0; x < x_max; x++) {
			int height = grid[y][x];
			int save_x = x;
			for(; x >= 0; x--) {
				if(grid[y][x] > height) {
					int save_y = y;
					for(; y >= 0; y--) {
						if(grid[y][save_x] > height) {
							return false;
						}
					}
					y = save_y;
					for(; y < y_max; y++) {
						if(height < grid[y][save_x]) {
							return false;
						}
					}
					y = save_y;
				}
			}
			for(x = save_x; x < x_max; x++) {
				if(height < grid[y][x]) {
					int save_y = y;
					for(; y >= 0; y--) {
						if(grid[y][save_x] > height) {
							return false;
						}
					}
					y = save_y;
					for(; y < y_max; y++) {
						if(height < grid[y][save_x]) {
							return false;
						}
					}
					y = save_y;
				}
			}
			x = save_x;
		}
	}
	return true;
}

int main(int argc, char* argv[]) {
	if(argc != 3) {
		cout << "Please provide the input name followed by the output name\n";
	}
	int cases;
	vector<bool> results;
	ifstream file_in(argv[1]);
	ofstream file_out(argv[2]);
	file_in >> cases;
	for(int index = 0; index < cases; index++) {
		int y_max, x_max;
		file_in >> y_max;
		file_in >> x_max;
		vector<vector<int> > grid;
		for(int y = 0; y < y_max; y++) {
			vector<int> row;
			for(int x = 0; x < x_max; x++) {
				int value;
				file_in >> value;
				cout << value;
				row.push_back(value);
			}
			cout << "\n";
			grid.push_back(row);
		}
		results.push_back(check_lawn(grid));
		cout << results.back() << "\n";
	}
	for(int index = 0; index < cases; index++) {
		file_out << "Case #" << index + 1 << ": ";
		if(results[index]) {
			file_out << "YES\n";
		} else {
			file_out << "NO\n";
		}
	}
}


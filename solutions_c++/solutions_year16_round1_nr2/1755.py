#include <iostream>
#include <map>
#include <vector>
using namespace std;

vector<int> grid_find(vector<vector<int> > &grid, int row, int col)
{
	map <int, int> cache;
	map <int, int>::iterator it;

	vector<int> res;
	
	for (int ri=0; ri < row; ++ri) {
		for (int ci=0; ci < col; ++ci) {
			cache[grid[ri][ci]]++;
		}
	}
	for(it = cache.begin(); it != cache.end(); ++it) {
		if(it->second % 2 == 1) {
			res.push_back(it->first);
		}
	}
	return res;
}

int main()
{
	int tcase;
	int row, col;
	vector<vector<int> > grid;
	vector<int> res;

	cin >> tcase;

	for (int i=1; i<=tcase; ++i) {

		cin >> col;
		row = col * 2 - 1;
		grid.resize(row);

		for(int ri=0; ri < row; ++ri) {

			grid[ri].resize(col);
			for(int ci=0; ci < col; ++ci) {
				cin >> grid[ri][ci];
			}
		}
		res = grid_find(grid, row, col);
		cout << "Case #" << i << ":";
		for(int i=0; i<res.size(); ++i) {
			cout << ' ' << res[i];
		}
		cout << endl;
	}
	return 0;
}

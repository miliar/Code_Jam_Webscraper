// 2014.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <sstream>
#include <iterator>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <stdio.h>
#include <algorithm>
#include <deque>

using namespace std;

class Mine {
private:
	int R, C, M;
	vector<string> grid;
	map<string, bool> cache;
	set<pair<int, int> > all;	

public:
	Mine(int r, int c, int m) {R = r; C = c; M = m;grid = vector<string>(R, string(C, '*'));}
	Mine(){}
	string gridToString(const vector<string>& curGrid) {
		ostringstream oss;

		for (int i = 0; i < R; ++i)
			copy(curGrid.begin(), curGrid.end(), ostream_iterator<string>(oss,""));
		string str = oss.str();
		return str;
	}

	void pair2Grid(vector<string>& curGrid) {
		curGrid = vector<string>(R, string(C, '*'));
		for (set<pair<int, int> >::const_iterator iter = all.begin();
			iter != all.end(); ++iter){

			curGrid[iter->first][iter->second] = '.';
		}
	}

	void addToCache(const vector<string>& curGrid, bool flag) {
		vector<string> tmpG = curGrid;
		cache[gridToString(tmpG)] = flag;
		/*reverse(tmpG.begin(), tmpG.end());
		cache[gridToString(tmpG)] = flag;
		for (int i = 0; i < R; ++i)
			reverse(tmpG[i].begin(), tmpG[i].end());
		cache[gridToString(tmpG)] = flag;
		tmpG = curGrid;
		for (int i = 0; i < R; ++i)
			reverse(tmpG[i].begin(), tmpG[i].end());
		cache[gridToString(tmpG)] = flag;*/
	}
	void parseData() {
		string line;
		
		cin >> R >> C >> M;
		getline(cin, line);
		grid = vector<string>(R, string(C, '*'));
	}

	void mineCount(vector<string>& curGrid, vector<vector<int>>& count) {
		for (int i = 0; i < R; ++i) {
			for (int j = 0; j < C; ++j) {
				if (curGrid[i][j] == '*') {
					for (int h = -1; h < 2; ++h) {
						for (int v = -1; v < 2; ++v) {
							if (i + h >= 0 && i + h < R && j + v >= 0 && j + v < C) ++count[i + h][j + v];
						}
					}
				}
			}
		}
	}

	void openGrid(vector<string>& curGrid, int i, int j, vector<pair<int, int> >& frontierList) {
		for (int h = -1; h <= 1; ++h) {
			for (int v = -1; v <= 1; ++v) {
				if (h == 0 && v == 0) continue;
				if ( h + i < 0 || h + i >= R || v + j < 0 || v + j >= C) continue;
				if (all.find(make_pair(h + i, v + j)) == all.end()) {
					frontierList.push_back(make_pair(h + i, v + j));
					all.insert(make_pair(h + i, v + j));
				}
			}
		}
	}
	
	bool solveRec(vector<string> curGrid, int i, int j, const vector<pair<int, int> >& frontierList) {
		if (i == 2 && j == 2) {
			int x = 1;
		}
		if (all.size() + M == R * C) return true;
		pair2Grid(curGrid);
		string cacheLine = gridToString(curGrid);
		if (cache.find(cacheLine) != cache.end()) return cache[cacheLine];

		vector<pair<int, int> > tmpFrontierList;
		openGrid(curGrid, i, j, tmpFrontierList);
		vector<pair<int, int>> alllist;
		copy(tmpFrontierList.begin(), tmpFrontierList.end(),back_inserter<vector<pair<int,int> >>(alllist));
		copy(frontierList.begin(), frontierList.end(),back_inserter<vector<pair<int,int> >>(alllist));
		if (all.size() + M == R * C) return true;
		else if (all.size() + M < R * C){			
			for (vector<pair<int,int>>::iterator iter = alllist.begin(); iter != alllist.end(); ++iter) {
				vector<pair<int, int>> thisList;
				vector<pair<int, int>>::iterator curIter = iter; 
				++curIter;
				copy(curIter, alllist.end(), back_inserter<vector<pair<int, int>>>(thisList));
				if (solveRec(curGrid, iter->first, iter->second, thisList)) return true;
			}
		}
		for(vector<pair<int,int>>::const_iterator iter = tmpFrontierList.begin(); iter != tmpFrontierList.end(); ++iter) 
				all.erase(*iter);
		addToCache(curGrid, false);
		return false;
	}

	void solve() {
		int ci = -1;
		int cj = -1;
		if (M == 0) {
			vector<string> curGrid(R, string(C, '.'));
			curGrid[0][0] = 'c';
			copy(curGrid.begin(), curGrid.end(), ostream_iterator<string>(cout, "\n"));
			return;
		}
		for (int i = 0; i < R; ++i) {
			for (int j = 0; j < C; ++j) {
				vector<string> curGrid = grid;
				all.insert(make_pair(i, j));
				vector<pair<int, int> > frontierList;
				if (solveRec(curGrid, i, j, frontierList)) {
					ci = i; cj = j;
					break;
				}
				all.erase(make_pair(i, j));
			}
			if (ci != -1) break;
		}
		if (ci == -1)
			cout << "Impossible" << endl;
		else {
			pair2Grid(grid);
			grid[ci][cj] = 'c';
			copy(grid.begin(), grid.end(), ostream_iterator<string>(cout, "\n"));
		}
	}

};

int main(int argc, char* argv[])
{	
	string line;
	int count;

	cin >> count;
	getline(cin, line);

	/*int c = 0;
	for (int i = 4; i <= 4; ++i) {
		for (int j = 4; j <= 4; ++j) {
			for (int k = 0; k < i * j; ++k) {
				Mine mn(i, j, k);
				cout << "Case #" << ++c << ": (" << i << "," << j << "," << k <<"): " << endl;
				mn.solve();
			}
		}
	}*/
	
	for (int i = 1; i <= count; ++i) {
		Mine mn;
		mn.parseData(); 
		cout << "Case #" << i << ": " << endl;
		mn.solve();
	}
	
	return 0;
}


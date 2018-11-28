#include <iostream>
#include <vector>
using namespace std;

class Solver {
	const vector<vector<int> >& data;
	vector<int> rows;
	vector<int> cols;
	int smallest;

	enum {BIG = 1000};

	void erase_row(int i)  {
		rows.erase(rows.begin() + i);
		smallest = BIG;
	}

	void erase_col(int i) {
		cols.erase(cols.begin() + i);
		smallest = BIG;
	}

	int scan_row(int i) {
		int row = rows[i],
			rowHeight = data[row][cols[0]];
		for (int j=0; j<cols.size(); j++) {
			int col = cols[j];
			smallest = min(smallest, data[row][col]);
			if (data[row][col] != rowHeight) {
				return BIG;
			}
		}
		return rowHeight;
	}

	int scan_col(int i) {
		int col = cols[i],
			colHeight = data[rows[0]][col];
		for (int j=0; j<rows.size(); j++) {
			int row = rows[j];
			smallest = min(smallest, data[row][col]);
			if (data[row][col] != colHeight) {
				return BIG;
			}
		}
		return colHeight;
	}
public:
	Solver(const vector<vector<int> >&a) 
		: data(a), rows(a.size()), cols(a[0].size()), smallest(BIG)
	{
		for (int i=0; i<rows.size(); i++)
			rows[i] = i;
		for (int i=0; i<cols.size(); i++)
			cols[i] = i;
	}

	string solve() {
		while (!rows.empty() && !cols.empty()) {
			int smallestRowHeight = BIG,
				smallestRow = BIG;

			for (int i=0; i<rows.size(); i++) {
				int rowHeight = scan_row(i);
				if (rowHeight < smallestRowHeight) {
					smallestRow = i;
					smallestRowHeight = rowHeight;
				}
			}

			int smallestColHeight = BIG,
				smallestCol = BIG;

			for (int i=0; i<cols.size(); i++) {
				int colHeight = scan_col(i);
				if (colHeight < smallestColHeight) {
					smallestCol = i;
					smallestColHeight = colHeight;
				}
			}

			if (smallestColHeight == smallest) {
				erase_col(smallestCol);
			} else if (smallestRowHeight == smallest) {
				erase_row(smallestRow);
			} else {
				return "NO";
			}
		}
		return "YES";
	}
};

int main()  {
	int T;
	cin >> T;
	for (int t=1; t<=T; t++) {
		int n, m;
		cin >> n >> m;
		vector<vector<int> > data(n, vector<int>(m));
		for (int i=0; i<n; i++) {
			for (int j=0; j<m; j++) {
				cin >> data[i][j];
			}
		}
		Solver s(data);
		cout << "Case #" << t << ": " << s.solve().data() << endl;
	}
	return 0;
}
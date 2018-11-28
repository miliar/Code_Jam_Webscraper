#include <algorithm>
#include <iostream>
#include <iterator>
#include <string>
#include <vector>
#include <set>
using namespace std;

struct Input {
	char x[100][100];
	vector<char> h;
	int max;
	int n, m;
	string solve() {
		prep();
		int i;
		for (i=0; i<h.size()-1;i++) {
			if (!ok(h[i], h[i+1])) {
				return "NO";
			}
		}
		return "YES";	
	}
	bool ok(int d, int nd) {
		int r,c;
		vector<int> rows, cols;
		// row
		for (r=0;r<n;r++) {
			for (c=0;c<m;c++) {
				if (x[r][c] != d) {
					break;
				}
			}
			if (c==m) {
				rows.push_back(r);
			}
		}
		// col
		for (c=0;c<m;c++) {
			for (r=0;r<n;r++) {
				if (x[r][c] != d) {
					break;
				}
			}
			if (r==n) {
				cols.push_back(c);
			}
		}
		// mask
		int i;
		for (i=0;i<rows.size();i++)
			for (c=0;c<m;c++)
				x[rows[i]][c] = nd;
		for (i=0;i<cols.size();i++)
			for (r=0;r<n;r++)
				x[r][cols[i]] = nd;
		//check
		for (r=0;r<n;r++) {
			for (c=0;c<m;c++) {
				if (x[r][c] == d) {
					return false;
				}
			}
		}
		return true;
	}
	void prep() {
		int r,c;
	  set<char> heights;
		for (r=0;r<n;r++) {
			for (c=0;c<m;c++) {
				heights.insert(x[r][c]);
			}
		}
		h = vector<char>(heights.begin(), heights.end());
		max = *heights.rbegin();
	}

	void print() {
		int r,c;
		for (r=0;r<n;r++) {
			for (c=0;c<m;c++) {
				cout << x[r][c] << ' ';
			}
			cout << endl;
		}
	}	
  void read() {
		cin >> n >> m;
		int r,c;
		for (r=0;r<n;r++) {
			for (c=0;c<m;c++) {
				cin >> x[r][c];
			}
		}
	}
};

int main() {
	int T;
	string line;
	cin >> T;
	getline(cin, line);
	Input input;
	for (int i=1; i<=T; i++) {
		input.read();
	  cout << "Case #" << i << ": " << input.solve() << endl;
	}
	return 0;
}

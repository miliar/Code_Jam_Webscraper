#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <set>
#include <queue>
#include <string>
#include <ctime>
#include <cstring>
#include <cstdlib>

using namespace std;

int q[1 << 12];
const int dx[] = { -1, -1, -1, 1, 1, 1, 0, 0 };
const int dy[] = { 1, 0, -1, 0, 1, -1, -1, 1 };

bool isInside(int x, int y, int R, int C) {
	return (x >= 0 && y >= 0 && x < R && y < C);
}

int mineCount(vector<string>& A, int& x, int& y) {
	int ret = 0;
	for (int k = 0; k < 8; k++) {
		if (isInside(x + dx[k], y + dy[k], A.size(), A[0].size()) && A[x + dx[k]][y + dy[k]] == '*') {
			ret++;
		}
	}

	return ret;
};

void fill(vector<string>& A, int x, int y) {
	int num = mineCount(A, x, y);
	A[x][y] = (char)('0' + num);
	if (num == 0) {
		for (int k = 0; k < 8; k++) {
			if (isInside(x + dx[k], y + dy[k], A.size(), A[0].size()) && A[x + dx[k]][y + dy[k]] == '.') {
				fill(A, x + dx[k], y + dy[k]);
			}
		}
	}
}

void print(vector<string>& A, ostream& out) {
	for (const string& x : A) {
		out << x << "\n";
		
	}

}

int getStartCell(vector< string > A, int mines) {
	int R = (int)A.size();
	int C = (int)A[0].size();

	auto isInside = [&](int x, int y) {
		return (x >= 0 && y >= 0 && x < R && y < C);
	};

	auto mineCount = [&](int& x, int& y) {
		int ret = 0;
		for (int k = 0; k < 8; k++) {
			if (isInside(x + dx[k], y + dy[k]) && A[x + dx[k]][y + dy[k]] == '*') {
				ret++;
			}
		}

		return ret;
	};

	if (mines == R * C - 1) {
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				if (A[i][j] == '.') {
					return i | j << 6;
				}
			}
		}
	}

	int startCell = -1;
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			if (A[i][j] == '.') {
				if (startCell != -1) {
					startCell = -2;
					continue;
				}
				startCell = i | j << 6;
				if (mineCount(i, j) > 0) continue;
				int left = 0, right = 0;
				q[right++] = i | j << 6;
				while (left < right) {
					int v = q[left++];
					int x = v & 63;
					int y = v >> 6;
					A[x][y] = (char)('0' + mineCount(x, y));
					if (A[x][y] - '0' > 0)continue;
					for (int k = 0; k < 8; k++) {
						if (isInside(x + dx[k], y + dy[k]) && A[x + dx[k]][y + dy[k]] == '.') {
							A[x + dx[k]][y + dy[k]] = 'v';
							q[right++] = (x + dx[k]) | (y + dy[k]) << 6;
						}
					}
				}
			}
		}

	}

	return startCell;
}

vector<string> getGrid(int R, int C, int m) {
	auto isInside = [&](int x, int y) {
		return (x >= 0 && y >= 0 && x < R && y < C);
	};

	vector<string> ret(R, string(C, '*'));

	int left, right;
	left = right = 0;
	q[right++] = 0;
	int M = m;
	m = R * C - m;
	while (left < right) {
		int v = q[left++];
		int x = v & 63;
		int y = v >> 6;
		for (int k = 0; k < 8; k++) {
			if (isInside(x + dx[k], y + dy[k]) && ret[x + dx[k]][y + dy[k]] == '*' && m) {
				m--;
				ret[x + dx[k]][y + dy[k]] = '.';
				q[right++] = (x + dx[k]) | (y + dy[k]) << 6;
			}
		}
	}
	// return ret; 
	int cell = getStartCell(ret, M);
	if (cell < 0) {
		ret.clear();
		ret.push_back("Impossible");
	}
	else {
		ret[cell & 63][cell >> 6] = 'c';
	}

	return ret;
}

vector<string> rotateMatrix(vector<string> ret) {
	vector<string> aux(ret[0].size(), string(ret.size(), '.'));
	int r = ret.size();
	int c = ret[0].size();
	for (int i = 0; i < r; i++){
		for (int j = 0; j < c; j++) {
			aux[c - j - 1][r - i - 1] = ret[i][j];
		}
	}

	return aux;
}

vector<string> solveSmall(int r, int c, int m) {
	vector<string> ret;
	if (m == 0) {
		ret = vector<string>(r, string(c, '.'));
		ret[0][0] = 'c';
		return ret;
	}
	if (m == r * c - 1) {
		ret = vector<string>(r, string(c, '*'));
		ret[0][0] = 'c';
		return ret;
	}
	bool mustRotate = false;
	if (r > c) {
		swap(r, c);
		mustRotate = true;
	}

	if (r == 1) {
		ret.push_back(string(m, '*') + string(c - m - 1, '.') + "c");
	}
	else
	if (c == 1) {
		for (int i = 0; i < m; i++) {
			ret.push_back("*");
		}

		for (int i = 0; i < r - m - 1; i++) {
			ret.push_back(".");
		}
		ret.push_back("c");
	}
	else
	if (r == 2) {
		if (c == 2) {
			if (m == 1 || m == 2) {
				ret.push_back("Impossible");
			}
		}
		else
		if (c == 3) {
			if (m == 1 || m == 3 || m == 4) {
				ret.push_back("Impossible");
			}
			else
			if (m == 2) {
				ret = {
					"*.c",
					"*.."
				};
			}
		}
		else
		if (c == 4) {
			if (m == 1 || m == 3 || m == 5 || m == 6) {
				ret.push_back("Impossible");
			}
			else
			if (m == 2) {
				ret = {
					"c..*",
					"...*"
				};
			}
			else
			if (m == 4) {
				ret = {
					"c.**",
					"..**"
				};
			}
		}
		else
		if (c == 5) {
			if (m == 1 || m == 3 || m == 5 || m == 7 || m == 8) {
				ret.push_back("Impossible");
			}
			else
			if (m == 2) {
				ret = {
					"c...*",
					"....*"
				};
			}
			else
			if (m == 4) {
				ret = {
					"c..**",
					"...**"
				};
			}
			else
			if (m == 6) {
				ret = {
					"c.***",
					"..***"
				};
			}
		}
	}
	else
	if (r == 3) {
		if (c == 3) {
			if (m == 2 || m == 4 || m == 6 || m == 7 || m == 8) {
				ret.push_back("Impossible");
			}
			else
			if (m == 1) {
				ret = {
					"c..",
					"...",
					"..*"
				};
			}
			else
			if (m == 3) {
				ret = {
					"c..",
					"...",
					"***"
				};
			}
			else
			if (m == 5) {
				ret = {
					"c.*",
					"..*",
					"***"
				};

			}
		}
		else
		if (c == 4) {
			if (m == 5 || m == 7 || m == 9 || m == 10) {
				ret.push_back("Impossible");
			}
			else
			if (m == 1) {
				ret = {
					"c...",
					"....",
					"...*"
				};
			}
			else
			if (m == 2) {
				ret = {
					"c...",
					"....",
					"..**"
				};
			}
			else
			if (m == 3) {
				ret = {
					"c..*",
					"...*",
					"...*"
				};
			}
			else
			if (m == 4) {
				ret = {
					"c...",
					"....",
					"****"
				};

			}
			else
			if (m == 6) {
				ret = {
					"..**",
					"c.**",
					"..**"
				};
			}
			else
			if (m == 8) {
				ret = {
					"c.**",
					"..**",
					"****"
				};
			}

		}
		else
		if (c == 5) {
			if (m == 8 || m == 10 || m == 12 || m == 13) {
				ret.push_back("Impossible");
			}
			else
			if (m == 1) {
				ret = {
					"c....",
					".....",
					"....*"
				};
			}
			else
			if (m == 2) {
				ret = {
					"c....",
					".....",
					"...**"
				};
			}
			else
			if (m == 3) {
				ret = {
					"c...*",
					"....*",
					"....*"
				};
			}
			else
			if (m == 4) {
				ret = {
					"c...*",
					"....*",
					"...**"
				};

			}
			else
			if (m == 5) {
				ret = {
					"c....",
					".....",
					"*****"
				};

			}
			else
			if (m == 6) {
				ret = {
					"...**",
					"c..**",
					"...**"
				};
			}
			else
			if (m == 7) {
				ret = {
					"c...*",
					"....*",
					"*****"
				};

			}
			else
			if (m == 9) {
				ret = {
					"c.***",
					"..***",
					"..***"
				};
			}
			else
			if (m == 11) {
				ret = {
					"c.***",
					"..***",
					"*****"
				};
			}
		}

	}
	else
	if (r == 4) {
		if (c == 4) {
			if (m == 9 || m == 11 || m == 13 || m == 14) {
				ret.push_back("Impossible");
			}
			else
			if (m == 1) {
				ret = {
					"c...",
					"....",
					"....",
					"...*"
				};
			}
			else
			if (m == 2) {
				ret = {
					"c...",
					"....",
					"....",
					"..**"
				};
			}
			else
			if (m == 3) {
				ret = {
					"c...",
					"....",
					"...*",
					"..**"
				};
			}
			else
			if (m == 4) {
				ret = {
					"c...",
					"....",
					"....",
					"****"
				};

			}
			else
			if (m == 5) {
				ret = {
					"c...",
					"....",
					"...*",
					"****"
				};
			}
			else
			if (m == 6) {
				ret = {
					"...*",
					"c..*",
					"..**",
					"..**"
				};
			}
			else
			if (m == 7) {
				ret = {
					"c..*",
					"...*",
					"...*",
					"****"
				};
			}
			else
			if (m == 8) {
				ret = {
					"c.**",
					"..**",
					"..**",
					"..**"
				};
			}
			else
			if (m == 10) {
				ret = {
					"c.**",
					"..**",
					"..**",
					"****"
				};

			}
			else
			if (m == 12) {
				ret = {
					"c.**",
					"..**",
					"****",
					"****"
				};
			}
		}
		else
		if (c == 5) {
			if (m == 13 || m == 15 || m == 17 || m == 18) {
				ret.push_back("Impossible");
			}
			else
			if (m == 1) {
				ret = {
					"c....",
					".....",
					".....",
					"....*"
				};
			}
			else
			if (m == 2) {
				ret = {
					"c....",
					".....",
					".....",
					"...**"
				};
			}
			else
			if (m == 3) {
				ret = {
					"c....",
					".....",
					".....",
					"..***"
				};
			}
			else
			if (m == 4) {
				ret = {
					"c...*",
					"....*",
					"....*",
					"....*"
				};

			}
			else
			if (m == 5) {
				ret = {
					"c....",
					".....",
					".....",
					"*****"
				};
			}
			else
			if (m == 6) {
				ret = {
					"c....",
					".....",
					"....*",
					"*****"
				};
			}
			else
			if (m == 7) {
				ret = {
					"c....",
					".....",
					"...**",
					"*****"
				};

			}

			else
			if (m == 8) {
				ret = {
					"c..**",
					"...**",
					"...**",
					"...**"
				};
			}
			else
			if (m == 9) {
				ret = {
					"c...*",
					"....*",
					"...**",
					"*****"
				};
			}
			else
			if (m == 10) {
				ret = {
					"c....",
					".....",
					"*****",
					"*****"
				};
			}
			else
			if (m == 11) {
				ret = {
					"c..**",
					"...**",
					"...**",
					"*****"
				};
			}
			else
			if (m == 12) {
				ret = {
					"c...*",
					"....*",
					"*****",
					"*****"
				};
			}
			else
			if (m == 14) {
				ret = {
					"c..**",
					"...**",
					"*****",
					"*****"
				};
			}
			else
			if (m == 16) {
				ret = {
					"c.***",
					"..***",
					"*****",
					"*****"
				};
			}
		}
	}
	else
	if (r == 5) {
		if (c == 5) {
			if (m == 18 || m == 20 || m == 22 || m == 23) {
				ret.push_back("Impossible");
			}
			else
			if (m == 1) {
				ret = {
					"c....",
					".....",
					".....",
					".....",
					"....*"
				};
			}
			else
			if (m == 2) {
				ret = {
					"c....",
					".....",
					".....",
					".....",
					"...**"
				};
			}
			else
			if (m == 3) {
				ret = {
					"c....",
					".....",
					".....",
					"....*",
					"...**"
				};
			}
			else
			if (m == 4) {
				ret = {
					"c....",
					".....",
					".....",
					"...**",
					"...**"
				};

			}
			else
			if (m == 5) {
				ret = {
					"c....",
					".....",
					".....",
					".....",
					"*****"
				};
			}
			else
			if (m == 6) {
				ret = {
					".....",
					"c....",
					"...**",
					"...**",
					"...**"
				};
			}
			else
			if (m == 7) {
				ret = {
					"c....",
					".....",
					".....",
					"...**",
					"*****"
				};

			}
			else
			if (m == 8) {
				ret = {
					"c....",
					".....",
					"...**",
					"..***",
					"..***"
				};
			}
			else
			if (m == 9) {
				ret = {
					"c....",
					".....",
					"..***",
					"..***",
					"..***"
				};
			}
			else
			if (m == 10) {
				ret = {
					"c....",
					".....",
					".....",
					"*****",
					"*****"
				};
			}
			else
			if (m == 11) {
				ret = {
					"c....",
					".....",
					"....*",
					"*****",
					"*****"
				};
			}
			else
			if (m == 12) {
				ret = {
					"c....",
					".....",
					"...**",
					"*****",
					"*****"
				};
			}
			else
			if (m == 13) {
				ret = {
					"c...*",
					"....*",
					"....*",
					"*****",
					"*****"
				};
			}
			else
			if (m == 14) {
				ret = {
					"c...*",
					"....*",
					"...**",
					"*****",
					"*****"
				};
			}
			else
			if (m == 15) {
				ret = {
					"c....",
					".....",
					"*****",
					"*****",
					"*****"
				};
			}
			else
			if (m == 16) {
				ret = {
					"c..**",
					"...**",
					"...**",
					"*****",
					"*****"
				};
			}
			else
			if (m == 17) {
				ret = {
					"c...*",
					"....*",
					"*****",
					"*****",
					"*****"
				};
			}
			else
			if (m == 19) {
				ret = {
					"c..**",
					"...**",
					"*****",
					"*****",
					"*****"
				};
			}
			else
			if (m == 21) {
				ret = {
					"c.***",
					"..***",
					"*****",
					"*****",
					"*****"
				};
			}
		}
	}

	if (ret[0] != "Impossible" && mustRotate) {
		ret = rotateMatrix(ret);
	}

	return ret;
}

void generateData(int testCount, int rBound, int cBound, string file) {
	ofstream out(file);
	srand(static_cast<unsigned int>(time(0)));
	out << testCount << "\n";
	for (int testCase = 1; testCase <= testCount; testCase++) {
		int r = rand() % rBound + 1;
		int c = rand() % cBound + 1;
		int m = rand() % (r * c);
		out << r << " " << c << " " << m << "\n";
	}
}

inline int bitcnt(int x) { int ret = 0; while (x) { x &= (x - 1); ret++; } return ret; }

void test(int i,int j) {
	ofstream cout("test.out");
	const char* xx = ".*";
	vector< vector<string> > g(i*j, vector<string>{"Impossible"});
	for (int k = 0; k < (1 << (i*j)); k++) {
		//if (bitcnt(k) > 15) continue;
		vector<string> a(i, string(j, '.'));
		for (int w = 0; w < i * j; w++) {
			a[w / j][w % j] = xx[(k >> w) & 1];
		}
		int nb = 0;
		int sx, sy;
		sx = sy = -1;
		vector<string> aux = a;
		for (int x = 0; x < i; x++) {
			for (int y = 0; y < j; y++) {
				if (a[x][y] == '.') {
					nb++;
					if (sx == -1 && mineCount(a, x, y) == 0) {
						sx = x;
						sy = y;
					}
				}
			}
		}
		bool weCan = false;
		if (sx == -1) {
			weCan = nb == 1;
		} else {
			aux[sx][sy] = 'c';
			weCan = true;
			fill(a, sx, sy);

			for (auto& z : a) for (auto q : z) if (q == '.') weCan = false;
		}
		if (weCan) {
			g[i * j - nb] = aux;
		}
	}

	for (int k = 1; k < i*j; k++) {
		if (g[k][0] != "Impossible") {
			cout << k << " :\n";
			print(g[k], cout);
		}
	}
	
}


void go() {
	ofstream cout("test.out");
	for (int i = 1; i <= 5; i++){
		for (int j = 1; j <= 5; j++) {
			for (int m = 0; m < i*j; m++) {
				vector<string> grid = solveSmall(i, j, m);
				if (grid[0] != "Impossible") {
					pair<int, int> s = { -1, -1 };
					for (int x = 0; x < i; x++) {
						for (int y = 0; y < j; y++) {
							if (grid[x][y] == 'c') {
								s = { x, y };
							}
						}
					}

					fill(grid, s.first, s.second);
					bool weCan = true;
					for (auto& z : grid)
					for (auto q : z) {
						if (q == '.') weCan = false;
					}

					print(grid, cout); cout << "\n";
					if (!weCan) {
						cout << "fucked\n";
					}
				}
			}
		}
	}
}

int main()
{
	//go(); return 0;
	//test(3,5); return 0;
	ifstream cin("test.in");
	ofstream cout("test.out");
	int testCount;
	int r, c, m;
	cin >> testCount;
	for (int testCase = 1; testCase <= testCount; testCase++) {
		cin >> r >> c >> m;
		vector<string> ans = solveSmall(r, c, m);
		cout << "Case #" << testCase << ":\n"; print(ans, cout);
	}
	return 0;
}

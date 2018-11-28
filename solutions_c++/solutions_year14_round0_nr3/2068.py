#include<iostream>
#include<vector>
#include<string>
#include<cassert>

using namespace std;
bool test(const vector<string>& res);
void solve(int n, int m, int mines);

void print(const vector<string>& res, int t) {
	
	/*if ((t == 0) || (t == 1)) {
		bool ans = test(res);
		if (ans) {
			cerr << "OK\n";
			return;
		}
		else {
			cerr << "ERROR!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n";
			assert(0);
			return;
		}
	}*/
	
	if (t == 0) {
		for (int i = 0; i < res.size(); ++i) {
			cout << res[i] << endl;
		}
		return;
	}
	if (t == 1) {
		for (int i = 0; i < res[0].size(); ++i) {
			for (int j = 0; j < res.size(); ++j) {
				cout << res[j][i];
			}
			cout << endl;
		}
		return;
	}
	cout << "Impossible" << endl;
	return;
	
}

bool valid(int x, int y, int n, int m) {
	return ((x >= 0) && (y >= 0) && (x < n) && (y < m));
}

vector<pair<int, int> > get(int x, int y, int n, int m) {
	vector<pair<int, int> > res;
	for (int i = -1; i < 2; ++i) {
		for (int j = -1; j < 2; ++j) {
			if ((i == 0) && (j == 0))
				continue;
			int xx = x + i, yy = y + j;
			if (valid(xx, yy, n, m))
				res.push_back(pair<int, int>(xx, yy));
		}
	}
	return res;
}

bool is0(int x, int y, const vector<string>& res) {
	vector<pair<int, int> > nei = get(x, y, res.size(), res[0].size());
	if (res[x][y] == '*')
		return false;
	for (int i = 0; i < nei.size(); ++i) {
		if (res[nei[i].first][nei[i].second] == '*')
			return false;
	}
	return true;
}

void dfs(int x, int y, const vector<string>& res, vector<vector<int> >& used) {
	used[x][y] = true;
	if (!is0(x, y, res))
		return;
	vector<pair<int, int> > nei = get(x, y, res.size(), res[0].size());
	for (int i = 0; i < nei.size(); ++i) {
		pair<int, int> to = nei[i];
		if (used[to.first][to.second])
			continue;
		if (res[to.first][to.second] == '*')
			continue;
		dfs(to.first, to.second, res, used);
	}
}

bool test(const vector<string>& res) {
	int n = res.size();
	int m = res[0].size();
	vector<vector<int> > used(n, vector<int>(m, 0));
	dfs(0, 0, res, used);
	bool ans = true;
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			ans = ans && ((used[i][j] == 1) == (res[i][j] != '*'));
		}
	}
	return ans;
}

void read(int& n, int& m, int& mines) {
	cin >> n >> m >> mines;

}

void solve() {
	int n, m, mines;
	read(n, m, mines);
	solve(n, m, mines);
}

void solve(int n, int m, int mines) {
	int tr = 0;
	if (m < n) {
		swap(m, n);
		tr = 1;
	}
	vector<string> res;
	res.assign(n, string(m, '.'));	
	if (n == 1) {
		res[0][0] = 'c';
		for (int i = 1; i < m - mines; ++i)
			res[0][i] = '.';
		for (int i = m - mines; i < m; ++i)
			res[0][i] = '*';
		print(res, tr);
		return;
	}
	if (n == 2) {
		if (2 * m - 1 == mines) {
			for (int i = 0; i < m; ++i) {
				res[1][i] = '*';
				if (i)
					res[0][i] = '*';
			}
			res[0][0] = 'c';
			print(res, tr);
			return;
		}
		if ((mines & 1) || (2 * m - mines == 2)) {
			print(res, 3);
			return;
		}
		res[0][0] = 'c';
		for (int i = m - mines / 2; i < m; ++i)
			res[0][i] = res[1][i] = '*';
		print(res, tr);
		return;
	}
	int open = n * m - mines;
	if ((open == 2) || (open == 3) || (open == 5) || (open == 7)) {
		print(res, 4345);
		return;
	}
	res[0][0] = 'c';
	if (mines == 0) {
		print(res, tr);
		return;
	}
	int r = open / m;
	int c = open % m;
	if (r > 1) {
		for (int i = r + 1; i < n; ++i)
			for (int j = 0; j < m; ++j)
				res[i][j] = '*';
		if (c != 1) {
			for (int j = c; j < m; ++j)
				res[r][j] = '*';
		}
		if (c == 1) {
			if (r == 2) {
				res[0][m - 1] = res[1][m - 1] = '*';
				for (int j = 3; j < m; ++j)
					res[r][j] = '*';
			}
			if (r != 2) {
				for (int j = 2; j < m; ++j)
					res[r][j] = '*';
				res[r - 1][m - 1] = '*';
			}
		}
		print(res, tr);
		return;
	}
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < m; ++j)
			if (i + j > 0)
				res[i][j] = '*';
	if (open == 1) {		
		print(res, tr);
		return;
	}
	if (open % 2 == 0) {
		for (int i = 0; i < open / 2; ++i) {
			res[1][i] = '.';
			if (i)
				res[0][i] = '.';
		}
		print(res, tr);
		return;
	}
	for (int i = 0; i < 3; ++i) {
		for (int j = 0; j < 3; ++j) {
			if (i + j > 0)
				res[i][j] = '.';
		}
	}
	open -= 3;
	for (int i = 3; i < open / 2; ++i)
		res[0][i] = res[1][i] = '.';
	print(res, tr);
}

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		cout << "Case #" << i + 1 << ": \n";
		solve();
		cerr << i << endl;
	}
	/*
	for (int r = 1; r < 50; ++r)
		for (int c = 1; c < 50; ++c)
			for (int m = 0; m < r * c; ++m) {
				cerr << r << "\t" << c << "\t" << m << "\t";
				solve(r, c, m);
			}*/
	return 0;
}
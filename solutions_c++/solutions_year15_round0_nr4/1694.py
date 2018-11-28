#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <fstream>
#include <queue>


using namespace std;

/*
int go(vector<int> v) {
	//if (me.find(v) != me.end()) {
		//return me[v];
	//}
	int t = -1;
	int n = -1;
	for (int i = 0; i < v.size(); i++) {
		if (v[i] > t) {
			t = v[i];
			n = i;
		}
	}
	if (t == 1) {
		return 1;
	}
	int u = 1e9;
	int r = v[n];
	v[n] = (v[n] + 2 - 1) / 2;
	r -= v[n];
	v.push_back(r);
	u = min(u, go(v) + 1);
	v.pop_back();
	v[n] = t;
	for (int i = 0; i < v.size(); i++) {
		v[i] = max(0, v[i] - 1);
	}
	u = min(u, go(v) + 1);
	return u;
}

int getmaxi(vector<int> &v) {
	int t = -1;
	int n = -1;
	for (int i = 0; i < v.size(); i++) {
		if (v[i] > t) {
			t = v[i];
			n = i;
		}
	}
	return n;
}

int d;
	in >> d;
	vector<int> v(d);
	for (int i = 0; i < d; i++) {
		in >> v[i];
	}
	int n = getmaxi(v);
	int w = 0;
	int ans = v[n];
	while (1) {
		int r = v[n];
		v[n] = (v[n] + 2 - 1) / 2;
		r -= v[n];
		v.push_back(r);
		w++;
		n = getmaxi(v);
		ans = min(ans, w + v[n]);
		if (v[n] == 1) {
			break;
		}
	}*/

/*
bool gg(int n) {
	if (n == 0) {
		bool em = false;
		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) {
				if (v[i][j] == '.') {
					v[i][j] = 'g';
				}
			}
		}
	}
	int dx[] = {1, 0, -1, 0};
	int dy[] = {0, -1, 0, 1};
	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			if (v[i][j] == 'g') {
				for (int k = 0; k < 4; k++) {
					int a = i + dx[k];
					int b = j + dy[k];
					if (a >= 0 && a < r && b >= 0 && b < c && v[a][b] == '.') {
						v[a][b] = 'g';
						bool res = gg(n - 1);
						v[a][b] = '.';
						if (res) {
							return true;
						}
					}
				}
			}
		}
	}
	return false;
}*/

/*int ggg(int n) {
	bool can = false;
	int dx[] = {1, 0, -1, 0};
	int dy[] = {0, -1, 0, 1};
	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			if (v[i][j] == 'g') {
				for (int k = 0; k < 4; k++) {
					int a = i + dx[k];
					int b = j + dy[k];
					if (a >= 0 && a < r && b >= 0 && b < c && v[a][b] == '.') {
						can = true;
						v[a][b] = 'g';
						bool res = ggg(n + 1);
						v[a][b] = '.';
						if (res) {
							return true;
						}
					}
				}
			}
		}
	}
	if (!can) {
		//printv();
		if (n % x == 0) {
			return true;
		} else {
			printv();
		}
	}
	return false;
}

bool go(int n) {
	if (n == 0) {
		//printv();
		bool gbo = false;
		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) {
				if (v[i][j] == '.') {
					v[i][j] = 'g';
					bool res = ggg(1);
					//cout << res << endl;
					v[i][j] = '.';
					if (res) {
						gbo = true;
						goto gohere;
					}
				}
			}
		}
	gohere:
		if (gbo) {
			return false;
		} else {
			return true;
		}
	}
	int dx[] = {1, 0, -1, 0};
	int dy[] = {0, -1, 0, 1};
	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			if (v[i][j] == 'r') {
				//cout << i<<' '<<j<<endl;
				//printv();
				for (int k = 0; k < 4; k++) {
					int a = i + dx[k];
					int b = j + dy[k];
					//cout <<"     "<< a<<' '<<b<<endl;
					if (a >= 0 && a < r && b >= 0 && b < c && v[a][b] == '.') {
						//cout << "yes"<<endl;
						v[a][b] = 'r';
						bool res = go(n - 1);
						v[a][b] = '.';
						if (res) {
							return true;
						}
					}
				}
			}
		}
	}
	return false;
}*/

vector<string> v;
vector<string> cur;
int r;
int c;
int x;


void printv(vector<string> &t) {
	for (int i = 0; i < t.size(); i++) {
		for (int j = 0; j < t[0].size(); j++) {
			cout << t[i][j] << ' ';
		}
		cout << endl;
	}
	cout << "-----------------" << endl;
}

map< vector<string>, vector<string> > merotate;
vector<string> rotate(vector<string> &o) {
	if (merotate.find(o) != merotate.end()) {
		return merotate[o];
	}
	int n = o.size();
	vector<string> t(n, string(n, ' '));
	for (int i = 0, j = n - 1; i < n; i++, j--) {
		for (int k = 0; k < n; k++) {
			t[i][k] = o[k][j];
		}
	}
	return merotate[o] = t;
}

map< vector<string>, vector<string> > mereduce;
vector<string> reduce(vector<string> &o) {
	if (mereduce.find(o) != mereduce.end()) {
		return mereduce[o];
	}
	int n = o.size();
	int a = -1, b = 30, c = -1, d = 30;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (o[i][j] == 'r') {
				a = max(a, i);
				b = min(b, i);
				c = max(c, j);
				d = min(d, j);
			}
		}
	}
	vector<string> t(a - b + 1, string(c - d + 1, ' '));
	for (int i = b; i <= a; i++) {
		for (int j = d; j <= c; j++) {
			t[i - b][j - d] = o[i][j];
		}
	}
	return mereduce[o] = t;
}

map< pair< vector<string>, int>, bool> rrome;
bool rro(int n) {
	pair< vector<string>, int> pa(cur, n);
	if (rrome.find(pa) != rrome.end()) {
		return rrome[pa];
	}
	bool can = false;
	int dx[] = {1, 0, -1, 0};
	int dy[] = {0, -1, 0, 1};
	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			if (cur[i][j] == 'g') {
				for (int k = 0; k < 4; k++) {
					int a = i + dx[k];
					int b = j + dy[k];
					if (a >= 0 && a < r && b >= 0 && b < c && cur[a][b] == '.') {
						can = true;
						cur[a][b] = 'g';
						bool res = rro(n + 1);
						cur[a][b] = '.';
						if (res) {
							return rrome[pa] = true;
						}
					}
				}
			}
		}
	}
	if (!can) {
		if (n % x != 0) {
			return rrome[pa] = false;
		}
		bool found = false;
		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) {
				if (cur[i][j] == '.') {
					found = true;
					cur[i][j] = 'g';
					bool res = rro(1);
					cur[i][j] = '.';
					if (res) {
						return rrome[pa] = true;
					}
				}
			}
		}
		if (!found) {
			return rrome[pa] = true;
		}
	}
	return rrome[pa] = false;
}

map< pair< vector<string>, int>, bool> rome;
bool ro(int n) {
	pair< vector<string>, int> pa(v, n);
	if (rome.find(pa) != rome.end()) {
		return rome[pa];
	}
	int dx[] = {1, 0, -1, 0};
	int dy[] = {0, -1, 0, 1};
	if (n == 0) {
		vector<string> t(v);
		for (int i = 0; i < t.size(); i++) {
			reverse(t[i].begin(), t[i].end());
		}
		vector< vector<string> > rr;
		rr.push_back(reduce(v));
		rr.push_back(reduce(t));
		for (int i = 0; i < 3; i++) {
			rr.push_back(reduce(rotate(v)));
		}
		for (int i = 0; i < 3; i++) {
			rr.push_back(reduce(rotate(t)));
		}
		bool ok = true;
		for (int i = 0; i < rr.size(); i++) {
			int a = rr[i].size();
			int b = rr[i][0].size();
			if (max(a, b) > max(r, c) || min(a, b) > min(r, c)) {
				goto okgoto;
			}
			if (a > r || b > c) {
				continue;
			}
			for (int j = 0; j < r - a + 1; j++) {
				for (int k = 0; k < c - b + 1; k++) {
					cur = vector<string>(r, string(c, '.'));
					for (int e = 0; e < a; e++) {
						for (int f = 0; f < b; f++) {
							cur[j + e][k + f] = rr[i][e][f];
						}
					}
					bool res = rro(0);
					if (res) {
						ok = false;
						goto okgoto;
					}
					/*bool rlose = true;
					for (int e = 0; e < a; e++) {
						for (int f = 0; f < b; f++) {
							if (cur[e][f] == '.') {
								rlose = false;
								cur[e][f] = 'g';
								bool res = rro(1);
								cur[e][f] = '.';
								if (res) {
									ok = false;
									goto okgoto;
								}
							}
						}
					}
					if (rlose) {
						ok = false;
						goto okgoto;
					}*/
				}
			}
		}
	okgoto:
		if (ok) {
			return rome[pa] = true;
		}
		return rome[pa] = false;
	}
	for (int i = 0; i < x; i++) {
		for (int j = 0; j < x; j++) {
			if (v[i][j] == 'r') {
				for (int k = 0; k < 4; k++) {
					int a = i + dx[k];
					int b = j + dy[k];
					if (a >= 0 && a < x && b >= 0 && b < x && v[a][b] == '.') {
						v[a][b] = 'r';
						bool res = ro(n - 1);
						v[a][b] = '.';
						if (res) {
							return rome[pa] = true;
						}
					}
				}
			}
		}
	}
	return rome[pa] = false;
}
string ansche[21][21][21];
void gcj_solve(int caseno, ifstream &in, ofstream &out) {
	ansche[2][2][2] = "GABRIEL";
	ansche[2][3][1] = "RICHARD";
	ansche[4][4][1] = "RICHARD";
	ansche[3][3][2] = "GABRIEL";
	ansche[3][2][1] = "RICHARD";
	ansche[2][4][2] = "GABRIEL";
	ansche[2][3][2] = "GABRIEL";
	ansche[1][2][1] = "GABRIEL";
	ansche[3][4][4] = "RICHARD";
	ansche[3][3][3] = "GABRIEL";
	ansche[2][4][1] = "GABRIEL";
	ansche[3][4][3] = "GABRIEL";
	ansche[3][3][1] = "RICHARD";
	ansche[4][1][1] = "RICHARD";
	ansche[2][3][3] = "RICHARD";
	ansche[3][2][2] = "RICHARD";
	ansche[2][3][1] = "RICHARD";
	ansche[3][4][3] = "GABRIEL";
	ansche[1][3][3] = "GABRIEL";
	ansche[1][3][1] = "GABRIEL";
	ansche[3][3][1] = "RICHARD";
	ansche[1][1][1] = "GABRIEL";
	ansche[4][4][4] = "GABRIEL";
	ansche[3][2][1] = "RICHARD";
	ansche[2][2][1] = "GABRIEL";
	ansche[1][3][2] = "GABRIEL";
	ansche[4][4][3] = "GABRIEL";
	ansche[4][4][2] = "RICHARD";
	ansche[4][4][2] = "RICHARD";
	ansche[1][3][2] = "GABRIEL";
	ansche[4][3][3] = "RICHARD";
	ansche[1][4][2] = "GABRIEL";
	ansche[3][3][2] = "GABRIEL";
	ansche[4][3][1] = "RICHARD";
	ansche[2][4][3] = "GABRIEL";
	ansche[2][4][3] = "GABRIEL";
	ansche[2][4][2] = "GABRIEL";
	ansche[2][2][1] = "GABRIEL";
	ansche[3][4][2] = "RICHARD";
	ansche[4][2][1] = "RICHARD";
	ansche[4][3][2] = "RICHARD";
	ansche[1][4][2] = "GABRIEL";
	ansche[4][2][1] = "RICHARD";
	ansche[3][4][1] = "RICHARD";
	ansche[4][3][1] = "RICHARD";
	ansche[2][1][1] = "RICHARD";
	ansche[4][3][2] = "RICHARD";
	ansche[3][4][1] = "RICHARD";
	ansche[1][4][3] = "GABRIEL";
	ansche[1][2][2] = "GABRIEL";
	ansche[4][4][3] = "GABRIEL";
	ansche[1][4][1] = "GABRIEL";
	ansche[4][2][2] = "RICHARD";
	ansche[1][3][1] = "GABRIEL";
	ansche[1][4][4] = "GABRIEL";
	ansche[3][4][2] = "RICHARD";
	ansche[1][2][1] = "GABRIEL";
	ansche[2][4][4] = "GABRIEL";
	ansche[2][4][1] = "GABRIEL";
	ansche[4][4][1] = "RICHARD";
	ansche[2][3][2] = "GABRIEL";
	ansche[3][1][1] = "RICHARD";
	ansche[1][4][3] = "GABRIEL";
	ansche[1][4][1] = "GABRIEL";

	int xx, rr, cc;
	in >> xx >> rr >> cc;
	r = max(rr, cc);
	c = min(rr, cc);
	x = xx;
	/*v = vector<string>(x, string(x, '.'));
	rome.clear();
	string ans = "GABRIEL";
	if (ansche[x][r][c] != "") {
		ans = ansche[x][r][c];
		goto end;
	}
	if (x > max(r, c)) {
		ans = "RICHARD";
		goto end;
	}
	for (int i = 0; i < x; i++) {
		for (int j = 0; j < x; j++) {
			v[i][j] = 'r';
			bool res = ro(x - 1);
			v[i][j] = '.';
			if (res) {
				ans = "RICHARD";
				goto end;
			}
		}
	}*/
end:
	string ans = ansche[x][r][c];
	cout <<x<<' '<< r<<' '<<c<<" Case #" << caseno << ": " << ans << "\n";
	//out <<x<<' '<< r<<' '<<c<<" Case #" << caseno << ": " << ans << "\n";
	out << "Case #" << caseno << ": " << ans << "\n";
}
int google_code_jam() {
	ifstream in("input0.in");
	ofstream out("output.out");
	if (!in.is_open() || in.eof() || !out.is_open()) {
		cout << "error" << endl;
		return -1;
	}
	int nc;
	in >> nc;
	for (int i = 1; i <= nc; i++) {
		if (in.eof()) {
			cout << "error 2" << endl;
			return -1;
		}
		gcj_solve(i, in, out);
	}
	in.close();
	out.close();
	return 0;
}

int main() {
	google_code_jam();
}
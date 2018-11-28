#include <bits/stdc++.h>

using namespace std;

struct RTC{~RTC(){cerr << "Time: " << clock() * 1.0 / CLOCKS_PER_SEC <<" seconds\n";}} runtimecount;
#define DBG(X) cerr << #X << " = " << X << '\n';
#define mp make_pair
#define mt make_tuple
#define pb push_back
#define eb emplace_back
#define sz(x) ((int)(x).size())
#define all(c) (c).begin(),(c).end()
#define forn(i, n) for (int i = 0; i < (n); i++)
struct omino {
  vector<vector<bool> > v;
  omino() {}
  omino(vector<vector<bool> > e) {
    int n = e.size();
    int m = e[0].size();
    int mini = 123456, maxi = -1;
    int minj = 123456, maxj = -1;
    forn (i, n) forn (j, m)
      if (e[i][j]) {
	mini = min(mini, i);
	maxi = max(maxi, i);
	minj = min(minj, j);
	maxj = max(maxj, j);
      }
    v = vector<vector<bool> >(maxi - mini + 1, vector<bool>(maxj - minj + 1));
    for (int i = mini; i <= maxi; i++)
      for (int j = minj; j <= maxj; j++)
	v[i - mini][j - minj] = e[i][j];
  }
  omino rotate() {
    int n = v.size();
    if (v.size() == 0) return omino();
    int m = v[0].size();
    vector<vector<bool> > ans(m, vector<bool>(n));
    for (int i = 0; i < n; i++)
      for (int j = 0; j < m; j++)
	ans[j][n - i - 1] = v[i][j];
    return omino(ans);
  }
  omino reflect() {
    int n = v.size();
    if (v.size() == 0) return omino();
    int m = v[0].size();
    vector<vector<bool> > ans = vector<vector<bool> >(all(v));
    for (int i = 0; i < n; i++) {
      int a = 0, b = m - 1;
      while (a < b) {
	bool tmp = ans[i][a];
	ans[i][a] = ans[i][b];
	ans[i][b] = tmp;
	a++;
	b--;
      }
    }
    return omino(ans);
  }
  bool operator < (const omino &other) const {
    return (v < other.v);
  }
  bool operator == (const omino &other) const {
    return (v == other.v);
  }
  string toString() {
    stringstream ss;
    for (int i = 0; i < v.size(); i++) {
      for (int j = 0; j < v[i].size(); j++)
	ss << v[i][j];
      ss << endl;
    }
    return ss.str();
  }
};
int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};
vector<vector<bool> > v(8, vector<bool>(8, false));
set<omino> vec[5];
bool mark[5][123];
void generate(int n) {
  vec[n].insert(omino(v));
  if (n == 4) return;
  for (int i = 0; i < 8; i++)
    for (int j = 0; j < 8; j++)
      if (v[i][j])
	for (int k = 0; k < 4; k++) {
	  int ii = i + dx[k];
	  int jj = j + dy[k];
	  if (ii >= 0 && ii < 8 && jj >= 0 && jj < 8)
	    if (!v[ii][jj]) {
	      v[ii][jj] = true;
	      generate(n + 1);
	      v[ii][jj] = false;
	    }
	}
}
vector<vector<omino> > elem[5];
void process() {
  v[3][3] = true;
  generate(1);
  for (int tam = 1; tam <= 4; tam++) {
    vector<omino> tmp(all(vec[tam]));
    int n = sz(tmp);
    vector<bool> mark(n, false);
    for (int i = 0; i < n; i++)
      if (!mark[i]) {
	mark[i] = true;
        set<omino> o;
	omino cur = tmp[i];
	for (int _ = 0; _  < 4; _++) {
	  o.insert(cur);
	  cur = cur.rotate();
	}
	cur = cur.reflect();
	for (int _ = 0; _  < 4; _++) {
	  o.insert(cur);
	  cur = cur.rotate();
	}
	for (auto e: o) {
	  for (int j = i + 1; j < n; j++)
	    if (e == tmp[j])
	      mark[j] = true;
	}
	elem[tam].pb(vector<omino>(all(o)));
      }
  }
}
vector<omino> myset;
bool board[20][20] = {0};
int r, c;
bool filledboard() {
  forn (i, r) forn (j, c)
    if (!board[i][j])
      return false;
  return true;
}
bool test(const omino& e, int i, int j) {
  if ((i + sz(e.v)) <= r && (j + sz(e.v[0])) <= c) {
    for (int a = 0; a < sz(e.v); a++)
      for (int b = 0; b < sz(e.v[a]); b++)
	if (e.v[a][b] && board[i + a][j + b])
	  return false;
    return true;
  }
  return false;
}
void push(const omino& e, int i, int j) {
  for (int a = 0; a < sz(e.v); a++)
    for (int b = 0; b < sz(e.v[a]); b++)
      if (e.v[a][b]) {
	assert(!board[i + a][j + b]);
	board[i + a][j + b] = true;
      }
}
void pop(const omino& e, int i, int j) {
  for (int a = 0; a < sz(e.v); a++)
    for (int b = 0; b < sz(e.v[a]); b++)
      if (e.v[a][b]) {
	assert(board[i + a][j + b]);
	board[i + a][j + b] = false;
      }
}
bool check() {
  if (filledboard()) return true;
  for (int i = 0; i < r; i++)
    for (int j = 0; j < c; j++)
      for (int k = 0; k < sz(myset); k++) {
	if (test(myset[k], i, j)) {
	  push(myset[k], i, j);
	  bool ans = check();
	  pop(myset[k], i, j);
	  if (ans) return true;
	}
      }
  return false;
}
string solve(int tam) {
  myset = vector<omino>();
  for (int i = 0; i < sz(elem[tam]); i++)
    for (int j = 0; j < sz(elem[tam][i]); j++)
      myset.pb(elem[tam][i][j]);
  for (int s = 0; s < sz(elem[tam]); s++) {
    bool possible = false;
    for (auto obj: elem[tam][s]) {
      for (int i = 0; i < r && !possible; i++)
	for (int j = 0; j < c && !possible; j++) {
	  memset(board, false, sizeof(board));
	  if (test(obj, i, j)) {
	    push(obj, i, j);
	    possible = check();
	  }
	}
      if (possible) break;
    }
    if (!possible)
      return "RICHARD";
  }
  return "GABRIEL";
}
int main() {
  process();
  int t, x;
  scanf("%d", &t);
  for (int caso = 1; caso <= t; caso++) {
    scanf("%d %d %d", &x, &r, &c);
    printf("Case #%d: ", caso);
    cout << solve(x) << endl;
  }
  return 0;
}

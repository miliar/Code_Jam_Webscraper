#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <iomanip>

using namespace std;

typedef long long ll;
typedef vector<string> ret_t;

class Solver {
public:
  ret_t solve(int r, int c, int m) {
    ret_t ret(r, string(c, '*'));
    int f = r*c - m;
    if (m == 0) {
      // no mines
      ret = vector<string>(r, string(c, '.'));
      ret[0][0] = 'c';
      return ret;
    }
    if (f == 1) {
      // just one empty field
      ret[0][0] = 'c';
      return ret;
    }
    if (f == 2*c || c == 1 || (f >= 2*c+2 && (f % c == 0 || c > 2))) {
      // solution with free row
      int x = 0;
      int y = 0;
      for (int i = 0; i < f; ++i) {
	ret[x][y] = '.';
	++y;
	if (y == c) {y = 0; ++x;}
      }
      if (f % c == 1) {
	ret[x][y] = '.';
	ret[x-1][c-1] = '*';
      }
      ret[0][0] = 'c';
      return ret;
    }
    if (f == 2*r || r == 1 || (f >= 2*r+2 && (f % r == 0 || r > 2))) {
      // solution with free column
      int x = 0;
      int y = 0;
      for (int i = 0; i < f; ++i) {
	ret[x][y] = '.';
	++x;
	if (x == r) {x = 0; ++y;}
      }
      if (f % r == 1) {
	ret[x][y] = '.';
	ret[r-1][y-1] = '*';
      }
      ret[0][0] = 'c';
      return ret;
    }
    if (r >= 3 && c >= 3 && f <= (r-1)*(c-1)
	&& (f % 2 == 0 || (r > 3 && c > 3))
	&& (f == 4 || f == 6 || f >= 8)) {
      int h = r - 1;
      int w = c - 1;
      while (2*(h+w-2) > f) {
	if (h >= w)
	  --h;
	else
	  --w;
      }
      int extra = f - 2*(h+w-2);
      for (int x = 0; x < h; ++x) {
	for (int y = 0; y < w; ++y) {
	  if (x < 2 || y < 2)
	    ret[x][y] = '.';
	  else if (extra > 0) {
	    --extra;
	    ret[x][y] = '.';
	  }
	}
      }
      ret[0][0] = 'c';
      return ret;
    }
    vector<string> imp(1, "Impossible");
    return imp;
  }
};

int main(int argc, char ** argv) {
    string s;
    int N;
    getline(cin, s);
    {
        stringstream A(s);
        A >> N;
    }
    for (int no = 1; no <= N; ++no) {
        cerr << "Case " << no << " / " << N << endl;
        Solver solver;
        // *** get input ***
        getline(cin, s);
        int r, c, m;
        {
            stringstream A(s);
            A >> r >> c >> m;
        }
        ret_t ret = solver.solve(r, c, m);

        // *** give output ***
        //cout << "Case #" << no << ": " << ret << endl; // one line
	cout << "Case #" << no << ":" << endl; for (int i = 0; i < ret.size(); ++i) cout << ret[i] << endl; // string vector
        //cout << "Case #" << no << ":\n" << ret; // multi-line
        //cout << "Case #" << no << ": " << fixed << setprecision(7) << ret << endl; // float
    }
    return 0;
}

#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <bitset>
#include <complex>
#include <deque>
#include <functional>
#include <iostream>
#include <iterator>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <utility>
#include <valarray>
#include <vector>
#include <ext/algorithm>
#include <ext/hash_map>
#include <ext/hash_set>
#include <ext/numeric>
using namespace std;
using namespace __gnu_cxx;

#define F(i,a,b)for(int i=a;i<b;++i)
#define rep(i,n)F(i,0,n)
#define all(a)a.begin(),a.end()
template<class T>vector<T>&operator<<(vector<T>& v,T t){v.push_back(t);return v;} 

char board[4][4];

int main() {
  int T;
  cin >> T;
  rep(t, T) {
    string s;
    rep(i, 4) rep(j, 4) {
      cin >> board[i][j];
    }

    bool complete = true;
    bool xwin, owin;
    rep(i, 4) {
      bool xwin = true;
      bool owin = true;
      rep(j, 4) {
        if (board[i][j] == 'X') {
          owin = false;
        } else if (board[i][j] == 'O') {
          xwin = false;
        } else if (board[i][j] == 'T') {
        } else if (board[i][j] == '.') {
          complete = false;
          owin = false;
          xwin = false;
        } else {
          assert(false);
        }
      }
      if (xwin) {
        s = "X won";
        goto done;
      } else if (owin) {
        s = "O won";
        goto done;
      } 
    }

    rep (j, 4) {
      bool xwin = true;
      bool owin = true;
      rep(i, 4) {
        if (board[i][j] == 'X') {
          owin = false;
        } else if (board[i][j] == 'O') {
          xwin = false;
        } else if (board[i][j] == 'T') {
        } else if (board[i][j] == '.') {
          complete = false;
          owin = false;
          xwin = false;
        } else {
          assert(false);
        }
      }
      if (xwin) {
        s = "X won";
        goto done;
      } else if (owin) {
        s = "O won";
        goto done;
      } 
    }

    xwin = owin = true;
    rep(i, 4) {
      if (board[i][i] == 'X') {
        owin = false;
      } else if (board[i][i] == 'O') {
        xwin = false;
      } else if (board[i][i] == '.') {
          owin = false;
          xwin = false;
      } 
    }
    if (xwin) {
      s = "X won";
      goto done;
    } else if (owin) {
      s = "O won";
      goto done;
    } 

    xwin = owin = true;
    rep(i, 4) {
      if (board[i][3-i] == 'X') {
        owin = false;
      } else if (board[i][3-i] == 'O') {
        xwin = false;
      } else if (board[i][3-i] == '.') {
        owin = false;
        xwin = false;
      } 
    }
    if (xwin) {
      s = "X won";
      goto done;
    } else if (owin) {
      s = "O won";
      goto done;
    } 
 
    done:
    if (!s.length()) {
      if (complete) {
        s = "Draw";
      } else {
        s = "Game has not completed";
      }
    } 

    printf("Case #%d: %s\n", t + 1, s.c_str());

  }
}

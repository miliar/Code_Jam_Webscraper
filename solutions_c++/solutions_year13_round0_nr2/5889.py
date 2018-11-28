// 2^20 brute-force i am an awful person
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


int N, M;
unsigned char board[101][101];
unsigned char scratch[101][101];

void mow(int x) {
  rep(i, N) {
    int mowlevel = (x % 2) ? 2 : 1;
    x /= 2;
    
    rep(j, M) {
      if (scratch[i][j] > mowlevel) scratch[i][j] = mowlevel;
    }
  }

  rep(j, M) {
    int mowlevel = (x % 2) ? 2 : 1;
    x /= 2;

    rep(i, N) {
      if (scratch[i][j] > mowlevel) scratch[i][j] = mowlevel;
    }
  }

}
int main() {
  memset(scratch, 100, sizeof(scratch));
  int T;
  cin >> T;
  rep(t, T) {
    cin >> N >> M;
    rep(i, N) rep(j, M) {
      int k;
      cin >> k;
      board[i][j] = k;
    }

    bool found = false;
    rep(i, (1 << (N+M))) {
      memset(scratch, 100, sizeof(scratch));
      mow(i);
      bool ok = true;
      rep(i, N) rep(j, M) {
        if (board[i][j] != scratch[i][j]) ok = false;
      }
      if (ok) {
        found = true;
        break;
      } 
    }


    printf("Case #%d: %s\n", t + 1, found ? "YES" : "NO");
  }

}

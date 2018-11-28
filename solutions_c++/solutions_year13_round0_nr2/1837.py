#include <iostream>
#include <vector>

#define rep(i, n) for(int i = 0; i < n; i++)

using namespace std;

int h, w;
int f[105][105];
int g[105][105];

bool solve() {

  rep(i, h) {
    rep(j, w) {
      g[i][j] = 100;
    }
  }

  bool can;

  for(int k = 100; k >= 1; k--) {

    rep(i, h) {
      can = true;
      rep(j, w) {
        if(f[i][j] > k) can = false;
      }

      if(can) {
        rep(j, w) {
          g[i][j] = k;
        }
      }
    }

    rep(j, w) {
      can = true;
      rep(i, h) {
        if(f[i][j] > k) can = false;
      }

      if(can) {
        rep(i, h) {
          g[i][j] = k;
        }
      }
    }

  }

  rep(i, h) {
    rep(j, w) {
      if(f[i][j] != g[i][j]) return false;
    }
  }

  return true;


}

int main() {

  int T;
  cin >> T;

  rep(t, T) {
    cin >> h >> w;

    rep(i, h) {
      rep(j, w) {
        cin >> f[i][j];
      }
    }

    cout << "Case #" << (t + 1) << ": " << (solve() ? "YES" : "NO") << endl;
  }

  return 0;
}

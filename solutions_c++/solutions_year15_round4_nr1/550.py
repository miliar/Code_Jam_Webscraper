#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <map>
#include <set>
#include <sstream>
#include <queue>
#include <stack>
#include <algorithm>
using namespace std;
typedef vector<int> VI;
typedef vector<VI> MI;
typedef pair<int,int> II;
typedef vector<II> VII;
typedef vector<VII> MII;
typedef long long ll;
typedef vector<ll> Vll;
typedef vector<Vll> Mll;
#define X first
#define Y second

const int inf = 1e9;
const double eps = 1e-9;

const int maxn = 31621;
const string tiles = ".>^<v";
const int di[5] = {0, 0, -1, 0, 1};
const int dj[5] = {0, 1, 0, -1, 0};

int main() {
  int ncase = 0;
  ios_base::sync_with_stdio(false);
  int T;
  cin >> T;
  while (T--) {
    int R, C;
    cin >> R >> C;

    MI mat(R, VI(C));
    for (int i = 0; i < R; ++i) {
      for (int j = 0; j < C; ++j) {
        char c;
        cin >> c;
        for (int k = 0; k < 5; ++k) {
          if (c == tiles[k]) mat[i][j] = k;
        }
      }
    }


    bool possible = true;
    int ans = 0;
    for (int i = 0; i < R; ++i) {
      for (int j = 0; j < C; ++j) {
        if (mat[i][j]) {
          int k = mat[i][j];
          bool reach = false;
          int ni = i + di[k], nj = j + dj[k];
          while (!reach && ni >= 0 && ni < R && nj >= 0 && nj < C) {
            if (mat[ni][nj] != 0) reach = true;
            ni += di[k];
            nj += dj[k];
          }

          if (!reach) {
            //search other directions to change
            
            for (int dir = 1; !reach && dir < 5; ++dir) if (dir != k) {
              ni = i + di[dir];
              nj = j + dj[dir];
              while (!reach && ni >= 0 && ni < R && nj >= 0 && nj < C) {
                if (mat[ni][nj] != 0) reach = true;
                ni += di[dir];
                nj += dj[dir];
              }
            }
            if (!reach) possible = false;
            ++ans;
          }
        }
      }
    }
    cout << "Case #" << ++ncase << ": ";
    if (possible) cout << ans << endl;
    else cout << "IMPOSSIBLE" << endl;
    
  }
}

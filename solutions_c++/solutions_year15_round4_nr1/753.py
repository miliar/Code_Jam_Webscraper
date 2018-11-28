

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <unordered_map>

#define rep(i,n) for (int i=0; i<(n); i++)
#define repf(i,a,b) for (int i=(a); i<=(b); i++)
#define repb(i,a,b) for (int i=(a); i>=(b); i--)

#define D(x) cout << #x << " = " << x << endl;
#define endl '\n'

using namespace std;

typedef long long int LL;

template<class T>
ostream& operator<<(ostream& a, const vector<T>& v) {
    a << "{";
    if (v.size()>0) a << v[0];
    for (int i=1; i<v.size(); i++) a << ", " << v[i];
    a << "}";
    return a;
}

unordered_map<char,pair<int,int>> delta { {'<',{0,-1}}, 
  {'>',{0,1}}, {'^',{-1,0}}, {'v',{1,0}} };

int minCost(const vector<string>& board, int R, int C) {
  int ans = 0;
  for (int i=0; i<R; i++) {
    for (int j=0; j<C; j++) {
      if (board[i][j] != '.') {
        bool possible = false;
        for (int k=1; ; k++) {
          int nr = i + k*delta[board[i][j]].first;
          int nc = j + k*delta[board[i][j]].second;
          if (nr<0 || nr>=R || nc<0 || nc>=C) break;
          if (board[nr][nc] != '.') {
            possible=true;
            break;
          }
        }
        if (possible) continue;
        for (int col=0; col<C; col++) {
          if (board[i][col] != '.' && col!=j) {
            ans++;
            possible = true;
            break;
          }
        }
        if (possible) continue;
        for (int row=0; row<R; row++) {
          if (board[row][j] != '.' && row!=i) {
            ans++;
            possible=true;
            break;
          }
        }
        if (!possible) return -1;
      }
    }
  }
  return ans;
}

int main() {
    cin.sync_with_stdio(false);
    cout.sync_with_stdio(false);
    cin.tie(NULL);
    int TC,R,C;
    cin >> TC;
    for (int tc=1; tc<=TC; tc++) {
      cin >> R >> C;
      vector<string> board(R);
      rep(i,R) cin >> board[i];
      int ans = minCost(board,R,C);
      cout << "Case #" << tc << ": ";
      if (ans == -1) cout << "IMPOSSIBLE" << endl;
      else cout << ans << endl;
    }
}



#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cassert>

#define rep(i,n) for (int i=0; i<(n); i++)
#define repf(i,a,b) for (int i=(a); i<=(b); i++)
#define repb(i,a,b) for (int i=(a); i>=(b); i--)

#define D(x) cout << #x << " = " << x << endl;
#define endl '\n'

#define RICH "RICHARD"
#define GAB "GABRIEL"

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

//assume always R <= C
string solve(int X, int R, int C) {
  //if X is bigger than 7, make a hole in the middle
  if (X >= 7) return RICH;
  //if X doesn't divide R*C, it is impossible for GAB for any figure
  if ( ((R*C) % X) != 0 ) return RICH;
  //Now check that the board is big enough to fit any figure RICH chooses
  //And RICH will try to put only L shaped ominoes trying to overflow the board
  int r,c;
  for (c=X; c>=0; c--) {
    r = X-c+1;
    if (c < r) {
      c++;
      break;
    }
    if (c>C || r>R) return RICH;
  }
  r = X-c+1;
  //if there is no way to cut left side and right side, GAB can always win
  if (r < R) return GAB;
  assert(r==R);
  //Otherwise r==R and RICH should try to cut communication between left and right side
  //leaving a non X multiple at each side. I claim that trying only T shaped tiles is correct
  for (int offset=0; 2*offset<c; offset++) {
    int a = r, b = offset*(r-1);
    bool rich_wins = true;
    for (int k=0; k<X; k++) {
      if ( ((a*k + b) % X) == 0 ) {
        if ((k+c) <= C) rich_wins = false;
      }
    }
    if (rich_wins) return RICH;
  }
  //If there is no possible T shape that cuts communication between left and right, GAB wins
  return GAB;
}

int main() {
    cin.sync_with_stdio(false);
    cout.sync_with_stdio(false);
    cin.tie(NULL);
    int TC,X,R,C;
    cin >> TC;
    for (int tc=1; tc<=TC; tc++) {
      cin >> X >> R >> C;
      string ans = solve(X,min(R,C),max(R,C));
      cout << "Case #" << tc << ": " << ans << endl;
    }
}

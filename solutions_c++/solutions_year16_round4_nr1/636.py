#define NDEBUG
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;


string memo[256][12];

const string& calc(char winner, int n) {
  string& ret = memo[int(winner)][n];
  if (!ret.empty()) {
    return ret;
  }

  if (n == 0) {
    return ret = string(1, winner);
  }
  char opp =
    winner == 'R' ? 'S' :
    winner == 'S' ? 'P' : 'R';
  const string& sub1 = calc(winner, n-1);
  const string& sub2 = calc(opp, n-1);
  ret = min(sub1+sub2, sub2+sub1);
  return ret;
}

int main() {
  ios_base::sync_with_stdio(false);

  int T;
  cin >> T;
  for (int tt=1; tt<=T; ++tt) { // caret here
    int N;
    vector<int> cnts(256);
    cin >> N >> cnts['R'] >> cnts['P'] >> cnts['S'];
    string ans;
    for (int i=0; i<3; ++i) {
      const string& rv = calc("PRS"[i], N);
      vector<int> rescnts(256);
      for (char ch : rv) {
        ++rescnts[ch];
      }
      if (cnts == rescnts) {
        if (ans.empty() || rv < ans) {
          ans = rv;
        }
      }
    }
    cout << "Case #" << tt << ": " << (ans.empty() ? "IMPOSSIBLE" : ans) << endl;
  }
}

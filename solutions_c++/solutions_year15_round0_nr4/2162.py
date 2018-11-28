#include<iostream>
#include<algorithm>
#include<cassert>

using namespace std;
const string Ga = "GABRIEL";
const string Ri = "RICHARD";

int main() {
  int T;
  int X,R,C;
  cin >> T;

  for(int t = 1; t <= T; ++t) {
    cin >> X >> R >> C;
    string ans;

    if(R > C) {
      swap(R, C);
    }
    assert(R <= C);

    if(X == 4) {
      if((R*C) % 4 != 0) ans = Ri;
      else {
        if(R == 1) ans = Ri;
        else if(R == 2) ans = Ri;
        else if(R == 3) {
          if(C == 4) ans = Ga;
          else ans = Ri;
        } else {
          assert(R == 4);
          ans = Ga;
        }
      }
    } else if(X == 3) {
      if((R*C) % 3 != 0) ans = Ri;
      else {
        if(R == 1) ans = Ri;
        else if(R == 2) ans = Ga;  // 2x3
        else if(R == 3) {
          ans = Ga;  // 3x3, 3x4
        } else {
          assert(R == 4);
          ans = Ri;
        }
      }
    } else if(X == 2) {
      if((R*C) % 2 != 0) ans = Ri;
      else {
        ans = Ga;
      }
    } else {
      assert(X == 1);
      ans = Ga;
    }

    cout << "Case #" << t << ": " << ans;
    if(t < T) cout << "\n";
  }

  return 0;
}

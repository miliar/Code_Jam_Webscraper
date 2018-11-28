#include<iostream>
#include<vector>

using namespace std;

int T, x, r, p,d;

int main() {
  cin >> T;
  for(int t=1; t<=T; ++t) {
    vector<int> v(20);
    cin >> r;
    for(int i=1; i<=4; ++i)
      for(int j=1; j<=4; ++j) {
        cin >> x;
        if (i == r) ++v[x];
      }
    
    cin >> r;
    for(int i=1; i<=4; ++i)
      for(int j=1; j<=4; ++j) {
        cin >> x;
        if (i == r) ++v[x];
      }

    p = 0;
    d = 0;
    for(int i=0; i<(int)v.size(); ++i) if (v[i] == 2) {
      d = i;
      ++p;
    }

    cout << "Case #" << t << ": ";
    if (p == 0) cout << "Volunteer cheated!" << endl;
    if (p == 1) cout << d << endl;
    if (p > 1) cout << "Bad magician!" << endl;

  }
  return 0;
}

#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>
using namespace std;

void subtr(int i, vector<int> &v, int level) {
  if (level == 0) {
    v[i] -= 1;
  } else {
    subtr(i, v, level - 1);
    subtr((i+1)%3, v, level - 1);
  }
}

string s = "PRS";
string disp(int i, int level) {
  if (level == 0) {
    return s.substr(i, 1);
  } else {
    int a = i, b = (i+1)%3;
    string x = disp(a, level - 1);
    string y = disp(b, level - 1);
    if (x > y) swap(x, y);
    return x + y;
  }
}

bool check(int i, int a, int b, int c, int level) {
  vector<int> v; v.push_back(a);v.push_back(b); v.push_back(c);
  subtr(i, v, level);
  return v[0] == 0 && v[1] == 0 && v[2] == 0;
}

string print(int i, int level) {
  return disp(i, level);
}


int T;
int N, A, B, C;
int main() {
  cin >> T;
  for(int t = 1; t <= T; ++t) {
    cin >> N >> B >> A >> C;
    string ans = "IMPOSSIBLE";
    cout << "Case #" << t << ": ";
    for(int i = 0; i < 3; ++i) {
      if (check(i, A, B, C, N)) {
        ans = print(i, N);
      }
    }
    cout << ans << "\n";
  }
}

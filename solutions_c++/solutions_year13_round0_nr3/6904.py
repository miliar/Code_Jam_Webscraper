#include <iostream>
#include <sstream>
#include <algorithm>
using namespace std;

inline bool is_pal(int x) {
  stringstream ss; 
  ss << x;
  string s;
  ss >> s;
  bool pal = true;
  for (int j =0; j < s.size() / 2; ++j) {
    pal = pal && s[j]==s[s.size()-j-1];
  }
  return pal;
}
int main() {
  int T, A, B;
  cin >> T;
  int p[1001];
  int n_pal =0;
  for (int i =0; i < 1001; ++i) {
    if (is_pal(i)) {
      p[n_pal++] = i;
    }
  }
  for (int t=0; t < T; ++t) {
    cin >> A >> B;
    int res = 0;
    for (int i = A; i <= B; ++i) {
      if (!is_pal(i)) continue;
      for (int j = 0; j < n_pal && p[j] * p[j] <= i; ++j) {
        if (p[j] * p[j] == i) {
          ++res;
        }
      } 
    }
    cout << "Case #" << t+1 << ": " << res << endl;
  }
  
  return 0;
}

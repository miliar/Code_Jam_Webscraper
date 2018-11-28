#include <algorithm>
#include <iostream>
#include <set>
#include <vector>
using namespace std;

vector<int> files;
multiset<int> spaces;

int main() {
  int T; cin >> T;
  for (int t = 1; t <= T; t++) {
    int N, X; cin >> N >> X;
    files.clear(); spaces.clear();
    for (int n = 0; n < N; n++) {
      int file; cin >> file; files.push_back(file);
    }
    sort(files.begin(), files.end(), greater<int>());
    int count = 0;
    for (int n = 0; n < N; n++) {
      int file = files[n];
      auto it = spaces.lower_bound(file);
      if (it == spaces.end()) { count++; spaces.insert(X-file); }
      else { spaces.erase(it); }
    }
    cout << "Case #" << t << ": " << count << endl;
  }
}

#include <algorithm>
#include <iostream>
#include <set>
#include <vector>

using namespace std;

int y(vector<double> a, vector<double> b) {
  int n = int(a.size());
  int score = 0;
  int left = 0, right = n-1;
  for (int i = 0; i < n; ++i) {
    if (a[i] > b[left]) {
      ++score;
      ++left;
    }
    else {
      --right;
    }
  }
  return score;
}

int z(vector<double> a, vector<double> b) {
  int n = int(a.size());
  set<double> b2(b.begin(), b.end());
  int score = 0;
  for (int i = 0; i < n; ++i) {
    set<double>::iterator it = b2.upper_bound(a[i]);
    if (it == b2.end()) {
      ++score;
      it = b2.begin();
    }
    b2.erase(it);
  }
  return score;
}

int main() {
  int T;
  cin >> T;
  for (int ca = 1; ca <= T; ++ca) {
    int n;
    cin >> n;
    vector<double> a(n), b(n);
    for (int i = 0; i < n; ++i) {
      cin >> a[i];
    }
    for (int i = 0; i < n; ++i) {
      cin >> b[i];
    }
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());
    
    cout << "Case #" << ca << ": " << y(a, b) << " " << z(a, b) << endl;
  }
}


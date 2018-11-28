#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int D;

vector<int> P;

void print_vect(vector<int> v) {
  for (int i = 0; i < v.size(); ++i)
    cout << " " << v[i];
  cout << endl;
}

int best(vector<int> v) {
  sort(v.begin(), v.end());

  //  print_vect(v);

  int m = v[v.size()-1];
  if (m == 1) return 1;


  vector<int> v2(v);

  for (int i = 0; i < v2.size(); ++i)
    if (v2[i] > 0) --v2[i];


  int res = best(v2);

  vector<int> v1(v);

  v1.pop_back();

  for (int i = 2; i <= m/2; ++i) {
    v1.push_back(i);
    v1.push_back(m - i);
    res = min(res, best(v1));
    v1.pop_back();
    v1.pop_back();
  }

  return 1 + res;
}

void solve() {
  cout << best(P) << endl;
}

int main() {
  int T;

  cin >> T;

  for (int t = 1; t <= T; ++t) {
    P.clear();

    cin >> D;

    for (int i = 0; i < D; ++i) {
      int p;
      cin >> p;
      P.push_back(p);
    }

    cout << "Case #" << t << ": ";

    solve();
  }

  return 0;
}

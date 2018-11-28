#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void print(vector<int> &a) {
  for (int i = 0; i < a.size(); i++)
    cout << a[i] << ' ';
  cout << endl;
}

int verify(vector<int> &a) {
  // print(a);
  for (int i = 1; i < a.size(); i++) {
    if (a[i] > a[i-1]) {

    } else {
      for (int j = i+1; j < a.size(); j++) {
        if (a[j] < a[j-1]) {

        } else {
          return j;
        }
      }
      return -1;
    }
  }
  return -1;
}

int simulate(vector<int> from, vector<int> &to) {
  int cnt = 0;
  for (int i = 0; i < to.size(); i++) {
    int idx_a = find(from.begin(), from.end(), to[i]) - from.begin();
    for (int j = idx_a; j > i; j--) {
      swap(from[j], from[j-1]);
      cnt++;
    }
  }
  return cnt;
}

int main() {
  int T;
  cin >> T;
  for (int CASE = 1; CASE <= T; CASE++) {
    int N;
    cin >> N;
    vector<int> a(N);
    for (int i = 0; i < N; i++)
      cin >> a[i];
    vector<int> t(a.begin(), a.end());
    sort(t.begin(), t.end());
    int res = 10000000;
    do {
      if (verify(t) == -1)
        res = min(res, simulate(a, t));
    } while (next_permutation(t.begin(), t.end()));
    cout << "Case #" << CASE << ": " << res << endl;
  }
}

#include<iostream>
#include<set>

using namespace std;

int main() {
  const int N = 4;
  int T = 0, k = 0, row_num = 0;

  cin >> T;
  for (int t=0; t<T; ++t) {
    set<int> pool;
    cin >> row_num;
    for (int i=0; i<N; ++i) {
      for (int j=0; j<N; ++j) {
        cin >> k;
        if (row_num == i+1) pool.insert(k);
      }
    }

    set<int> matches;
    cin >> row_num;
    for (int i=0; i<N; ++i) {
      for (int j=0; j<N; ++j) {
        cin >> k;
        if (row_num == i+1 && pool.find(k) != pool.end()) {
          matches.insert(k);
        }
      }
    }

    cout << "Case #" << t+1 << ": ";
    if (0 == matches.size()) {
      cout << "Volunteer cheated!" << endl;
    } else if (1 == matches.size()) {
      cout << (*matches.begin()) << endl;
    } else {
      cout << "Bad magician!" << endl;
    }
  }

  return 0;
}

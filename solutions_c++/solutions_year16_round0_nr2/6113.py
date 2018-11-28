#include <iomanip>
#include <algorithm>
#include <bitset>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

using namespace std;

template<class T>
ostream& operator<< (ostream& fout, const vector<T>& vec) {
  for (size_t i = 0; i < vec.size(); ++i) {
    fout << vec[i] << ' ';
  }
  return fout;
}

template <class T>
istream& operator>> (istream& fin, vector<T>& vec) {
  for (size_t i = 0; i < vec.size(); ++i) {
    cin >> vec[i];
  }
  return fin;
}

int count(const string& input) {
  int n = input.size();
  char prev = input[0];
  int result = 0;
  for (int i = 1; i < n; ++i) {
    if (prev != input[i]) {
      ++result;
      prev = input[i];
    }
  }
  if (prev != '+') {
    ++result;
  }
  return result;
}

int main() {
#ifndef LOCAL
  //freopen("input.txt", "rt", stdin);
  //freopen("output.txt", "wt", stdout);
#endif
#ifdef LOCAL
  freopen("input.txt", "rt", stdin);
#endif

  ios_base::sync_with_stdio(0);
  cin.tie(0);
  int test_count;
  cin >> test_count;
  for (int t = 0; t < test_count; ++t) {
    string input;
    cin >> input;
    cout << "Case #" << t + 1 << ": " << count(input) << '\n';
  }
}

#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
#include <string>

/*
10
1 10 9 8 0 7 5 4 3 2
*/

using namespace std;

long long solve(vector<long long> &A, int begin, int ud) {
  long long x;
  if (begin == A.size()) return 0;
  if (ud == 0 && begin == 0) {
    x = -1;
  }
  else {
    x = A[begin-1];
  }
  long long ret = 100000000;
  if (ud == 0) {
    for (int ii = begin; ii < A.size(); ii++) {
      if (A[ii] > x) {
        vector<long long> dup = A;
        long long newret = 0;
        for (int jj = ii; jj > begin; jj--) {
          long long tmp = dup[jj];
          dup[jj] = dup[jj-1];
          dup[jj-1] = tmp;
        }
        newret+= ii - begin;
        newret += min(solve(dup, begin+1, 0), solve(dup, begin+1, 1));
        ret = min(ret, newret);
      }
    }
  }
  if (ud == 1) {
    for (int ii = begin; ii < A.size(); ii++) {
      if (A[ii] < x) {
        vector<long long> dup = A;
        long long newret = 0;
        for (int jj = ii; jj > begin; jj--) {
          long long tmp = dup[jj];
          dup[jj] = dup[jj-1];
          dup[jj-1] = tmp;
        }
        newret+= ii - begin;
        newret += solve(dup, begin+1, 1);
        ret = min(ret, newret);
      }
    }
  }
  return ret;
}

int main() {
  long long T;
  cin >> T;

  for (long long ii = 1; ii <= T; ii++) {
    cout << "Case #" << ii << ": ";
    long long N;
    cin >> N;
    vector<long long> A;
    for (int ii = 0; ii < N; ii++) {
      long long x;
      cin >> x;
      A.push_back(x);
    }
    cout << solve(A, 0, 0) << endl;
  }
}

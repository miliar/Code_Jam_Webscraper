#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <algorithm>

using namespace std;

void go(int* a) {
  int arr[4][4];
  int ans; cin >> ans; ans--;
  for (int i = 0; i < 4; i++) for (int j = 0; j < 4; j++) cin >> arr[i][j];
  for (int j = 0; j < 4; j++) a[j] = arr[ans][j];
}

int go(const int* a, const int* b) {
  int res = 0;
  for (int i = 0; i < 4; i++) {
    for (int j = 0; j < 4; j++) if (a[i] == b[j]) {
      if (res == 0)
        res = a[i];
      else
        return -1;
    }
  }
  return res;
}

int main() {
  int testCases; cin >> testCases;
  for (int caseNo = 1; caseNo <= testCases; caseNo++) {
    int a[4], b[4];
    go(a); go(b);
    int res = go(a, b);
    cout << "Case #" << caseNo << ": ";
    if (res > 0)
      cout << res << endl;
    else if (res == 0)
      cout << "Volunteer cheated!" << endl;
    else
      cout << "Bad magician!" << endl;
  }
  return 0;
}

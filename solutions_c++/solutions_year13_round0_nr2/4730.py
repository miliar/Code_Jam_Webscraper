#include <iostream>
#include <stdio.h>
#include <set>
#include <iterator>
#include <memory.h>
using namespace std;
int n, m;
int a[200][200];
bool xInvalid[200];
bool yInvalid[200];
set<int> height;
string judge() {
  set<int>::reverse_iterator it = height.rbegin();
  memset(xInvalid, 0, sizeof(xInvalid));
  memset(yInvalid, 0, sizeof(yInvalid));
  for (; it != height.rend(); it++) {
    int nowHeight = *it;
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
	if (a[i][j] >= nowHeight) {
	  xInvalid[i] = true;
	  yInvalid[j] = true;
	}
      }
    }
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
	if (a[i][j] < nowHeight && xInvalid[i] && yInvalid[j]) {
	  return "NO";
	}
      }
    }
  }
  return "YES";
}
int main() {
    int T, t = 0;
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    cin >> T;
    while(T--) {
      height.clear();
      cin >> n >> m;
      for (int i = 0; i < n; i++) {
	for (int j = 0; j< m; j++) {
	  cin >> a[i][j];
	  height.insert(a[i][j]);
	}
      }
      string res = judge();
      cout << "Case #" << ++t << ": " << res << endl;
    }
}

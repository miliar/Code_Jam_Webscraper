#include <bits/stdc++.h>

using namespace std;

#define F first
#define S second
#define FILE "test"

int n;
vector<int> a;

void read() {
  a.clear();
  cin >> n;
  a.resize(n);
  for (int i = 0; i < n; i++) {
    scanf("%d", &a[i]);
  }
}

void solve(int num) {
  cout << "Case #" << num << ": ";
  //
  int sum = 0;
  for (int i = 0; i < n; i++) {
    sum += a[i];
  }
  while (sum) {
    // two;
    bool f = false;
    for (int i = 0; i < n; i++) {
      if (f) break;
      for (int j = i + 1; j < n; j++) {
        if (f) break;
        if (a[i] == 0 || a[j] == 0) continue;
        a[i]--;
        a[j]--;
        int mx = 0;
        for (int w = 0; w < n; w++) {
          mx = max(mx, a[w]);
        }
        if (mx * 2 <= sum - 2) {
          f = true;
          cout << (char)(i + 'A') << (char)(j + 'A') << " ";
          sum -= 2;
          break;
        } else {
          a[i]++;
          a[j]++;
        }
      }
    }
    if (f) continue;
    for (int i = 0; i < n; i++) {
      if (a[i] == 0) continue;
      if (f) break;
      a[i]--;
      int mx = 0;
      for (int w = 0; w < n; w++) {
        mx = max(mx, a[w]);
      }
      if (sum - 1 >= mx * 2) {
        f = true;
        cout << (char)(i + 'A') << " ";
        sum--;
        break;
      } else {
        a[i]++;
      }
    }
  }
  //
  cout << endl;
}
int main() {
  freopen(FILE".in", "r", stdin);
  freopen(FILE".out", "w", stdout);
  int t;
  int k = 1;
  cin >> t;
  while (t--) {
    read();
    solve(k);
    k++;
  }
  return 0;
}

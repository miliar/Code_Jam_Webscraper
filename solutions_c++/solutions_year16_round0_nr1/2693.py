#include <bits/stdc++.h>

using namespace std;

int arr[10];

int main() {
  int n;
  cin >> n;
  for (int i = 0; i < n; ++i) {
    int a;
    cin >> a;
    memset(arr, 0, sizeof arr);
    int all = 0;
    int ans = 0;
    int aux = a;
    if (!a) {
      cout << "Case #" << (i + 1) << ": INSOMNIA\n";
      continue;
    }
    while (all < 10) {
      ++ans;
      aux = a * ans;
      while(aux) {
        if (!arr[aux % 10]) {
          arr[aux % 10] = 1;
          ++all;
        }
        aux /= 10;
      }
    }
      cout << "Case #" << (i + 1) << ": " << (ans * a) << endl;
  }
  return 0;
}

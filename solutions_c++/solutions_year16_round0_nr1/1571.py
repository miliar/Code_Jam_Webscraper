#include <iostream>
#include <vector>
using namespace std;
void work(long long now, vector<bool> &vis, int &cnt) {
  while (now) {
    int digit = now % 10;
    if (!vis[digit]) {
      vis[digit] = true;
      cnt++;
    }
    now /= 10;
  }
}
int main() {
  int tk;
  cin >> tk;

  for (int tk1 = 1; tk1 <= tk; tk1++) {
    long long n;
    cin >> n;
    cout << "Case #" << tk1 << ": ";

  //for (long long n = 0; n <= 1000000; n++) {
    if (n == 0) {
      cout << "INSOMNIA" << endl;
      continue;
    }
    int cnt = 0;
    vector<bool> vis(10);
    int i;
    for (i = 0; true; i++) {
      long long now = n * i;
      work(now, vis, cnt);
      if (cnt == 10) {
        break;
      }
    }
    //cout << n << "\t";
    cout << n * i << endl;

  }
  return 0;
}

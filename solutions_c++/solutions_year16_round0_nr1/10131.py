#include<bits/stdc++.h>
using namespace std;

#define endl '\n'
#define D(x) cout << #x << " = " << (x) << endl;

void count(long long x, vector<int> &v) {
  while (x > 0) {
    v[x%10] = true;
    x /= 10;
  }
}

int main() {
  int TC = 1;
  long long n;
  int t;
  cin >> t;
  while (t --> 0) {
    cin >> n;
    vector<int> v(10, 0);
    int good = false;
    long long ans = 0;
    for (int i = 1; i <= 1000000; ++i) {
      long long cur = n * i;
      count(cur, v);
      int tot = accumulate(v.begin(), v.end(), 0);
      
      if (tot == 10) {
        ans = cur;
        good = true;
        break;
      }
    }

    cout << "Case #" << TC++ << ": ";
    if (good) {
      cout << ans << endl;
    } else cout << "INSOMNIA" << endl;
  }
  
  return 0;
}

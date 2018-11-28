#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

int solve(int n, int t)
{
  vector<int> v(10, 0);
  if (n == 0) return -1;

  int k = n;
  for (int i = 0; i < 100000; ++i) {
    int tmp = k;

    /*
    for(int p: v) {
      cout << p << ",";
    }
    cout << endl;
    */

    if (tmp > 9) {
      while (true) {
        int c = tmp % 10;
        v[c] = 1;
        tmp = tmp / 10;
        if (tmp < 10) {
          v[tmp] = 1;
          break;
        }
      }
    } else {
      v[tmp] = 1;
    }

    int sum_of_elems = std::accumulate(v.begin(), v.end(), 0);
    if (sum_of_elems == 10) {
      break;
    }

    k += n;
  }

  return k;
}

int main() {
  int t, n, ans;
  cin >> t;
  for (int i = 0; i < t; i++) {
    cin >> n;
    ans = solve(n, t);
    if (ans == -1) {
      cout << "Case #" << (i + 1) << ": INSOMNIA" << endl;
    } else {
      cout << "Case #" << (i + 1) << ": " << ans << endl;
    }
  }
}

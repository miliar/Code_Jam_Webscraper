#include <iostream>
#include <vector>
using namespace std;

int solve_case() {
  int n;
  cin >> n;
  ++n;
  vector<int> v(n);
  for (int i = 0; i < n; ++i) {
    char c;
    cin >> c;
    v[i] = c - '0';
  }

  int qtt = 0, res = 0;
  for (int i = 0; i < n; ++i) {
    if (qtt < i) {
      res += i - qtt;
      qtt = i;
    }
    qtt += v[i];
  }
  return res;
}

int main() {
  int casos;
  cin >> casos;
  for (int cas = 1; cas <= casos; ++cas) {
    cout << "Case #" << cas << ": " << solve_case() << endl;
  }
}

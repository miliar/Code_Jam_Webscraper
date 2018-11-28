#include <iostream>
#include <string>

using namespace std;

int main()
{
  int T, n;
  string A;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    cin >> n >> A;
    int req = 0, total = A[0] - '0';
    for (int i = 1; i <= n; i++) {
      if (total < i) {
        req += i - total;
        total = i;
      }
      total += A[i] - '0';
    }
    cout << "Case #" << t << ": " << req << '\n';
  }

  return 0;
}

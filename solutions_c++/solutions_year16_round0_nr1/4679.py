#include <iostream>
#include <sstream>
#include <cassert>

using namespace std;

typedef long long ll;

void solve(int N)
{
  if (N == 0) {
    cout << "INSOMNIA" << endl;
    return;
  }

  int mask = 0;
  int step = 1;
  ll last = N;
  while (true) {
    ostringstream oss;
    oss << last;
    for (auto c : oss.str()) {
      mask |= (1 << (c - '0'));
    }
    if (mask == (1 << 10) - 1) {
      cout << last << endl;
      return;
    }
    last += N;
    step++;
    assert(step <= 100);
  }

}

int main()
{
  int T;
  cin >> T;
  for (int i = 1; i <= T; i++) {
    cout << "Case #" << i << ": ";
    int N;
    cin >> N;
    solve(N);
  }

  return 0;
}

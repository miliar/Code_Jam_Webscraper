#include <iostream>
#include <bitset>
using namespace std;

int solve(long long N)
{
  int i;
  bitset<10> b;
  for (i = 1; ; i++) {
    long long sheep = N * i;
    while (sheep != 0) {
      int remaining = sheep % 10;
      b.set(remaining, 1);
      sheep = sheep / 10;
    }
    if (b.all()) break;
  }
  return N * i;
}

int main(int argc, char *argv[])
{
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    long long N;
    cin >> N;
    if (N == 0) {
      cout << "Case #" << t << ": " << "INSOMNIA" << endl;
      continue;
    }
    int res = solve(N);
    cout << "Case #" << t << ": " << res << endl;
  }
  return 0;
}


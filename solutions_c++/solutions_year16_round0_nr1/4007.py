#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int solve(int N) {
  if (N == 0) return -1;

  vector<int> count(10, 0);
  unsigned long long n = N, prev = 0;

  bool good = false;
  while (prev < n && !good) {
    prev = n;
    unsigned long long v = n;

    while (v) {
      count[v % 10] += 1;
      v /= 10;
    }

    good = true;
    for (int i = 0; i < 10; ++i) {
      if (count[i] == 0) {
        good = false;
        break;
      }
    }
    n += N;
  }

  if (good) return n-N;
  return -1;
}

int main(int argc, char* argv[]) {
  if (argc < 2) return 1;
  ifstream ifs(argv[1]);

  int T;
  ifs >> T;

  for (int i = 0; i < T; ++i) {
    int N;
    ifs >> N;

    int ret = solve(N);
    if (ret > 0) {
      cout << "Case #" << i+1 << ": " << ret << endl;
    } else {
      cout << "Case #" << i+1 << ": " << "INSOMNIA" << endl;
    }
  }

  return 0;
}

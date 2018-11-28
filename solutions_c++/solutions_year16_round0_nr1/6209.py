#include <iostream>
#include <set>

using namespace std;

void print_output(long long res, int it) {
  cout << "Case #" << it << ": ";
  if (res == 0) {
    cout << "INSOMNIA\n";
  } else {
    cout << res << "\n";
  }
}

int main() {
  int nt;
  cin >> nt;
  for (int it = 1; it <= nt; it++) {
    long long n;
    cin >> n;
    if (n == 0) {
      print_output(0, it);
      continue;
    }

    set<int> seen;
    long long curr = 0;
    while (seen.size() < 10) {
      curr += n;
      long long tmp = curr;
      while (tmp > 0) {
        seen.insert(tmp % 10);
        tmp = tmp / 10;
      }
    }
    print_output(curr, it);
  }
  return 0;
}

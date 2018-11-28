#include <iostream>
#include <set>

using namespace std;

void add_digits(int n, set<int>& s) {
  while (n > 0) {
    s.insert(n % 10);
    n /= 10;
  }
}

void solve(int n) {
  if (n == 0) {
    cout << "INSOMNIA" << endl;
    return;
  }

  int i = 1;
  set<int> s;
  while (true) {
    add_digits(n * i, s);
    if (s.size() == 10) {
      cout << n*i << endl;
      break;
    }
    i++;
  }

}

int main() {
  int N;
  cin >> N;
  for (int i = 0; i < N; i++) {
    int n;
    cin >> n;
    cout << "Case #" << (i+1) << ": ";
    solve(n);
  }

  return 0;
}

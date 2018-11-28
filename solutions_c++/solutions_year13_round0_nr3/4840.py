#include <iostream>
#include <cstdio>
#include <map>

using namespace std;

bool is_fair(unsigned long long i) {
  string s = to_string(i);
  int n = s.size();

  bool pal = true;
  for (int i = 0; i < n; ++i) {
    if (s[i] != s[n-i-1]) {
      pal = false;
    }
  }
  return pal;
}

int main(int argc, char *argv[]) {
  int n;
  int lower_b, upper_b;
  int counter;

  freopen(argv[1], "r", stdin);

  cin >> n;

  for (int c = 1; c <= n; ++c) {
    cout << "Case #" << c << ": ";

    cin >> lower_b;
    cin >> upper_b;

    counter = 0;

    for (unsigned long long i = 1; i*i <= upper_b; ++i) {
      if (i * i < lower_b) continue;
      if (is_fair(i) && is_fair(i*i)) {
        counter++;
      }
    }
    cout << counter;

    cout << endl;
  }

  return 0;
}

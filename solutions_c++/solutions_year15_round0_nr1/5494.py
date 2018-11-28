#include <iostream>
#include <iomanip>

using namespace std;

void run(int t) {
  int maxS;
  string a;
  cin >> maxS >> a;
  int add = 0;
  int standing = 0;
  for (int i = 0; i <= maxS; i++) {
    if (i > standing) {
      add += i - standing;
      standing = i;
    }
    standing += a[i] - '0';
  }
  cout << "Case #" << t << ": " << add << endl;
}

int main() {
  cout << setprecision(7) << fixed;
  int T; cin >> T;
  for (int t = 1; t <= T; t++) {
    run(t);
  }
}

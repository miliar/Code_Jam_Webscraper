#include <string>
#include <iostream>

using namespace std;

int main () {
  int t;
  cin >> t;
  for (int tt = 1; tt <= t; tt++) {
    int n;
    string s;
    cin >> n >> s;
    int friends = 0;
    int standing = 0;
    for (int i = 0; i <= n; i++) {
      int r = s[i] - '0';
      while (i > standing) {
        standing++;
        friends++;
      }
      standing += r;
    }

    cout << "Case #" << tt << ": " << friends << endl;
  }
}


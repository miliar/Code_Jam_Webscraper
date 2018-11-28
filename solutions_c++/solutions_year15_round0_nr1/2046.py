#include <iostream>
#include <string>

using namespace std;

int main() {
  ios::sync_with_stdio(false);

  int tc;
  cin >> tc;

  for (int t = 1; t <= tc; t++) {
    cout << "Case #" << t << ": ";

    int n;
    string cnts;
    cin >> n >> cnts;

    int standing = 0;
    int added = 0;

    for (int i = 0; i < cnts.size(); i++) {
      if (cnts[i] > '0' && standing < i) {
        added += i - standing;
        standing = i;
      }
      standing += cnts[i] - '0';
    }

    cout << added << '\n';
  }

  return 0;
}

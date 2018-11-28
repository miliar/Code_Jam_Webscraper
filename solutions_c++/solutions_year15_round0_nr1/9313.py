#include <iostream>
using namespace std;


char a[1024];

int main() {
  int T, S, ans, j, people;
  cin >> T;

  for (int i = 1; i <= T; i++) {
    cin >> S >> a;
    ans = 0;
    j = 0;
    people = 0;

    while (j <= S) {
      if (j > people) {
        ans += (j - people);
        people = j;
      }
      people += (a[j++] - '0');
    }

    cout << "Case #" << i << ": " << ans << endl;
  }
  return 0;
}
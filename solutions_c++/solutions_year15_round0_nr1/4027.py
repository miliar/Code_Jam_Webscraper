#include <stdlib.h>
#include <iostream>

using namespace std;

int main()
{
  int T;
  cin >> T;
  for (int count = 1; count <= T; count++) {
    int Smax;
    cin >> Smax;
    int c[2000];
    for (int i = 0; i <= Smax; i++) {
      char ch;
      cin >> ch;
      c[i] = (int) (ch - '0');
    }
    int cs = 0; // cumulative sum
    int ans = 0;
    for (int i = 0; i <= Smax; i++) {
      if (cs < i) {
        ans += (i - cs);
        cs = i;
      }
      cs += c[i];
    }
    cout << "Case #" << count << ": " << ans << "\n";
  }
  return 0;
}


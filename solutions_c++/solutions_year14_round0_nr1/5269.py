#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
  int T;
  cin >> T;
  for (int i = 1; i <= T; i++) {
    cout << "Case #" << i << ": ";
    bool possible[17];
    fill(possible, possible+17, true);

    for (int t = 0; t < 2; t++) {
      int R;
      cin >> R;
      for (int r = 1; r <= 4; r++) {
	for (int c = 1; c <= 4; c++) {
	  int x;
	  cin >> x;
	  if (r != R) possible[x] = false;
	}
      }
    }

    int c = count(possible+1, possible+17, true);
    if (c == 1) {
      cout << (find(possible+1, possible+17, true) - possible) << endl;
    } else if (c == 0) {
      cout << "Volunteer cheated!" << endl;
    } else {
      cout << "Bad magician!" << endl;
    }
  }
  return 0;
}

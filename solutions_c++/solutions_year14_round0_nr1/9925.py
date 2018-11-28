#include <iostream>
#include <set>

using namespace std;

int main() {
  int t, x, y;
  cin >> t;
  for (int w = 1; w <= t; w++) {
    set<int> s;
    int ans = -1;
    for (int lvl = 0; lvl < 2; lvl++) {
      cin >> x;
      for (int i = 0; i < 4; i++)
        for (int j = 0; j < 4; j++) {
          cin >> y;
          if (x == i + 1 && s.find(y) != s.end())
            ans = y;
          if (x == i + 1)
            s.insert(y);
        }
    }
    cout << "Case #" << w << ": ";
    if (s.size() == 8)
      cout << "Volunteer cheated!\n";
    else if (s.size() == 7)
      cout << ans << "\n";
    else
      cout << "Bad magician!\n";
    
  }
  return 0;
}

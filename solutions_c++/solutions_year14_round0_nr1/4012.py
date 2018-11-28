#include <set>
#include <iostream>
using namespace std;

int a[4][4];

void Read() {
  for (int i = 0; i < 4; ++i)
    for (int j = 0; j < 4; ++j)
      cin >> a[i][j];
}

int main() {
  int Z;
  cin >> Z;
  for (int z = 0; z < Z; ++z) {
    int x;
    cin >> x;
    Read();
    set<int> s;
    for (int i = 0; i < 4; ++i) {
      s.insert(a[x-1][i]);
    }
    cin >> x;
    Read();
    int count=0, last;
    for (int i = 0; i < 4; ++i)
      if (s.count(a[x-1][i])) {
        count++;
        last=a[x-1][i];
      }
    cout << "Case #" << 1+z << ": ";
    if (count == 0) {
      cout << "Volunteer cheated!" << endl;
    } else if (count == 1) {
      cout << last << endl;
    } else {
      cout << "Bad magician!" << endl;
    }
  }
  return 0;
}

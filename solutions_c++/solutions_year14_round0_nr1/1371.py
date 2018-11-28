#include <cmath>
#include <functional>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <unordered_map>
#include <queue>
#include <set>
using namespace std;

#define FOR(i,a,b) for (int i = (a); i < (b); ++i)
#define REP(i,n) FOR(i,0,n)

int a[5][5], b[5][5];

int main() {
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);

  int T;
  cin >> T;
  REP(tests,T) {
    cout << "Case #" << tests + 1 << ": ";
    int x, y;
    cin >> x;
    --x;
    REP(i,4) {
      REP(j,4) {
        cin>>a[i][j];
      }
    }
    cin >> y;
    --y;
    REP(i,4) {
      REP(j,4) {
        cin >> b[i][j];
      }
    }

    set<int> s;
    REP(i,4) {
      s.insert(a[x][i]);
    }
    set<int> s2;
    REP(i,4) {
      if (s.count(b[y][i])) {
        s2.insert(b[y][i]);
      }
    }
    if (s2.size() == 1) {
      cout << *s2.begin() << endl;
      continue;
    }

    if (s2.size() == 0) {
      cout << "Volunteer cheated!" << endl;
      continue;
    }

    cout << "Bad magician!" << endl;
  }
  return 0;
}
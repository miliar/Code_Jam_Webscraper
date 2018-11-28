#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int N;
char t[4][5];

int u[4];
vector<int> order;
bool doit(int i) {
  if (i == N) return true;
  int x = order[i];
  bool found = false;
  for (int j = 0; j < N; j++) if (t[x][j] != '0' && !u[j]) {
    found = true;
    u[j]++;
    bool valid = doit(i+1);
    u[j]--;
    if (!valid) return false;
  }
  return found;
}

int main() {
  int T, prob=1;
  for (cin >> T; T--;) {
    cin >> N;
    cout << "Case #" << prob++ << ": ";
    for (int i = 0; i < N; i++) cin >> t[i];

    int ret = 1000000;
    for (int b = 0; b < (1<<16); b++) {
      int cost = 0;
      for (int i = 0; i < 4; i++)
      for (int j = 0; j < 4; j++) if (b&(1<<(4*i+j))) {
        cost++;
        t[i][j]++;
      }

      bool fail = false;
      order.clear();
      for (int i = 0; i < N; i++) order.push_back(i);
      do {
        if (!doit(0)) {fail = true; break;}
      } while (next_permutation(order.begin(), order.end()));
      if (!fail) ret = min(ret, cost);

      for (int i = 0; i < 4; i++)
      for (int j = 0; j < 4; j++) if (b&(1<<(4*i+j))) {
        t[i][j]--;
      }
    }

    cout << ret << endl;
  }
}

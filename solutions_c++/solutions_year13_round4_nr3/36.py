#include <algorithm>
#include <iostream>
#include <queue>
#include <string>
#include <sstream>
#include <vector>
#include <cmath>
#include <cassert>

using namespace std;

const int MAXN = 2005;

int n;
int x[MAXN];
int y[MAXN];

int num_preds[MAXN];
vector<int> succs[MAXN];
bool done[MAXN];

int a[MAXN];

void Solve() {
  int n;
  cin >> n;

  for (int i = 0; i < n; i++) {
    cin >> x[i];
    num_preds[i] = 0;
    succs[i].clear();
  }

  for (int i = 0; i < n; i++) {
    cin >> y[i];
  }

  for (int i = 0; i < n; i++) {
    int last = -1;

    for (int j = 0; j < i; j++) {
      if (x[i] <= x[j]) {
        num_preds[j]++;
        succs[i].push_back(j);
      }

      if (x[j] + 1 == x[i]) {
        last = j;
      }
    }

    if (last != -1) {
      num_preds[i]++;
      succs[last].push_back(i);
    }
  }

  for (int i = n - 1; i >= 0; i--) {
    int last = -1;

    for (int j = n - 1; j  > i; j--) {
      if (y[i] <= y[j]) {
        num_preds[j]++;
        succs[i].push_back(j);
      }

      if (y[j] + 1 == y[i]) {
        last = j;
      }
    }

    if (last != -1) {
      num_preds[i]++;
      succs[last].push_back(i);
    }
  }

  for (int i = 0; i < n; i++) {
    done[i] = false;
  }

  for (int k = 0; k < n; k++) {
    int c;
    for (c = 0; c < n; c++) {
      if (!done[c] && num_preds[c] == 0) {
        break;
      }
    }

    assert(!done[c] && num_preds[c] == 0);
    done[c] = true;

    a[c] = k;

    for (int i : succs[c]) {
      num_preds[i]--;
    }
  }

  for (int i = 0; i < n; i++) {
    if (i > 0) {
      cout << " ";
    }
    cout << a[i] + 1;
  }

  cout << endl;
}

int main() {
  int num_cases;
  cin >> num_cases;
  for (int i = 1; i <= num_cases; i++) {
    cout << "Case #" << i << ": ";
    Solve();
  }
}

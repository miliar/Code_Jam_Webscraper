#include <iostream>
#include <algorithm>
#include <vector>
#include <cassert>
#include <map>
using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define FORI(i,a,b) for(int i=(a);i<=(b);i++)
#define REP(i,b) FOR(i,0,b)
#define all(a) (a).begin(), (a).end()

const int oo = 999999999;

typedef vector<int> vi;

void normalize(vi& values) {
  map<int, int> position;
  for(int v: values) {
    position[v] = 0;
  }
  int x = 0;
  for(auto& it: position) {
    it.second = ++x;
  }
  for(int& v: values) {
    v = position[v];
  }
}
void print_vi(const vi& values) {
    for (int i : values) {
      cerr << i << " ";
    }
    cerr << endl;
}


int solve() {
    int n;
    cin >> n;
    assert(1 <= n);

    vi values(n);
    REP(i, n) cin >> values[i];

    normalize(values);


    int totalMoves = 0;

    FOR(v, 1, n+1) {
      int i = find(all(values), v) - values.begin();
      assert(0 <= i && i < n);

      int j;
      for (j = 0; j < i; j++) {
        if (values[j] > values[i] || (j > 0 && values[j - 1] > values[j])) {
          // should move left to j
          break;
        }
      }
      const int leftDistance = i - j;
      for (j = n - 1; j > i; j--) {
        if (values[j] > values[i] || (j < n - 1 && values[j + 1] > values[j])) {
          // should move right to j
          break;
        }
      }
      const int rightDistance = j - i;
      assert(leftDistance >= 0);
      assert(rightDistance >= 0);
      if (leftDistance < rightDistance) {
        j = i - leftDistance;
        for(int k = i - 1; k >= j; k--) {
          values[k + 1] = values[k];
        }
        values[j] = v;
        totalMoves += leftDistance;
      } else {
        j = i + rightDistance;
        for(int k = i + 1; k <= j; k++) {
          values[k - 1] = values[k];
        }
        values[j] = v;
        totalMoves += rightDistance;
      }
    }
    return totalMoves;
}

int main() {
    ios::sync_with_stdio(false);
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int solution = solve();
        cout << "Case #" << (i+1) << ": " << solution << endl;
    }
}

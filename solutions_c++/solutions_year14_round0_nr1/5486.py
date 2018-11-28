#define NDEBUG
#include <algorithm>
#include <cstdio>
#include <iostream>
#include <iterator>
#include <set>
using namespace std;

#define repeat(n) for (int repc = (n); repc > 0; --repc)
#define ALL(x) (x).begin(), (x).end()

set<int> one_round() {
  int answer;
  cin >> answer;
  set<int> output;
  for (int i=1; i<=4; ++i) {
    repeat (4) {
      int x;
      cin >> x;
      if (i == answer) {
        output.insert(x);
      }
    }
  }
  return output;
}

void solve1() {
  set<int> A = one_round(), B = one_round(), C;
  set_intersection(ALL(A), ALL(B), inserter(C, C.begin()));
  if (C.size() == 1) {
    printf("%d\n", *C.begin());
  } else if (C.size() == 0) {
    puts("Volunteer cheated!");
  } else {
    puts("Bad magician!");
  }
}

int main() {
  ios_base::sync_with_stdio(false);

  int T;
  cin >> T;
  for (int tt=1; tt<=T; ++tt) {
    printf("Case #%d: ", tt);
    solve1();
  }
}

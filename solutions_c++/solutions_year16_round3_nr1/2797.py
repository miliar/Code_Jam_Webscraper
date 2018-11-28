#include <iostream>
#include <limits>
#include <bitset>
#include <algorithm>
#include <map>

using namespace std;

struct Party {
  Party() : c('A'), count(0) {}
  char c;
  int count;
};

struct Comp {
  bool operator()(const Party& s1, const Party& s2) {
    return s1.count < s2.count;
  }
};

int main() {
  std::ios::sync_with_stdio(false);
  int T; cin >> T;

  for (int i = 1; i <= T; ++i) {
    int N; cin >> N;
    vector<Party> P(N);

    int total = 0;
    for (int i=0; i<N; ++i) {
      P[i].c = static_cast<char>('A' + i);
      cin >> P[i].count;
      total += P[i].count;
    }

    make_heap(P.begin(), P.end(), Comp());
    cout << "Case #" << i << ": ";
    while(P.size() > 1) {
      Party p = P.front();
      pop_heap(P.begin(), P.end(), Comp()); P.pop_back();
      Party n = P.front();
      if (p.count - n.count >= 2) {
        cout << p.c << p.c;
        p.count -= 2;
        if (p.count > 0) {
          P.push_back(p); push_heap(P.begin(), P.end(), Comp());
        }
      } else if (p.count - n.count >= 1) {
        cout << p.c;
        p.count -= 1;
        if (p.count > 0) {
          P.push_back(p); push_heap(P.begin(), P.end(), Comp());
        }
      } else {
        if (P.size() > 1) {
          cout << p.c;
          p.count -= 1;
          if (p.count > 0) {
            P.push_back(p); push_heap(P.begin(), P.end(), Comp());
          }
        } else {
          pop_heap(P.begin(), P.end(), Comp()); P.pop_back();
          cout << p.c << n.c;
          p.count -= 1;
          n.count -= 1;
          if (p.count > 0) {
            P.push_back(p); push_heap(P.begin(), P.end(), Comp());
          }
          if (n.count > 0) {
            P.push_back(n); push_heap(P.begin(), P.end(), Comp());
          }
        }
      }
      cout << " ";
    }
    cout << endl;
  }
}

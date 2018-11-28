#include <cstdio>
#include <set>

const int MAXN = 10100;


using namespace std;

typedef multiset<int>::iterator it;
int T, N, X;

int main() {
  scanf("%d", &T);
  for(int t = 1; t <= T; ++t) {
    scanf("%d %d", &N, &X);
    multiset<int> s;
    s.insert(0);
    for(int i = 0; i < N; ++i) {
      int nxt;
      scanf("%d", &nxt);
      s.insert(nxt);
    }

    int ans = 0;
    while (!s.empty()) {
      int x = *s.rbegin();
      if (!x) break;
      s.erase(s.find(x));

      ++ans;

      if (x != X) {
        int y = X - x;
        it i = s.upper_bound(y);
        --i;
        int z = *i;
        if (z) {
          s.erase(i);
        }
      }
    }

    printf("Case #%d: %d\n", t, ans);
  }
}

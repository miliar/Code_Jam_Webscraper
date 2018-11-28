#include <cstdio>
#include <algorithm>
#include <functional>
#include <cstring>
#include <utility>
#include <vector>

#define tr(c, i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define pb push_back

using namespace std;

int main() {
  int examples;
  scanf("%d", &examples);
  for (int ex = 1; ex <= examples; ex++) {
    int N, M;
    scanf("%d%d", &N, &M);
    vector<pair<int, pair<int, int> > > v;
    for (int r = 0; r < N; r++) {
      for (int c = 0; c < M; c++) {
        int h;
        scanf("%d", &h);
        v.push_back(make_pair(h, make_pair(r, c)));
      }
    }
    sort(v.begin(), v.end(), greater<pair<int, pair<int, int> > >());
    int *row = new int[N]();
    int *col = new int[M]();
    bool flag = true;
    tr(v, i) {
      int h = i->first, r = i->second.first, c = i->second.second;
      if (row[r] == 0) row[r] = h;
      if (col[c] == 0) col[c] = h;
      if (row[r] > h && col[c] > h) {
        flag = false;
        break;
      }
    }

    // output
    printf("Case #%d: %s", ex, flag ? "YES" : "NO");
    printf("\n");
  }
}

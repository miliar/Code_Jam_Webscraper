#include <bits/stdc++.h>
#define MAXN 105
using namespace std;

typedef pair<int,int> pii;
int testcase;
int R, C;
char B[MAXN][MAXN];
vector <int> rows[MAXN], cols[MAXN];
set <pii> S;

int main () {
 // freopen("A-small-attempt0.in","r",stdin);
//  freopen("A.out","w",stdout);
  scanf("%d",&testcase);
  for (int TC=1;TC<=testcase;++TC) {
    scanf("%d%d",&R,&C);
    for (int i=1;i<=R;++i) rows[i].clear();
    for (int j=1;j<=C;++j) cols[j].clear();
    for (int i=1;i<=R;++i)
      for (int j=1;j<=C;++j) {
        scanf(" %c",&B[i][j]);
        if (B[i][j] != '.') {
          rows[i].push_back(j);
          cols[j].push_back(i);
        }
      }
    bool ok = 1;
    for (int i=1;i<=R;++i)
      for (int j=1;j<=C;++j)
        if (B[i][j] != '.') {
          if (rows[i].size() == 1 && cols[j].size() == 1) ok = 0;
        }
    S.clear();
    for (int i=1;i<=R;++i)
      if (!rows[i].empty()) {
        if (B[i][rows[i][0]] == '<') S.insert(pii(i,rows[i][0]));
        int L = rows[i].size()-1;
        if (B[i][rows[i][L]] == '>') S.insert(pii(i,rows[i][L]));
      }
    for (int j=1;j<=C;++j)
      if (!cols[j].empty()) {
        if (B[cols[j][0]][j] == '^') S.insert(pii(cols[j][0],j));
        int L = cols[j].size()-1;
        if (B[cols[j][L]][j] == 'v') S.insert(pii(cols[j][L],j));
      }
    if (ok == 0) {
      printf("Case #%d: IMPOSSIBLE\n",TC);
    }
    else printf("Case #%d: %d\n",TC,(int)S.size());
  }
}

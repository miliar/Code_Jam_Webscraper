#include <cstdio>
#include <cstdlib>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
using namespace std;

#define MOD 1000000007

int N;
vector<string> S;
vector<vector<string> > W;
long long RN, RC;

void rec(int i) {
  if (i == (int)S.size()) {
//    fprintf(stderr, "===============\n");
    long long mynodes = 0;
    for (int s = 0; s < N; s++) {
//      fprintf(stderr, "server %d:\n", s);
      set<string> nodes;
      for (vector<string>::iterator it = W[s].begin(); it != W[s].end(); ++it) {
//        fprintf(stderr, "  string '%s'\n", it->c_str());
        for (int m = 0; m <= it->size(); m++) {
          nodes.insert(it->substr(0, m));
        }
      }
//      for (set<string>::iterator it = nodes.begin(); it != nodes.end(); ++it) {
//        fprintf(stderr, "  node '%s'\n", it->c_str());
//      }
      mynodes += nodes.size();
    }
//    fprintf(stderr, "total nodes: %lld\n", mynodes);
    if (mynodes > RN) {
      RN = mynodes;
      RC = 0;
    }
    if (mynodes == RN) {
      RC++;
      if (RC == MOD) RC = 0;
    }
  } else {
    for (int s = 0; s < N; s++) {
      W[s].push_back(S[i]);
      rec(i+1);
      W[s].pop_back();
    }
  }
}

int main() {
  int T;
  scanf("%d", &T);
  for (int tc = 1; tc <= T; tc++) {
    printf("Case #%d: ", tc);

    int m;
    scanf("%d%d", &m, &N);
    S.clear();
    for (int i = 0; i < m; i++) {
      char buf[111];
      scanf("%s", buf);
      S.push_back(buf);
    }

    W.clear();
    W.resize(N);

    RN = 0;
    RC = 0;
    rec(0);

    printf("%lld %lld\n",  RN, RC);
  }
}

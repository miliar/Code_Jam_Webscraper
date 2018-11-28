#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <list>
#include <queue>
#include <set>
#include <map>
#include <numeric>
#include <utility>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;


class Node {
  public:
  Node() {};
  void addChild(Node *n) {
    children_.push_back(n);
  }

  int & salary() {
    return salary_;
  }

  int & manager() {
    return manager_;
  }

/*  int & low() {
    return low_;
  }

  int & high() {
    return high_;
  }
*/
  int cnt(int l, int h) const {
    if (salary_ > h || salary_ < l) return 0;
    int ret = 1;
    for (const Node * c : children_) {
      ret += c->cnt(l, h);
    }
    return ret;
  }
  
  void clean() {
    children_.clear();
  }
  private:
  int salary_;
  int manager_;
 // int low_;
 // int high_;
  vector<Node*> children_;
};

Node nodes[1000002];

void gen(int n, int m, int am, int cm, int rm, int s, int as, int cs, int rs) {
  nodes[0].salary() = s;
  nodes[0].manager() = -1;
  nodes[0].clean();
  for (auto i = 1; i < n; ++i) {
    s = (static_cast<long long>(s) * as + cs) % rs;
    nodes[i].salary() = s;
    m = (static_cast<long long>(m) * am + cm) % rm;
    nodes[i].manager() = m % i;
    nodes[m % i].addChild(nodes + i);
    nodes[i].clean();
  }
}

void solve() {
  int n, d;
  scanf("%d%d", &n, &d);
  int s, as, cs, rs, m, am, cm , rm;
  scanf("%d%d%d%d", &s, &as, &cs, &rs);
  scanf("%d%d%d%d", &m, &am, &cm, &rm);
  gen(n, m, am, cm, rm, s, as, cs, rs);
  int ret = 0;
  for (auto i = 0; i < n; ++i) {
    ret = max(ret, nodes[0].cnt(nodes[i].salary(), nodes[i].salary() + d));
  }
  printf("%d\n", ret);
}

int main() {
  int t;
  scanf("%d", &t);
  for (int tc = 1; tc <= t; ++tc) {
    printf("Case #%d: ", tc);
    solve();
  }
  return 0;
}

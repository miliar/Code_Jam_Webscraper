#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <set>

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

using namespace std;

typedef long long LL;

struct Node {
  LL s, e;
  Node(LL ss=0, LL ee=0): s(ss), e(ee) {}
};

bool operator<(const Node &a, const Node &b) {
  if (a.s != b.s) return a.s < b.s;
  else return a.e < b.e;
}

LL cal(LL x, LL n) {
  if (x==0)
    return 0;
  return x*(2*n-x+1)/2;
}

int main() {
	freopen("A-small-attempt0.in", "r", stdin);
  freopen("A-small-attempt0.out", "w", stdout);

  int T;
  cin >> T;
  for (int cas = 1; cas <= T; cas++) {
    LL n, m, s, e, p;
    cin >> n >> m;
    LL old_val = 0;
    vector<Node> node_vec;
    for (int i = 0; i < m; i++) {
      cin >> s >> e >> p;
      LL x = e - s;
      old_val += cal(x, n) * p;

      for (int j = 0; j < p; j++)
        node_vec.push_back(Node(s, e));
    }

    sort(node_vec.begin(), node_vec.end());
    LL new_val = 0;
    for (int i = node_vec.size()-1; i >=0; i--) {
      LL e = node_vec[i].e;
      for (int j = i-1; j>=0; j--) {
        if (node_vec[j].e >= node_vec[i].s && node_vec[j].e < e) {
          swap(e, node_vec[j].e);
        }
      }

      new_val += cal(e-node_vec[i].s, n);       

    }

    cout << "Case #" << cas << ": " << old_val - new_val << '\n';

  }

	return 0;
}

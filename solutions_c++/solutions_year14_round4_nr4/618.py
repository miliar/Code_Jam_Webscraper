#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <deque>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
using namespace std;

set<string> trie[20];
int T, n, m, max_node, count_node;
int loc[20], card[20];
string s[20];

void solve() {
  for (int i = 0; i < n; i++) if (!card[i]) return;
  for (int i = 0; i < n; i++) trie[i].clear();
  for (int i = 0; i < m; i++) {
    int p = loc[i];
    string prep = "";
    for (int j = 0; j < s[i].size(); j++) {
      prep += s[i][j];
      trie[p].insert(prep);
    }
  }
  int tot = 0;
  for (int i = 0; i < n; i++) tot += (int) trie[i].size() + 1;
  // for (int i = 0; i < m; i++) cout << loc[i] << ' ';
  // cout << tot << endl;
  if (tot > max_node) max_node = tot, count_node = 0;
  if (tot == max_node) count_node++;
  if (tot == 10) {
    // cout << "good" << endl;
    // for (int i = 0; i < m; i++) cout << loc[i] << ' ';
    //cout << endl;
  }
}

void run(int id) {
  if (id == m) {
  	solve();
	return;
  }
  for (int i = 0; i < n; i++) {
    loc[id] = i;
    card[i]++;
    run(id + 1);
    card[i]--;
  }
}

int main() {
  scanf("%d", &T);
  for (int it = 1; it <= T; it++) {
    scanf("%d %d", &m, &n);
    for (int i = 0; i < m; i++) cin >> s[i];
    max_node = 0;
    count_node = 0;
    run(0);
    printf("Case #%d: %d %d\n", it, max_node, count_node);
  }
}

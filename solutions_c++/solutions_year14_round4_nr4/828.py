#include <cstdio>
#include <iostream>
#include <ctime>
#include <cassert>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <bitset>

using namespace std;

typedef long long int int64;
typedef long double ext;

const int maxm = 20;
const int maxn = 20;
const int maxl = 40;

int tests;
int m, n;

char s[maxm][maxl];
int ord[maxm];

bool was[maxm];
vector<int> ids[maxn];

int maxc, max_cnt;

const int MOD = 1000000007;

const int alpha = 26;

struct vertex {
  int go[alpha];
};

vector<vertex> trie;


int add_v() {  
  vertex v;
  for (int i = 0; i < alpha; i++)
    v.go[i] = -1;
  trie.push_back(v);
  return trie.size() - 1;
}

void add(char  *s) {
  //cerr << "ADD\n";
  int u = 0;
  for (int i = 0; s[i]; i++) {    
    int c = s[i] - 'A';
    //cerr << "(" << u << ", " << c << ") ";
    if (trie[u].go[c] == -1) {      
      add_v();
      trie[u].go[c] = trie.size() - 1;
    }        
    u = trie[u].go[c];
  }
  //cerr << "\n";
}

int build_trie(vector<int> v) {
  //+cerr << "BUILD\n";
  trie.clear();
  add_v();  
  for (int i = 0; i < int(v.size()); i++)  {
    add(s[v[i]]);
  }
  return int(trie.size());
}


void check() {
    int x = 0;
    for (int i = 0; i < n; i++) {
      if (ids[i].size() == 0)
        return;
    }
    for (int i = 0; i < n; i++) {
      x += build_trie(ids[i]);
    }
    if (x > maxc) {
      maxc = x;
      max_cnt = 1;
    }
    else if (x == maxc) {
      max_cnt = (max_cnt + 1) % MOD;
    }
}

void brute(int k, int lst) {
  //cerr << "BRUTE(" << k << " " << lst << ")\n";
  if (k == n) {    
    for (int i = 0; i < m; i++)
      if (!was[i])
        return;
    //cerr << "CHECK\n";
    check();
    return;
  }
  if (ids[k].size() > 0)
    brute(k + 1, -1);
  for (int i = lst + 1; i < m; i++) {
    if (was[i])
      continue;
    ids[k].push_back(i);
    was[i] = true;
    brute(k, i);
    was[i] = false;
    ids[k].pop_back();
  }
}

int main() {
  assert(freopen("input.txt", "rt", stdin));
  assert(freopen("output.txt", "wt", stdout));
  scanf("%d\n", &tests);
  for (int test = 0; test < tests; test++) {
    printf("Case #%d: ", test + 1);
    scanf("%d %d\n", &m, &n);
    for (int i = 0; i < m; i++) {
      scanf("%s\n", s[i]);
      ord[i] = i;
    }
    maxc = -1;
    max_cnt = 0;
    for (int i = 0; i < n; i++)
      ids[i].clear();
    for (int i = 0; i < m; i++)
      was[i] = false;
    brute(0, -1);
    printf("%d %d\n", maxc, max_cnt);
    fflush(stdout);
  }
  return 0;
}
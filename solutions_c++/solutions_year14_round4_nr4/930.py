#include <iostream>
#include <cstdio>
using namespace std;

int ass[11];
int n, m;
char s[11][14];

int best;
int cnt;
int cur;

struct node {
  char c;
  node * next[111];
};

node * newnode() {
  node * ret = new node;
  for (int i = 0; i < 111; ++i) ret->next[i] = NULL;
  return ret;
}

void insert(char * s, node * n) {
  if (!(*s)) return;
  //printf("inserting %s\n", s);
  if (n->next[(int)*s] == NULL) {
    n->next[(int)*s] = newnode();
    ++cur;
  }
  return insert(s+1, n->next[(int)*s]);
}

void cleanup(node * n) {
  for (int i = 0; i < 111; ++i) {
    if (n->next[i] != NULL) {
      cleanup(n->next[i]);
    }
  }
  delete n;
}

void checkit() {
  cur = 0;
  for (int i = 0; i < n; ++i) {
    node * root = NULL;
    for (int j = 0; j < m; ++j) {
      if (ass[j] == i) {
        if (root == NULL) {
          root = newnode();
          ++cur;
        }
        insert(s[j], root);
      }
    }
    if (root != NULL) cleanup(root);
  }
  if (cur > best) {
    best = cur;
    cnt = 1;
  } else if (cur == best) {
    ++cnt;
  }
}

void tryit(int pos) {
  if (pos == m) {
    checkit();
    return;
  }
  for (int i = 0; i < n; ++i) {
    ass[pos] = i;
    tryit(pos+1);
  }
}

int main() {
  int t;
  cin >> t;
  for (int tt = 1; tt <= t; ++tt) {
    cin >> m >> n;
    for (int i = 0; i < m; ++i) scanf("%s", s[i]);
    best = 0; cur = 0;
    tryit(0);
    cout << "Case #" << tt << ": " << best << " " << cnt << endl;
  }
}

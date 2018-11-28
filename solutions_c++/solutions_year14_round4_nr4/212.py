#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>
using namespace std;

const int CH = 100;
const int MAXM = 1000;
const int MAXN = 100;

string s[MAXM];
int m, n;
int id[MAXM], cnt[MAXN];

struct Trie {
  int next[MAXM * CH + 100][26], L;
  int root;

  int newNode() {
    for (int i = 0; i < 26; i++) {
      next[L][i] = -1;
    }
    return L++;
  }

  void init() {
    L = 0;
    root = newNode();
  }

  void insert(string s) {
    int now = root;
    for (int i = 0; i < (int)s.size(); i++) {
      if (next[now][s[i] - 'A'] == -1) {
        next[now][s[i] - 'A'] = newNode();
      }
      now = next[now][s[i] - 'A'];
    }
  }
};

Trie xiaodao[MAXN];
int ansTot, ans;

void DFS(int now) {
  if (now == m) {
    for (int i = 0; i < n; i++) {
      if (cnt[i] == 0) {
        return;
      }
    }
    for (int i = 0 ; i < n; i++) {
      xiaodao[i].init();
    }
    for (int i = 0; i < m; i++) {
      xiaodao[id[i]].insert(s[i]);
    }
    int tot = 0;
    for (int i = 0; i < n; i++) {
      tot += xiaodao[i].L;
    }
    if (tot > ansTot) {
      ansTot = tot;
      ans = 1;
    } else if (tot == ansTot) {
      ans++;
    }
    return;
  }
  for (int i = 0; i < n; i++) {
    id[now] = i;
    cnt[i]++;
    DFS(now + 1);
    cnt[i]--;
  }
}

int main() {
  int totCas;
  cin >> totCas;
  for (int cas = 1; cas <= totCas; cas++) {
    cin >> m >> n;
    for (int i = 0; i < m; i++) {
      cin >> s[i];
    }
    memset(cnt, 0, sizeof(cnt));
    ansTot = 0;
    ans = 0;
    DFS(0);
    printf("Case #%d: %d %d\n", cas, ansTot, ans);
  }
	return 0;
}


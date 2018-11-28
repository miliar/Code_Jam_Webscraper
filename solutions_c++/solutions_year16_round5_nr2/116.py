#include <bits/stdc++.h>
using namespace std;

int t;
int n, m;
string s[5];
char c[1005];
char ch[1005];

vector <int> childs[105];
int parent[105];
int MAX_TRY = 5000;
string ss;
set<int> possible;
int cnt[105];

string generateRandom(int r) {
  vector<string> cstr;
  for (int x : childs[r]) {
    cstr.push_back(generateRandom(x));
  }
  vector<bool> finished;
  vector <int> indexes;
  for (int i = 0; i < childs[r].size(); i++) {
    finished.push_back(false);
    indexes.push_back(0);
  }
  int numFinished = 0;
  int nn = childs[r].size();
  string result;
  if (r != 0) {
    result.append(1, ch[r]);
  }
  while (numFinished < nn) {
    int total = 0;
    for (int i = 0; i < nn; i++) {
      total += cstr[i].size() - indexes[i];
    }
    int x = rand() % total;
    int y = 0;
    while (x >= cstr[y].size() - indexes[y]) {
      x -= cstr[y].size() - indexes[y];
      ++y;
    }
    result.append(1, cstr[y][indexes[y]]);
    indexes[y]++;
    if (indexes[y] == cstr[y].size()) {
      finished[y] = true;
      ++numFinished;
    }
  }
  return result;
}
int main() {
  srand(time(NULL));
  scanf("%d", &t);
  for (int cs = 1; cs <= t; cs++) {
    scanf("%d", &n);
    for (int i = 0; i <= n; i++) {
      childs[i].clear();
    }
    for (int i = 1; i <= n; i++) {
      scanf("%d", &parent[i]);
      childs[parent[i]].push_back(i);
    }
    scanf("%s", ch);
    for (int i = n; i >= 1; i--) {
      ch[i] = ch[i-1];
    }
    scanf("%d", &m);
    for (int i = 0; i < m; i++) {
      scanf("%s", c);
      s[i] = c;
    }
    for (int i = 0; i < m; i++) {
      cnt[i] = 0;
    }
    for (int i = 0; i < MAX_TRY; i++) {
      ss = generateRandom(0);
      for (int j = 0; j < m; j++) {
        if (ss.find(s[j]) != string::npos) {
          ++cnt[j];
        }
      }
    }
    printf("Case %d:", cs);
    for (int i = 0; i < m; i++) {
      printf(" %.3lf", (double)cnt[i] / MAX_TRY);
    }
    printf("\n");

  }
}

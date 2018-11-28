#include <algorithm>
#include <cassert>
#include <cstring>
#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

#define LOG(x) cerr << #x << " = " << (x) << "\n"

typedef long long llint;
typedef pair<int,int> pii;
const int MAXN = 110;

int n;
char buff[100100];
char word[1100];
vector<string> a[MAXN];
unordered_map<string,int> mp[2];
int ans = 1e9;

void rek(int x, int cnt) {
  if (x == n) {
    ans = min(cnt, ans);
    return;
  }
  for (int j = 0; j < 2; ++j) {
    if (x == 0 && j == 1) continue;
    if (x == 1 && j == 0) continue;
    for (string &s : a[x]) {
      ++mp[j][s];
      if (mp[j][s] == 1 && mp[j^1][s]) {
        ++cnt;
      }
    }
    rek(x + 1, cnt);
    for (string &s : a[x]) {
      --mp[j][s];
      if (mp[j][s] == 0 && mp[j^1][s]) {
        --cnt;
      }
    }
  }
}

void solve() {
  ans = 1e9;
  for (int i = 0; i < n; ++i) {
    a[i].clear();
  }
  mp[0].clear();
  mp[1].clear();

  scanf("%d\n", &n);
  for (int i = 0; i < n; ++i) {
    scanf("%[^\n]\n", buff);
    int cnt = 0;
    int t;
    while (sscanf(buff + cnt, "%s%n", word, &t) == 1) {
      a[i].push_back(string(word));
      cnt += t;
    }
  }

  int diff = 0;/*
  for (string &s : a[0]) {
    ++mp[0][s];
  }
  for (string &s : a[1]) {
    ++mp[1][s];
    diff += mp[0][s] > 0;
  }*/

  rek(0, diff);
  printf("%d\n", ans);
}

int main() {
  int t; scanf("%d", &t);
  for (int i = 0; i < t; ++i) {
    printf("Case #%d: ", i+1);
    solve();
  }
  return 0;
}


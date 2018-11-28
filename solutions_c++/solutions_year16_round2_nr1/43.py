#include <bits/stdc++.h>
using namespace std;

int cnt[256], ret[10];
string d[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

void remove(int x) {
  for (auto &c: d[x]) cnt[c] -= ret[x];
}

void run(int cas) {
  printf("Case #%d: ", cas);
  string s; cin >> s;
  memset(cnt, 0, sizeof(cnt));
  memset(ret, 0, sizeof(ret));
  for (auto &c: s) cnt[c]++;
  ret[0] = cnt['Z']; remove(0);
  ret[6] = cnt['X']; remove(6);
  ret[8] = cnt['G']; remove(8);
  ret[2] = cnt['W']; remove(2);
  ret[4] = cnt['U']; remove(4);
  ret[5] = cnt['F']; remove(5);
  ret[7] = cnt['V']; remove(7);
  ret[3] = cnt['R']; remove(3);
  ret[1] = cnt['O']; remove(1);
  ret[9] = cnt['I']; remove(9);
  for (int i = 0; i < 10; ++i) {
    for (int _ = 0; _ < ret[i]; ++_) putchar('0' + i);
  }
  puts("");
}

int main() {
  int T; scanf("%d", &T);
  for (int cas = 1; cas <= T; ++cas) run(cas);
  return 0;
}

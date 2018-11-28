#include <bits/stdc++.h>
using namespace std;

char buf[5000];

void remove(unordered_map<char,int> &X, int k, const char *str) {
  int n = strlen(str);
  for (int i = 0; i < n; ++i) {
    X[str[i]]-=k;
  }
}

void solve() {
  unordered_map<char,int> X;
  vector<int> ans(10);
  int n = strlen(buf);
  for (int i = 0; i < n; ++i) {
    X[buf[i]]++;
  }
  int k = X['Z'];
  remove(X,k,"ZERO");
  ans[0] = k;

  k = X['X'];
  remove(X,k,"SIX");
  ans[6] = k;

  k = X['S'];
  remove(X,k,"SEVEN");
  ans[7] = k;

  k = X['V'];
  remove(X,k,"FIVE");
  ans[5]=k;

  k = X['W'];
  remove(X,k,"TWO");
  ans[2] = k;

  k = X['U'];
  remove(X,k,"FOUR");
  ans[4] = k;

  k = X['O'];
  remove(X,k,"ONE");
  ans[1] = k;

  k = X['G'];
  remove(X,k,"EIGHT");
  ans[8] = k;

  k = X['I'];
  remove(X,k,"NINE");
  ans[9] = k;

  k = X['H'];
  remove(X,k,"THREE");
  ans[3] = k;

  for (int i = 0; i < 10; ++i) {
    for (int j = 0; j < ans[i]; ++j) {
      printf("%d",i);
    }
  }
  printf("\n");
}

int main() {
  int T;
  scanf("%d",&T);
  for (int i = 0; i < T; ++i) {
    scanf("%s", buf);
    printf("Case #%d: ", i+1);
    solve();
  }
  return 0;
}

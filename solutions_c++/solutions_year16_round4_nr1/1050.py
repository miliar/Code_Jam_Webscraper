#include <bits/stdc++.h>
using namespace std;

#define debug(args...) fprintf(stderr, args)

typedef long long ll;
typedef pair<int,int> pii;
const int oo = 0x3f3f3f3f;

string memo[13][4];
bool mark[13][4];

int f(char c) {
  if (c == 'R') return 0;
  if (c == 'S') return 1;
  else return 2;
}

string go(int lvl, char c) {
  if (lvl == 0) {
    return string(1, c);
  }
  
  if (mark[lvl][f(c)]) return memo[lvl][f(c)];
  mark[lvl][f(c)] = 1;
  
  if (c == 'R') {
    return memo[lvl][f(c)] = min(
        go(lvl - 1, 'R') + go(lvl - 1, 'S'),
        go(lvl - 1, 'S') + go(lvl - 1, 'R'));
  }
  
  if (c == 'P') {
    return memo[lvl][f(c)] = min(
        go(lvl - 1, 'P') + go(lvl - 1, 'R'),
        go(lvl - 1, 'R') + go(lvl - 1, 'P'));
  }
  
  if (c == 'S') {
    return memo[lvl][f(c)] = min(
        go(lvl - 1, 'P') + go(lvl - 1, 'S'),
        go(lvl - 1, 'S') + go(lvl - 1, 'P'));
  }
}

int main() {
  memset(mark, 0, sizeof mark);

  int TC; scanf("%d", &TC);
  
  for (int caso = 1; caso <= TC; ++caso) {
    int N, R, P, S; scanf("%d %d %d %d", &N, &R, &P, &S);
    int C = 1 << N;
    
    vector<string> possib = {
        go(N, 'P'),
        go(N, 'S'),
        go(N, 'R')};
        
    string ans = "IMPOSSIBLE";
 
    for (string x : possib) {
      int r = 0, p = 0, s = 0;
      for (char c : x) {
        if (c == 'R') ++r;
        else if (c == 'P') ++p;
        else ++s;
      }
      
      if (r == R && p == P && s == S) {
        if (ans == "IMPOSSIBLE") ans = x;
        else ans = min(ans, x);
      }
    }   
 
    printf("Case #%d: %s\n", caso, ans.c_str());
  }

  return 0;
}

#include <bits/stdc++.h>
using namespace std;


string res;

char beats(char c) {
  if (c == 'R') return 'S';
  else if (c == 'S') return 'P';
  else return 'R';
}

string construct(int lev, char winner) {
  if (lev == 0) {
    string s = "";
    s.append(1, winner);
    return s;
  } else {
    string tmp = construct(lev - 1, winner);
    string tmp2 = construct(lev - 1, beats(winner));
    if (tmp < tmp2) {
      return tmp + tmp2;
    } else {
      return tmp2 + tmp;
    }
  }
}
int n, r, p, s;
int r1, p1, s1;

void count() {
  r1 = 0; p1 =0; s1 = 0;
  for (char c : res) {
    if (c == 'R') r1++;
    else if (c == 'P') p1++;
    else s1++;
  }
}
int t;
int main() {
  int cs = 0;
  scanf("%d", &t);
  while (t--) {
    ++cs;
    string result = "";
    printf("Case #%d: ", cs);
    scanf("%d %d %d %d", &n, &r, &p, &s);
    res = "";
    res = construct(n, 'R');
    count();
    if (r1 == r && p1 == p && s1 == s) {
      if (result == "" || res < result) {
        result = res;
      }
      printf("%s\n", res.c_str());
      continue;
    }
    res = construct(n, 'P');
    count();
    if (r1 == r && p1 == p && s1 == s) {
      if (result == "" || res < result) {
        result = res;
      }
      printf("%s\n", res.c_str());
      continue;
    }
    res = construct(n, 'S');
    count();
    if (r1 == r && p1 == p && s1 == s) {
      if (result == "" || res < result) {
        result = res;
      }
      printf("%s\n", res.c_str());
      continue;
    }
    printf("IMPOSSIBLE\n");
  }
}

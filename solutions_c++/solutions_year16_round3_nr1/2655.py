#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <iostream>
using namespace std;
typedef long long ll;

struct P {
  int num, index;
};
bool operator < (P a, P b) {
  if (a.num == b.num) {
    return a.index > b.index;
  }
  return a.num < b.num;
}

int main() {
  int t, n;
  FILE *fin, *fout;
  fin = fopen("/Users/zuotian/A-large.in", "r");
  fout = fopen("/Users/zuotian/A-large.out", "w");
  fscanf(fin, "%d", &t);
  for (int r = 1; r <= t; ++r) {
    fscanf(fin, "%d", &n);
    priority_queue<P> s;
    for (int i = 0; i < n; ++i) {
      P x;
      fscanf(fin,"%d", &x.num);
      x.index = i;
      s.push(x);
    }
    fprintf(fout, "Case #%d:", r);
    if (n == 2) {
      int l = s.top().num;
      while (l--) {
        fprintf(fout, " AB");
      }
      fprintf(fout, "\n");
      continue;
    }
    while (s.top().num != 1) {
      P temp = s.top();
      s.pop();
      fprintf(fout, " %c", temp.index + 'A');
      temp.num--;
      s.push(temp);
    }
    if (n & 0x1) {
      P temp = s.top();
      s.pop();
      fprintf(fout, " %c", temp.index + 'A');
      int l = n / 2;
      while (l--) {
        P temp = s.top();
        s.pop();
        fprintf(fout, " %c", temp.index + 'A');
        temp = s.top();
        s.pop();
        fprintf(fout, "%c", temp.index + 'A');
      }
    } else {
      int l = n / 2;
      while (l--) {
        P temp = s.top();
        s.pop();
        fprintf(fout, " %c", temp.index + 'A');
        temp = s.top();
        s.pop();
        fprintf(fout, "%c", temp.index + 'A');
      }
    }
    fprintf(fout, "\n");
  }
  fclose(fin);
  fclose(fout);

  
  return 0;
}

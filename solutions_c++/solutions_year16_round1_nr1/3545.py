#define _CRT_SECURE_NO_DEPRECATE
#include <algorithm>
#include <bitset>
#include <cstdio>
#include <cassert>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <functional>
#include <unordered_map>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <list>
#include <deque>
#include <queue>
#include <math.h>
#include <map>
#include <numeric>
#include <set>
#include <stack>
#include <stdio.h>
#include <string>
#include <sstream>
#include <utility>
#include <vector>

using namespace std;
bool test = false;
const double pi = acos(-1.0);
const double eps = 1e-11;
int breakpoint = 0;

const char rootdir[] = "C:\\CodeJam\\TheLastWord";
void reopen(char* a) {
  char input[256], output[256];
  sprintf(input, "%s\\%s", rootdir, a);
  sprintf(output, "%s\\%s", rootdir, a);
  char *p = strstr(output, ".in");
  if (p) sprintf(p, ".out");
  else sprintf(&p[strlen(output)], ".out");
  freopen(input, "r", stdin);
  if (!test) freopen(output, "w", stdout);
}

char S[1024];

void solve(int t) {
  assert(strlen(S) <= 1000);
  char output[2048];
  char buf[2048];
  memset(output, 0, 2048);
  memset(buf, 0, 2048);
  int b = 1024;
  int e = 1024;
  output[b] = S[0];
  buf[b] = S[0];
  for (int i = 1; i < strlen(S); i++) {
    char c = S[i];
    output[b-1] = c;
    buf[e + 1] = c;
    if (strcmp(&output[b - 1], &buf[b]) > 0) {
      b--;
      buf[b] = c;
    } else {
      e++;
      output[e] = c;
    }
  }
  printf("Case #%d: %s\n", t, &output[b]);
}

int main() {
  // test = true;
  // reopen("sample.in");
  // reopen("A-small-attempt0.in");
  reopen("A-large.in");

  int tt;
  scanf("%d", &tt);
  for (int qq = 1; qq <= tt; qq++) {
    scanf("%s", S);
    solve(qq);
  }
  return 0;
}

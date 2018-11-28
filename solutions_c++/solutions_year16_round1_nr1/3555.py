/**
 * Jerry Ma
 * A.cpp
 */

#include <assert.h>
#include <ctype.h>
#include <limits.h>
#include <math.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#include <algorithm>
#include <array>
#include <bitset>
#include <chrono>
#include <complex>
#include <deque>
#include <forward_list>
#include <fstream>
#include <iostream>
#include <iterator>
#include <limits>
#include <list>
#include <map>
#include <memory>
#include <numeric>
#include <queue>
#include <random>
#include <regex>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

using namespace std;

typedef long long int lli;
typedef pair<int, int> pii;
typedef pair<int, lli> pil;
typedef pair<lli, int> pli;
typedef pair<lli, lli> pll;

int gInt () {
  int i;
  scanf("%d", &i);
  return i;
}

lli gLong () {
  lli i;
  scanf("%lld", &i);
  return i;
}

double gDouble () {
  double i;
  scanf("%lf", &i);
  return i;
}

void quit () {
  fflush(stdout);
  exit(0);
}

char buf[1005];
int n;

void rec (int a, int b) {
  if (a >= b) {
    return;
  }
  char maxLetter = buf[a];
  int firstOccurrence = a;
  for (int i = a + 1; i < b; ++i) {
    if (buf[i] > maxLetter) {
      maxLetter = buf[i];
      firstOccurrence = i;
    }
  }
  vector<char> st;
  for (int i = firstOccurrence; i < b; ++i) {
    if (buf[i] == maxLetter) {
      printf("%c", buf[i]);
    } else {
      st.push_back(buf[i]);
    }
  }
  rec(a, firstOccurrence);
  for (auto it = st.begin(); it != st.end(); ++it) {
    printf("%c", *it);
  }
}

void solve (int nC) {
  scanf("%s", buf);
  n = strlen(buf);
  printf("Case #%d: ", nC);
  rec(0, n);
  printf("\n");
}

int main (int argc, char ** argv) {
  int nC = gInt();
  for (int i = 0; i < nC; ++i) {
    solve(i + 1);
  }
  quit();
}

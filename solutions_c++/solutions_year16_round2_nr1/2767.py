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

const char rootdir[] = "C:\\CodeJam\\GettingTheDigits";
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

char S[2048];

// "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
// A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
void init() {
  char words[10][8] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", 
                        "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };

  // number of words contain the letter
  int wc[30];

  // words contain the letter
  vector<string> wds[30];

  for (int i = 0; i < 30; i++) wc[i] = 0;
  for (int i = 0; i < 10; i++) {
    printf("%s ", words[i]);
    char *p = words[i];
    while (*p != 0) {
      wc[*p - 'A']++;
      wds[*p - 'A'].push_back(words[i]);
      p++;
    }
  }
  printf("\n");
  for (int i = 0; i < 26; i++) {
    printf(" %c", 'A' + i);
  }
  printf("\n");
  for (int i = 0; i < 26; i++) {
    printf("%2d", wc[i]);
  }
  for (int i = 0; i < 26; i++) {
    if (wds[i].size() == 0) continue;
    printf("\n%c: ", 'A' + i);
    for (int j = 0; j < wds[i].size(); j++)
      printf("%s ", wds[i][j].c_str());
  }
  printf("\n");
}

// "ONE", "THREE", "FIVE", "SEVEN", "NINE"
// A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
void init2() {
  char words[10][8] = { "ONE", "THREE", "FIVE", "SEVEN", "NINE" };

  // number of words contain the letter
  int wc[30];

  // words contain the letter
  vector<string> wds[30];

  for (int i = 0; i < 30; i++) wc[i] = 0;
  for (int i = 0; i < 5; i++) {
    printf("%s ", words[i]);
    char *p = words[i];
    while (*p != 0) {
      wc[*p - 'A']++;
      wds[*p - 'A'].push_back(words[i]);
      p++;
    }
  }
  printf("\n");
  for (int i = 0; i < 26; i++) {
    printf(" %c", 'A' + i);
  }
  printf("\n");
  for (int i = 0; i < 26; i++) {
    printf("%2d", wc[i]);
  }
  for (int i = 0; i < 26; i++) {
    if (wds[i].size() == 0) continue;
    printf("\n%c: ", 'A' + i);
    for (int j = 0; j < wds[i].size(); j++)
      printf("%s ", wds[i][j].c_str());
  }
  printf("\n");
}

void init3() {
  char words[10][8] = { "NINE", "" };

  // number of words contain the letter
  int wc[30];

  // words contain the letter
  vector<string> wds[30];

  for (int i = 0; i < 30; i++) wc[i] = 0;
  for (int i = 0; i < 1; i++) {
    printf("%s ", words[i]);
    char *p = words[i];
    while (*p != 0) {
      wc[*p - 'A']++;
      wds[*p - 'A'].push_back(words[i]);
      p++;
    }
  }
  printf("\n");
  for (int i = 0; i < 26; i++) {
    printf(" %c", 'A' + i);
  }
  printf("\n");
  for (int i = 0; i < 26; i++) {
    printf("%2d", wc[i]);
  }
  for (int i = 0; i < 26; i++) {
    if (wds[i].size() == 0) continue;
    printf("\n%c: ", 'A' + i);
    for (int j = 0; j < wds[i].size(); j++)
      printf("%s ", wds[i][j].c_str());
  }
  printf("\n");
}

int lc[26];
int dc[10];  // count of each digit

void subtract(char c, int d, char word[]) {
  int idx = c - 'A';
  int count = lc[idx];
  if (count == 0) return;
  dc[d] += count;
  char *p = word;
  while (*p != 0) {
    assert(lc[*p - 'A'] >= count);
    lc[*p - 'A'] -= count;
    p++;
  }
}

void solve(int t) {
  for (int i = 0; i < 26; i++) lc[i] = 0;
  for (int i = 0; i < 10; i++) dc[i] = 0;

  char *p = S;
  while (*p != 0) {
    lc[*p - 'A']++;
    p++;
  }
  subtract('G', 8, "EIGHT");
  subtract('U', 4, "FOUR");
  subtract('W', 2, "TWO");
  subtract('X', 6, "SIX");
  subtract('Z', 0, "ZERO");

  subtract('F', 5, "FIVE");
  subtract('H', 3, "THREE");
  subtract('O', 1, "ONE");
  subtract('R', 3, "THREE");
  subtract('S', 7, "SEVEN");
  subtract('T', 3, "THREE");

  subtract('E', 9, "NINE");
  subtract('I', 9, "NINE");
  subtract('N', 9, "NINE");
  for (int i = 0; i < 26; i++) assert(lc[i] == 0);
  printf("Case #%d: ", t);
  for (int i = 0; i < 10; i++) {
    for (int j = 0; j < dc[i]; j++) {
      printf("%d", i);
    }
  }
  printf("\n");
}

int main() {
  // test = true;
  // reopen("sample.in");
  // reopen("A-small-attempt0.in");
  reopen("A-large.in");

  if (test) {
    init();
    init2();
    init3();
  }
  int tt;
  scanf("%d", &tt);
  for (int qq = 1; qq <= tt; qq++) {
    scanf("%s", S);
    if (test) printf("%s\n", S);
    solve(qq);
  }
  return 0;
}

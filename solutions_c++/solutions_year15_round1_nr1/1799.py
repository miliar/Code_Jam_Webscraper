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
#include <hash_map>
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
const double pi=acos(-1.0);
const double eps=1e-11;
int breakpoint = 0;

const char rootdir[] = "C:\\CodeJam\\MushroomMonster";
void reopen(char* a) {
	char input[256], output[256];
	sprintf(input, "%s\\%s", rootdir, a);
	sprintf(output, "%s\\%s", rootdir, a);
	char *p = strstr(output, ".in");
	if (p) sprintf(p, ".out"); 
	else sprintf(&p[strlen(output)], ".out");
	freopen(input,"r",stdin);
	if (!test) freopen(output,"w",stdout);
}

int T;
int N;
int m[10020];

int main() {
  test = false;
  // reopen("sample.in");
  // reopen("A-small-attempt0.in");
  reopen("A-large.in");

  scanf("%d", &T);
  
  for (int TC = 1; TC <= T; TC++) {
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
      scanf("%d", &m[i]);
    }
    int maxrate = 0;
    int c1 = 0;
    int c2 = 0;
    for (int i = 1; i < N; i++) {
      int d = m[i-1] - m[i];
      if (d > 0) {
        maxrate = std::max(maxrate, d);
        c1 += d;
      }
    }
    for (int i = 0; i < N-1; i++) {
      c2 += std::min(maxrate, m[i]);
    }

    printf("Case #%d: %d %d\n", TC, c1, c2);
  }
}
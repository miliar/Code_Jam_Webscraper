#include <stdio.h>
#include <math.h>
#include <stdlib.h>

#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

#define MAX 1000001

int start;
int N;
int freq[MAX+2];

int changes[MAX+2];
int size[MAX+2];
int remaining[MAX+2];

void go(int tc) {
  cin >> start >> N;
  for (int i=0; i<MAX+2; i++) {
    freq[i] = 0;
    changes[i] = 0;
    size[i] = 0;
    remaining[i] = 0;
  }

  for (int i=0; i<N; i++) {
    int n;
    cin >> n;
    freq[n] += 1;
  }
  for (int i=MAX; i>=0; i--) {
    remaining[i] = remaining[i+1] + freq[i];
  }

  int ans = -1;
  size[0] = start;
  changes[0] = 0;
  for (int i=1; i<=MAX; i++) {
    changes[i] = changes[i-1];
    size[i] = size[i-1];
    if (freq[i] == 0) continue;

    int s = size[i];
    if (i < s) {
      size[i] = size[i] + i * freq[i];
      continue;
    }

    // remove
    int chr = changes[i] + remaining[i];

    // or add
    int cha = MAX*2;
    int sa = s;
    if (s > 1) {
      cha = changes[i];
      while (i >= sa) {
        cha += 1;
        sa += (sa-1);
      }
      sa += i * freq[i];
    }

    // better to remove
    if (chr <= cha) {
      ans = chr;
      break;
    }

    // better to add
    changes[i] = cha;
    size[i] = sa;
  }

  if (ans == -1) {
    ans = changes[MAX];
  }

  printf("Case #%d: %d\n", tc, ans);
}

int main() {
  int tc;
  cin >> tc;
  for (int i=0; i<tc; i++) {
    go(i+1);
  }
}

// vim: ts=2 sts=2


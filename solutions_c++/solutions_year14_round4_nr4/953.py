#include <cmath>
#include <ctime>
#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <cctype>
#include <stack>
#include <complex>
using namespace std;

typedef long long int int64;

#define EPS 10e-9
#define INF 0x3f3f3f3f
#define REP(i,n) for(int i=0; i<(n); i++)

int n, m;
char s[10][30];

int num;
int trie[90][30];
int used[10];

int64 add(int r, int ind, int x) {
  if (x == strlen(s[ind])) return 0;
  char c = s[ind][x];
  if (trie[r][c-'A'] == -1) {
    trie[r][c-'A'] = num;
    num++;
    return add(num-1, ind, x+1) + 1;
  }
  return add(trie[r][c-'A'], ind, x+1);
}

int64 count() {
  int64 res = 0;
  REP(i, m) {
    num = 1;
    memset(trie, -1, sizeof(trie));
    REP(j, n) {
      if (used[j] == i) {
        res += add(0, j, 0);
      }
    }
    if (num > 1)
      res++;
  }
  return res;
}

int64 res;
int64 sum;

void calcula(int ind) {
  if (ind == n) {
    int64 x = count();
    if (x > res) {
      res = x;
      sum = 1;
    }
    else if (x == res) {
      sum++;
    }
    return;
  }
  REP(i, m) {
    used[ind] = i;
    calcula(ind+1);
  }
}

int main()
{	
  int t;
  scanf("%d", &t);
  REP(ct, t) {
    scanf("%d %d", &n, &m);
    REP(i, n) {
      scanf("%s", s[i]);
    }
    res = 0;
    calcula(0);
    printf("Case #%d: %lld %lld\n", ct+1, res, sum);
  }
	return 0;
}
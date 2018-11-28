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

int n;
int v[1050];
int aux[1050];
int w[1050];

int merge1(int a, int b) {
  int res = 0;
  for (int i = a; i <= b; i++) {
    for (int j = a; j < b; j++) {
      if (w[j] > w[j+1]) {
        res++;
        swap(w[j], w[j+1]);
      }
    }
  }
  return res;
}

int merge2(int a, int b) {
  int res = 0;
  for (int i = a; i <= b; i++) {
    for (int j = a; j < b; j++) {
      if (w[j] < w[j+1]) {
        res++;
        swap(w[j], w[j+1]);
      }
    }
  }
  return res;
}

bool check() {
  bool foi = false;
  for (int i = 0; i < n-1; i++) {
    if (!foi && w[i] > w[i+1]) {
      foi = true;
      continue;
    }
    if (foi && w[i] < w[i+1]) return false;
  }
  return true;
}

int maior(int a, int b) {
  int x, y;
  REP(i, n) {
    if (v[i] == a) {
      x = i;
    }
    if (v[i] == b) {
      y = i;
    }
  }
  if (x > y) return true;
  return false;
}

int calcula() {
  int res = 0;
  REP(i, n) {
    for (int j = 0; j < n-1; j++) {
      if (maior(w[j], w[j+1])) {
        res++;
        swap(w[j], w[j+1]);
      }
    }
  }
  return res;
}

int main()
{	
  int t;
  scanf("%d", &t);
  REP(ct, t) {
    scanf("%d", &n);
    REP(i, n) {
      scanf("%d", &v[i]);
    }
    REP(i, n) {
      aux[i] = i;
    }
    int res = INF;
    do {
      REP(i, n) {
        w[i] = v[aux[i]];
      }
      if (check()) {
        res = min(res, calcula());
      }
    }while (next_permutation(aux, aux+n));
    printf("Case #%d: %d\n", ct+1, res);
  }
	return 0;
}
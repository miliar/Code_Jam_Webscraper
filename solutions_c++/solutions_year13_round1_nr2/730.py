#pragma comment(linker, "/STACK:16777216")
#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#include <cstdio>
#include <cmath>
#include <cctype>
#include <cassert>
#include <cstring>
#include <cstdlib>
#include <utility>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <ctime>
#include <stack>
#include <algorithm>
#include <numeric>
#include <complex>
#include <functional>
#include <list>
#include <iostream>
using namespace std;

#define C(_a, _v) memset(_a,_v,sizeof(_a))
#define ALL(_obj) (_obj).begin(),(_obj).end()
#define FORB(_i,_a,_b) for((_i)=(_a);(_i)<(_b);++(_i))
#define FORE(_i,_a,_b) for((_i)=(_a);(_i)<=(_b);++(_i))
#define FOR(_i,_n) FORB(_i,0,_n)
#define FORS(_i,_obj) FOR(_i,(_obj).size())
#define ADJ(_i,_v) for((_i)=kick[_v];(_i)>=0;(_i)=foll[_i])
#define X first
#define Y second
#define I64 "%I64d"
#define pb push_back
#define ppb pop_back
#define mp make_pair

typedef long long i64;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef pair<i64, i64> pii64;
typedef vector<pii> vpii;

template<typename T>inline bool remin(T&c,const T&n){if(n<c){c=n;return 1;}return 0;}
template<typename T>inline bool remin2(T&c,const T&n){if(c<0||n<c){c=n;return 1;}return 0;}
template<typename T>inline bool remax(T&c,const T&n){if(c<n){c=n;return 1;}return 0;}
template<typename T>inline void addmod(T&c,const T&n,const T&m){c = (c + n) % m;}

int _in;int in(){scanf("%d",&_in);return _in;}

// stuff cutline

const int N = 1e4 + 5;

int cap, inc, n, maj[N], mark[N];

void go(int from, int to, int sup, int tg) {
  if (to - from > 0) {
    int i = from, mx = maj[from], left, right, guarantee, lo, mi, hi;
    while (++i < to) {
      remax(mx, maj[i]);
    }
    while (maj[--i] != mx);
    left = i - from;
    right = to - i;
    guarantee = (int)min(i64(sup + left * inc), (i64)cap);
    lo = 0;
    hi = cap + 1;
    while (lo + 1 != hi) {
      mi = (lo + hi) / 2;
      ((guarantee - mi >= 0 && i64(guarantee - mi + inc * right) >= (i64)tg) ? lo : hi) = mi;
    }
    mark[i] = lo;
    go(from, i, sup, guarantee);
    go(i + 1, to, min(guarantee - lo + inc, cap), tg);
  }
}

int main() {
#ifndef DEBUG
  freopen("C:\\Users\\anonymous\\Downloads\\B-small-attempt1.in", "r", stdin);
  freopen("out.txt", "w", stdout);
#endif
  i64 sum;
  int tests = in(), t, i;
  FORE (t, 1, tests) {
    scanf("%d%d%d", &cap, &inc, &n);
    FOR (i, n) {
      scanf("%d", maj + i);
    }
    go(0, n, cap, 0);
    sum = 0;
    FOR (i, n) {
      sum += (i64)maj[i] * (i64)mark[i];
    }
    printf("Case #%d: " I64 "\n", t, sum);
  }
  return 0;
}
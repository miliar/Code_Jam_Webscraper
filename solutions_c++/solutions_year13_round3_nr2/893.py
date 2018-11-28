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
#define I64 "%lld"
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

const int N = 3000, MAXJ = 4, GUESS = 100;

char cert[N], compass[5] = "NESW";

int way[N * 2 + 1][N * 2 + 1], dir[4][2] = { { 0, 1 }, { 1, 0 }, { 0, -1 }, { -1, 0 } }, trace[N * 2 + 1][N * 2 + 1];

int main() {
  queue<int> qu;
  int i, j, d, di, dj, jump;
  C(way, -1);
  way[N][N] = 0;
  qu.push(0);
  qu.push(0);
  while (!qu.empty()) {
    i = qu.front(); qu.pop();
    j = qu.front(); qu.pop();
    jump = way[i + N][j + N] + 1;
    FOR (d, 4) {
      di = i + dir[d][0] * jump;
      dj = j + dir[d][1] * jump;
      if (di >= -N && di <= N && dj >= -N && dj <= N && remin2(way[di + N][dj + N], jump)) {
        qu.push(di);
        qu.push(dj);
        trace[di + N][dj + N] = d;
      }
    }
  }
#ifndef _DEBUG
  freopen("C:\\Users\\anonymous\\Downloads\\B-small-attempt3.in", "r", stdin);
  freopen("out.txt", "w", stdout);
#endif
  stack<char> sol;
  int tests = in(), t, x, y, m, guess, cx, cy, answer, k, step;
  FORE (t, 1, tests) {
    scanf("%d%d", &x, &y);
    /*
    answer = -1;
    FORB (guess, 1, GUESS) {
      FOR (m, 1 << (MAXJ * 2)) {
        cx = x;
        cy = y;
        i = m;
        j = guess;
        do {
          if (cx >= -N && cx <= N && cy >= -N && cy <= N && way[cx + N][cy + N] >= 0) {
            if (way[cx + N][cy + N] == j) {
              answer = guess;
            }
            break;
          }
          cx += dir[i % 4][0];
          cy += dir[i % 4][1];
          i /= 4;
          --j;
        } while (++i < MAXJ && j > 0);
      }
    }
    if (answer < 0) {
      puts("FAIL");
      break;
    }
    */
    sol.push('\n');
    do {
      step = way[x + N][y + N];
      k = trace[x + N][y + N];
      sol.push(compass[k]);
      x -= dir[k][0] * step;
      y -= dir[k][1] * step;
    } while (x != 0 || y != 0);
    printf("Case #%d: ", t);
    while (!sol.empty()) {
      putchar(sol.top());
      sol.pop();
    }
  }
  return 0;
}

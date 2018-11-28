#include <iostream>
#include <complex>
#include <sstream>
#include <string>
#include <algorithm>
#include <deque>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <vector>
#include <set>
#include <limits>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <ctime>
using namespace std;
#define REP(i, j) for(int i = 0; i < (int)(j); ++i)
#define FOR(i, j, k) for(int i = (int)(j); i < (int)(k); ++i)
#define P pair<int, int>
#define SORT(v) sort((v).begin(), (v).end())
#define REVERSE(v) reverse((v).begin(), (v).end())
const int MAX_HW = 6;

int T, R, C, M, v[MAX_HW][MAX_HW];
int my[] = {1, -1, 0, 0, 1, 1, -1, -1};
int mx[] = {0, 0, 1, -1, 1, -1, 1, -1};

int cnt_bit(int bit){
  int ret = 0;
  while(bit > 0){
    if(bit & 1) ++ret;
    bit >>= 1;
  }
  return ret;
}

void make_v(int bit){
  REP(i, R){
    REP(j, C){
      if(bit & 1) v[i][j] = -1;
      else v[i][j] = 0;
      bit >>= 1;
    }
  }
  REP(i, R){
    REP(j, C){
      if(v[i][j] == -1) continue;
      int cnt = 0;
      REP(k, 8){
        int ny = i + my[k], nx = j + mx[k];
        if(ny >= 0 && nx >= 0 && ny < R && nx < C && v[ny][nx] == -1) ++cnt;
      }
      v[i][j] = cnt;
    }
  }
}

void dfs(int y, int x, bool checked[MAX_HW][MAX_HW]){
  checked[y][x] = true;
  if(v[y][x] != 0) return ;
  REP(i, 8){
    int ny = y + my[i], nx = x + mx[i];
    if(ny >= 0 && nx >= 0 && ny < R && nx < C && v[ny][nx] != -1 && !checked[ny][nx]) dfs(ny, nx, checked);
  }
}

bool is_end_v(bool checked[MAX_HW][MAX_HW]){
  REP(i, R)
    REP(j, C)
    if(v[i][j] != -1 && !checked[i][j]) return false;
  return true;
}

P check(){
  REP(y, R){
    REP(x, C){
      if(v[y][x] == -1) continue;
      bool checked[MAX_HW][MAX_HW];
      memset(checked, 0, sizeof(checked));
      dfs(y, x, checked);
      if(is_end_v(checked)) return P(y, x);
    }
  }
  return P(-1, -1);
}

void disp(int y, int x){
  REP(i, R){
    REP(j, C){
      if(i == y && j == x) printf("c");
      else if(v[i][j] == -1) printf("*");
      else printf(".");
    }
    printf("\n");
  }
}

int main() {
  scanf("%d", &T);
  REP(t, T){
    printf("Case #%d:\n", t + 1);
    scanf("%d %d %d", &R, &C, &M);
    bool find_ans = false;
    REP(i, (1 << (R * C))){
      if(cnt_bit(i) != M) continue;
      make_v(i);
      P check_r = check();
      if(check_r.first != -1){
        find_ans = true;
        disp(check_r.first, check_r.second);
        break;
      }
    }
    if(!find_ans) printf("Impossible\n");
  }
  return 0;
}

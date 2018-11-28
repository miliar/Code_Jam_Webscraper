#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;
#define DEBUG(x) cerr << '>' << #x << ':' << (x) << endl;
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define REP(i,a) for(int i=0; i<(a);++i)
inline bool EQ(double a, double b) {return fabs(a-b) < 1e-9;}

typedef long long ll;

int T, X, R, C;

vector<vector<bool>> grid = vector<vector<bool>>(4, vector<bool>(4, false));
int full = 0;

void print_shape(const vector<vector<bool>>& s) {
  REP(y,4) {
    REP(x,4) printf("%c", s[y][x] ? '#' : '.');
    printf("\n");
  }
  printf("\n");
}

vector<vector<bool>> rotate(const vector<vector<bool>>& in) {
  vector<vector<bool>> out;
  REP(y,4) {
    out.emplace_back();
    REP(x,4) {
      out.back().push_back(in[x][3-y]);
    }
  }
  return out;
}

vector<vector<bool>> reflect(const vector<vector<bool>>& in) {
  vector<vector<bool>> out;
  REP(y,4) {
    out.emplace_back();
    REP(x,4) {
      out.back().push_back(in[y][3-x]);
    }
  }
  return out;
}

void addRotations(vector<vector<vector<bool>>>& v) {
  int l = v.size();
  REP(i,l) {
    vector<vector<bool>> shape = v[i];
    shape = rotate(shape);
    v.push_back(shape);
    shape = rotate(shape);
    v.push_back(shape);
    shape = rotate(shape);
    v.push_back(shape);
  }
}

void addReflections(vector<vector<vector<bool>>>& v) {
  int l = v.size();
  REP(i,l) {
    vector<vector<bool>> shape = v[i];
    shape = reflect(shape);
    v.push_back(shape);
  }
}

vector<vector<vector<bool>>> getViews(const vector<vector<bool>>& s) {
  vector<vector<vector<bool>>> r(1, s);
  addRotations(r);
  addReflections(r);
  return r;
}

bool place(const vector<vector<bool>>& shape, int x0, int y0) {
  vector<pair<int, int>> placed;
  bool ok = true;
  REP(dy,4) REP(dx,4) {
    if (shape[dy][dx]) {
      int x = x0 + dx;
      int y = y0 + dy;
      if (x < 0 || y < 0 || x >= C || y >= R || grid[y][x]) {
        ok = false;
        break;
      }
      grid[y][x] = true;
      ++full;
      placed.push_back({x, y});
    }
  }
  if (!ok) {
    for (const auto& p : placed) {
      grid[p.second][p.first] = false;
      --full;
    }
  }
  return ok;
}

void unplace(const vector<vector<bool>>& shape, int x0, int y0) {
  REP(dy,4) REP(dx,4) {
    if (shape[dy][dx]) {
      int x = x0 + dx;
      int y = y0 + dy;
      grid[y][x] = false;
      --full;
    }
  }
}

vector<vector<vector<vector<bool>>>> shapes = {
  {},
  {
    {
      {1,0,0,0},
      {0,0,0,0},
      {0,0,0,0},
      {0,0,0,0}
    }
  },
  {
    {
      {1,1,0,0},
      {0,0,0,0},
      {0,0,0,0},
      {0,0,0,0}
    }
  },
  {
    {
      {1,1,1,0},
      {0,0,0,0},
      {0,0,0,0},
      {0,0,0,0}
    },
    {
      {1,1,0,0},
      {0,1,0,0},
      {0,0,0,0},
      {0,0,0,0}
    }
  },
  {
    {
      {1,1,0,0},
      {1,1,0,0},
      {0,0,0,0},
      {0,0,0,0}
    },
    {
      {1,1,0,0},
      {1,0,0,0},
      {1,0,0,0},
      {0,0,0,0}
    },
    {
      {1,0,0,0},
      {1,1,0,0},
      {1,0,0,0},
      {0,0,0,0}
    },
    {
      {1,0,0,0},
      {1,1,0,0},
      {0,1,0,0},
      {0,0,0,0}
    },
    {
      {1,0,0,0},
      {1,0,0,0},
      {1,0,0,0},
      {1,0,0,0}
    }
  }
};

map<int, bool> cache;

int getKey(const vector<vector<bool>>& shape) {
  int k = 0;
  REP(y,4) REP(x,4) {
    k *= 2;
    if (shape[y][x]) ++k;
  }
  return k;
}

bool canPlace(const vector<vector<bool>>& shape) {
  FOR(y,-3,3) FOR(x,-3,3) {
    if (place(shape, x, y)) {
      int key = getKey(grid);
      auto it = cache.find(key);
      if (it != cache.end()) {
        unplace(shape, x, y);
        if (it->second) return true;
        continue;
      }
      if (full == R * C) {
        unplace(shape, x, y);
        cache[key] = true;
        return true;
      }
      REP(i,(int)shapes[X].size()) {
        vector<vector<vector<bool>>> views = getViews(shapes[X][i]);
        for (const auto& s : views) {
          if (canPlace(s)) {
            unplace(shape, x, y);
            cache[key] = true;
            return true;
          }
        }
      }
      cache[key] = false;
      unplace(shape, x, y);
    }
  }
  return false;
}

int main() {
  scanf("%d", &T);
  
  REP(t,T) {
    scanf("%d%d%d", &X, &R, &C);
    cache.clear();
    bool ans = false;
    REP(i,(int)shapes[X].size()) {
      bool someWorks = false;
      for (const auto& s : getViews(shapes[X][i])) {
        if (canPlace(s)) {
          someWorks = true;
          break;
        }
      }
      if (!someWorks) {
        ans = true;
        break;
      }
    }
    printf("Case #%d: %s\n", t+1, ans ? "RICHARD" : "GABRIEL");
  }
  
  return 0;
}

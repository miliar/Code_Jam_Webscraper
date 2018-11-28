#include <bits/stdc++.h>
#include <cstring>

using namespace std;

enum Arrow {
  NONE, LEFT, RIGHT, TOP, BOTTOM,
};

int R, C;

#define MAXR 128
#define MAXC 128

deque<deque<Arrow> > MAP;
bool VISITED[MAXR][MAXC];

bool muri() {
  set<pair<int, int> > yabai;
  for(int i = 0; i < R; ++i){
    for(int j = 0; j < C; ++j){
      if(MAP[i][j] == NONE){
        continue;
      }
      bool ok = false;
      for(int x = 0; x < R; ++x){
        if(x == i){ continue; }
        if(MAP[x][j] != NONE){
          ok = true;
        }
      }
      for(int y = 0; y < C; ++y){
        if(y == j){ continue; }
        if(MAP[i][y] != NONE){
          ok = true;
        }
      }
      if(!ok){
        return true;
      }
    }
  }
  return false;
}

int res;

void visit(int i, int j){
  if(MAP[i][j] == NONE){
    return;
  }
  Arrow arrow;
  arrow = MAP[i][j];
  while(1){
    if(i < 0 || j < 0 || i >= R || j >= C){
      ++res; // はみでた
      return;
    }
    if(VISITED[i][j]){
      return;
    }
    if(MAP[i][j] != NONE){
      arrow = MAP[i][j];
      VISITED[i][j] = true;
    }
    switch(arrow){
    case NONE:
      break;
    case TOP:
      --i;
      break;
    case BOTTOM:
      ++i;
      break;
    case LEFT:
      --j;
      break;
    case RIGHT:
      ++j;
      break;
    }
  }
}

void solve()
{
  if(muri()){
    cout << "IMPOSSIBLE" << "\n";
    return;
  }
  res = 0;
  for(int i = 0; i < R; ++i){
    for(int j = 0; j < C; ++j){
      visit(i, j);
    }
  }
  cout << res << "\n";
}

int main(){
  size_t T;
  std::cin >> T;
  for(size_t i = 1; i <= T; ++i){
    std::cin >> R >> C;
    MAP.clear();
    memset(VISITED, 0, sizeof(VISITED));
    for(int j = 0; j < R; ++j){
      MAP.emplace_back();
      std::string s;
      cin >> s;
      cerr << s << "debug\n";
      for(int k = 0; k < C; ++k){
        Arrow arrow = NONE;
        switch(s[k]){
        case '.': arrow = NONE; break;
        case '^': arrow = TOP; break;
        case '>': arrow = RIGHT; break;
        case 'v': arrow = BOTTOM; break;
        case '<': arrow = LEFT; break;
        }
        MAP.back().emplace_back(arrow);
      }
    }
    for(int i = 0; i < R; ++i){
      for(int j = 0; j < C; ++j){
        cerr << MAP[i][j] << " ";
      }
      cerr << "\n";
    }
    std::cout << "Case #" << i << ": ";
    solve();
  }
}

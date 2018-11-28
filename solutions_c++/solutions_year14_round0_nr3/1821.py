#include <iostream>
#include <algorithm>

using namespace std;

const int MAX_ROW = 50;
const int MAX_COL = 50;
const int NDIR = 8;
const int DR[] = {-1, -1, -1, 0, 0, 0, 1, 1, 1};
const int DC[] = {-1, 0, 1, -1, 0, 1, -1, 0, 1};

int row, col, m;
int g[MAX_ROW][MAX_COL];
int bak[MAX_ROW][MAX_COL];
bool vis[MAX_ROW][MAX_COL];

void put(int i, int j){
  bak[i][j] = g[i][j];
  g[i][j] = -1;
  for(int di = -1; di <= 1; ++di)
    for(int dj = -1; dj <= 1; ++dj)
      if(0 <= i+di && i+di < row && 0 <= j+dj && j+dj < col){
        //        cout << i+di << "," << j+dj << endl;
        if(g[i+di][j+dj] != -1)
          ++g[i+di][j+dj];
      }
}

void unput(int i, int j){
  for(int di = -1; di <= 1; ++di)
    for(int dj = -1; dj <= 1; ++dj)
      if(0 <= i+di && i+di < row && 0 <= j+dj && j+dj < col)
        if(g[i+di][j+dj] != -1)
          --g[i+di][j+dj];
  g[i][j] = bak[i][j];
}

int dfs(int i, int j){
  int res = 1;
  vis[i][j] = true;
  for(int k = 0; k < NDIR; ++k){
    int ni = i + DR[k], nj = j + DC[k];
    if(!(0 <= ni && ni < row && 0 <= nj && nj < col) || vis[ni][nj]) continue;

    if(g[ni][nj] == 0)
      res += dfs(ni, nj);
    else if(g[ni][nj] != -1){
      vis[ni][nj] = true;
      ++res;
    }
  }
  return res;
}

bool valid(int set){
  for(int i = 0; i < row; ++i)
    fill_n(vis[i], col, false);

  for(int i = 0; i < row; ++i)
    for(int j = 0; j < col; ++j)
      if(g[i][j] == 0){
        int open = dfs(i, j);
        if(open+set == row*col)
          return true;
        break;
      }
  return false;
}

void output_g(void){
  for(int i = 0; i < row; ++i){
    cout << "  ";
    for(int j = 0; j < col; ++j){
      if(g[i][j] == -1)
        cout << "_ ";
      else
        cout << g[i][j] << " ";
    }
    cout << endl;
  }
}

bool solve(int cur, int set){
  if(m == set) return valid(m);
  if(cur == row*col) return false;

  //  cout << "solve: " << cur << " : " << set << endl;

  //  for(int ncur = cur; ncur < row*col; ++ncur){
  int ncur = cur;
    int i = ncur / col, j = ncur % col;

    //    output_g();
    //    cout << "  put: " << i << ", " << j << endl;
    put(i, j);
    ++set;
    //    output_g();

    //  cout << "  " << valid(set) << endl;
    //  cout << "  --" << endl;
    // for(int i = 0; i < row; ++i){
    //   cout << "  ";
    //   for(int j = 0; j < col; ++j){
    //     cout << vis[i][j] << " ";
    //   }
    //   cout << endl;
    // }
    if(solve(ncur+1, set))
      return true;
    unput(i, j);
    --set;
    //    cout << "  unput: " << i << ", " << j << endl;
    //    output_g();
    //  }

    if(i == 0 && j == 0) return false;
  return solve(cur+1, set);
}

int main(void){
  int t;
  cin >> t;
  for(int c = 0; c < t; ++c){
    cin >> row >> col >> m;

    for(int i = 0; i < row; ++i)
      fill_n(g[i], col, 0);

    // output_g();

    cout << "Case #" << c+1 << ":" << endl;
    if(row*col - m == 1){
      bool first = true;
      for(int i = 0; i < row; ++i){
        for(int j = 0; j < col; ++j){
          if(first){
            first = false;
            cout << 'c';
          }
          else
            cout << '*';
        }
        cout << endl;
      }
    }
    else if(solve(0, 0)){
      bool first = true;
      for(int i = 0; i < row; ++i){
        for(int j = 0; j < col; ++j)
          if(g[i][j] == -1){
            cout << '*';
          }
          else if(g[i][j] == 0 && first){
            cout << 'c';
            first = false;
          }
          else
            cout << '.';
        cout << endl;
      }
    }
    else{
      cout << "Impossible" << endl;
    }
  }

  return 0;
}

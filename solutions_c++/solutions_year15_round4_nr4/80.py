// I believe I can search in small.
#include <iostream>
#include <cstring>
#include <cassert>
#include <algorithm>
#include <vector>
#include <set>
using namespace std;
bool valid[6][6]; // it's valid
char number[6][6];
char pattern[6][6]; 
long answer;
int R, C;
int count2(int y,int x,int target) {
  int cnt = 0;
  if(y != 0)
    if(number[y-1][x] == target) cnt++;
  if(y != R - 1)
    if(number[y + 1][x] == target) cnt++;
  if(number[y][(x + C - 1) % C] == target) cnt++;
  if(number[y][(x + C + 1) % C] == target) cnt++;
  return cnt;
}
void update_valid2(int y, int x) {
  if(number[y][x] == 0) return;
  if(count2(y, x, number[y][x]) == number[y][x]) {
    valid[y][x] = true;
  }
}
void update_valid(int y, int x) {
  update_valid2(y,x);
  if(y != 0)update_valid2(y - 1,x);
  if(y != R - 1)update_valid2(y + 1,x);
  update_valid2(y,(x + C - 1) % C);
  update_valid2(y,(x + C + 1) % C);
}

void update_pattern() {
  for(int y = 0; y < R; y++) {
    for(int x = 0; x < C; x++) {
      if(number[y][x] != 0)continue;
      pattern[y][x] = 0;
      for(int t = 1; t <= 3; t++) {
        // 条件
        // 1. 上下左右に同じ数字でvalidなマスが存在しない
        // 2. 開きマス+上下左右のマスの和がt以上である
        if(count2(y,x,t) + count2(y,x,0) < t) continue;
        if(y != 0 && valid[y-1][x] && number[y-1][x] == t) continue;
        if(y != R - 1 && valid[y+1][x] && number[y+1][x] == t) continue;
        if(valid[y][(x + C - 1) % C] && number[y][(x + C - 1) % C] == t) continue;
        if(valid[y][(x + C + 1) % C] && number[y][(x + C + 1) % C] == t) continue;
        pattern[y][x] |= 1 << (t-1);
      }
    }
  }
}

bool check2() {
  for(int y = 0; y < R; y++) {
    for(int x = 0; x < C; x++) {
      if(number[y][x] != 0) {
        if(!valid[y][x]) {
          if(count2(y,x,0) == 0) return false;
        }
      }
    }
  }
  return true;
}

void show_current() {
#ifndef RUN
  cout << "---- CURRENT STATUS -----" << endl;
  for(int y = 0; y < R; y++) {
    for(int x = 0; x < C; x++) {
      cout << (int)number[y][x];
    }
    cout << endl;
  }
  cout << "---VALID STATUS ---" << endl;
  for(int y = 0; y < R; y++) {
    for(int x = 0; x < C; x++) {
      cout << (int)valid[y][x];
    }
    cout << endl;
  }
#endif
}

set<vector<vector<int> > > ss;
// 答えを一つ追加する
void count2er() {
  vector<vector<int> > row(R, vector<int>(C));
  for(int y = 0; y < R; y++) {
    for(int x = 0; x < C; x++) {  
      row[y][x] = number[y][x];
    }
  }
  if(ss.count(row)) return;
  answer++;
  for(int x = 0; x < C; x++) {
    //assert(ss.count(row) == 0);
    ss.insert(row);
    for(int y = 0; y < R; y++) {
      rotate(row[y].begin(), row[y].begin()+1, row[y].end());
    }
  }
}

void solve() {
  int min_count2 = 99999;
  int tx = -1, ty = -1;
  for(int y = 0; y < R; y++) {
    for(int x = 0; x < C; x++) {
      if(number[y][x] != 0) continue;
      if(__builtin_popcount(pattern[y][x]) < min_count2) {
        min_count2 = __builtin_popcount(pattern[y][x]);
        tx = x; ty = y;
      }
    }
  }
  if(min_count2 == 0) return; // invalid
  if(!check2()) return;
  if(tx == -1) {
    // valid answer
    show_current();
    count2er();
    return;
  }
  assert(number[ty][tx] == 0);
  // 3つの数字を置く
  for(int target = 1; target <= 3; target++ ){
    if(pattern[ty][tx] >> (target - 1) & 1) {
      // 準備
      number[ty][tx] = target;
      char backup_valid[sizeof(valid)];
      char backup_pattern[sizeof(pattern)];
      memcpy(backup_valid, valid, sizeof(valid));
      memcpy(backup_pattern, pattern, sizeof(pattern));
      // msos
      update_valid(ty, tx);
      update_pattern();
      solve();
      // 戻す
      number[ty][tx] = 0;
      memcpy(valid, backup_valid, sizeof(valid));
      memcpy(pattern, backup_pattern, sizeof(pattern));
    }
  }
}

int main() {
  cin >> R >> C;
  memset(pattern, (1 << 3) - 1, sizeof(pattern));
  solve();
  cout << answer << endl;
}


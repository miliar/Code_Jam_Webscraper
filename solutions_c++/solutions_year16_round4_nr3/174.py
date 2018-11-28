#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <queue>
#include <set>
#include <map>

using namespace std;

#define ll long long
#define pii pair<int,int>

int R,C,T;
int grid[505][505];
int with[505];

bool failure;

ifstream fin("C.in");
ofstream fout("C.out");

bool check(int dir,pii loc) {
  if (dir == 0) loc.first++;
  else if (dir == 1) loc.second--;
  else if (dir == 2) loc.first--;
  else loc.second++;
  if (loc.first < 0 || loc.first >= R || loc.second < 0 || loc.second >= C) return true;
  return false;
}

void process(int a,int b) {
  int pdir,dir; //0 is going down, 1 is going left, 2 is going up, 3 is going right
  pii loc;
  if (a < C) {
    pdir = 3;
    dir = 0;
    loc = pii(-1,a);
  }
  else if (a < R+C) {
    pdir = 0;
    dir = 1;
    loc = pii(a-C,C);
  }
  else if (a < R+C+C) {
    pdir = 1;
    dir = 2;
    loc = pii(R,C-(a-R-C)-1);
  }
  else {
    pdir = 2;
    dir = 3;
    loc = pii(R-(a-R-C-C)-1,-1);
  }
  //cout << loc.first << " " << loc.second << " " << dir << "\n";
  while (!check(dir,loc)) {
    if (dir == 0) loc.first++;
    else if (dir == 1) loc.second--;
    else if (dir == 2) loc.first--;
    else loc.second++;
    if (grid[loc.first][loc.second] == 0) {
      if (dir == 0 || dir == 2) grid[loc.first][loc.second] = 2;
      else grid[loc.first][loc.second] = 1;
      /*if (dir == 0) {
        if (pdir == 3) grid[loc.first][loc.second] == 2;
        else grid[loc.first][loc.second] == 1;
      }
      else if (dir == 2) {
        if (pdir == 1) grid[loc.first][loc.second] == 2;
        else grid[loc.first][loc.second] == 1;
      }
      else if (dir == 1) {
        if (pdir == 0) grid[loc.first][loc.second] == 2;
        else grid[loc.first][loc.second] == 1;
      }
      else if (dir == 3) {
        if (pdir == 2) grid[loc.first][loc.second] == 2;
        else grid[loc.first][loc.second] == 1;
      }*/
    }
    pdir = dir;
    if (grid[loc.first][loc.second] == 2) {
      if (dir == 0) dir = 3;
      else if (dir == 1) dir = 2;
      else if (dir == 2) dir = 1;
      else dir = 0;
    }
    else {
      if (dir == 0) dir = 1;
      else if (dir == 1) dir = 0;
      else if (dir == 2) dir = 3;
      else dir = 2;
    }
    //cout << loc.first << " " << loc.second << " " << dir << "\n";
  }
  if (dir == 0) loc.first++;
  else if (dir == 1) loc.second--;
  else if (dir == 2) loc.first--;
  else loc.second++;
  int landed;
  if (loc.first == -1) landed = loc.second;
  if (loc.second == C) landed = C+loc.first;
  if (loc.first == R) landed = R+C+(C-loc.second-1);
  if (loc.second == -1) landed = R+C+C+(R-loc.first-1);
  if (landed != b) failure = true;
}

int main() {
  fin >> T;
  for (int tt = 1; tt <= T; tt++) {
    failure = false;
    cout << "Working on Case #" << tt << "\n";
    fin >> R >> C;
    for (int i = 0; i < R; i++) {
    	for (int j = 0; j < C; j++) grid[i][j] = 0;
    }
    for (int i = 0; i < R+C; i++) {
      int a,b;
      fin >> a >> b;
      a--; b--;
      with[a] = b;
      with[b] = a;
    }
    vector<int> todo;
    for (int i = 0; i < 2*(R+C); i++) todo.push_back(i);
    bool flag = true;
    while (flag) {
      flag = false;
      for (int i = 0; i < todo.size(); i++) {
        if (with[todo[i]] == todo[(i+1)%todo.size()]) {
          //cout << "LINKED " << todo[i] << " " << todo[(i+1)%todo.size()] << "\n";
          process(todo[i],todo[(i+1)%todo.size()]);
          if (failure) break;
          if (i == todo.size()-1) {
            todo.erase(todo.end()-1);
            todo.erase(todo.begin());
          }
          else {
            todo.erase(todo.begin()+i);
            todo.erase(todo.begin()+i);
          }
          flag = true;
          break;
        }
      }
    }
    fout << "Case #" << tt << ":\n";
    if (failure || todo.size() != 0) fout << "IMPOSSIBLE\n";
    else {
      for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
          if (grid[i][j] == 1) fout << "/";
          else fout << "\\";
        }
        fout << "\n";
      }
    }
  }
  return 0;
}
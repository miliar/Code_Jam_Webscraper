#include <iostream>
#include <cstdio>
#include <string.h>
#include <vector>
#include <map>
using namespace std;

const int BMAX = 12;
int board[BMAX][BMAX];
int rev_board[BMAX][BMAX];
void Init() {
  for (int i = 0; i < BMAX; ++i) {
    for (int j = 0; j < BMAX; ++j) {
      board[i][j] = 0;
      rev_board[i][j] = 0;
    }
  }
}

void Input(int &n, int &m) {
  scanf("%d%d", &n, &m);
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < m; ++j) {
      scanf("%d", &board[i][j]);
      rev_board[j][i] = board[i][j];
    }
  }
}

pair<int, int> GetHor(int board[BMAX][BMAX], int bn, int bm, int row) {
  int value = -1;
  for (int c = 0; c < bm; ++c) {
    if (value == -1 || value < board[row][c]) {
      value = board[row][c];
    }
  }
  return pair<int, int>(row, value);
}

vector<pair<int, int> > GetVer(int board[BMAX][BMAX], int bn, int bm, int row) {
  pair<int, int> hor_move = GetHor(board, bn, bm, row);
  vector<pair<int, int> > ret;
  for (int c = 0; c < bm; ++c) {
    if (hor_move.second > board[row][c]) {
      ret.push_back(pair<int, int>(c, board[row][c]));
    }
  }
  return ret;
}

bool Judge(int board[BMAX][BMAX], int bn, int bm) {
  map<int, int> table;
  table.clear();
  for (int r = 0; r < bn; ++r) {
    vector<pair<int, int> > moves = GetVer(board, bn, bm, r);
    for (int e = 0; e < moves.size(); ++e) {
      int key = moves[e].first;
      int value = moves[e].second;
      if (table.count(key) == 0) {
	table[key] = value;
      } else {
	if (table[key] != value) {
	  return false;
	}
      }
    }
  }

  int test_board[BMAX][BMAX];
  for (int i = 0; i < bn; ++i) {
    pair<int, int> move = GetHor(board, bn, bm, i);
    for (int j = 0; j < bm; ++j) {
      test_board[i][j] = move.second;
    }
  }

  for (map<int, int>::iterator it = table.begin(); it != table.end(); ++it) 
    int col = it->first;
    int value = it->second;
    for (int i = 0; i < bn; ++i) {
      test_board[i][col] = value;
    }
  }
  for (int i = 0; i < bn; ++i) {
    for (int j = 0; j < bm; ++j) {
      if (board[i][j] != test_board[i][j]) {
	return false;
      }
    }
  }
  return true;
}

int main() {
  //  freopen("in.txt", "r", stdin);
  int go = 0;
  scanf("%d", &go);
  int n, m;
  for (int i = 1; i <= go; ++i) {
    Input(n, m);
    bool ans = Judge(board, n, m) & Judge(rev_board, m, n);
    printf("Case #%d: ", i);
    if (ans) {
      printf("YES\n");
    } else {
      printf("NO\n");
    }
  }
  
  return 0;
}

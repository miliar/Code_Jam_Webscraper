#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <string>
using namespace std;

typedef vector< vector<int> > Board;
void input(Board& board, bool& completed);
int check(Board& board, bool completed);
bool check(Board& board, int flag);
void output(int t, int res);
int main(){
  freopen("TTTT.in", "r", stdin);
  freopen("TTTT.res", "w", stdout);
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    Board board;
    bool completed;
    input(board, completed);
    output(t, check(board, completed));
    board.clear(); 
  }
  fclose(stdin);
  fclose(stdout);
  return 0;
}

void input(Board& board, bool& completed){
  completed = true;
  string str;
  for (int i = 0; i < 4; ++i) {
    cin >> str;
    vector<int> row;
    for (int j = 0; j < 4; ++j) {
      switch ((char)str.at(j)) {
        case 'X': row.push_back(0); break;
        case 'O': row.push_back(1); break;
        case 'T': row.push_back(-1); break;
        case '.': row.push_back(-2); completed = false; break;
        default : ; 
      }
    }
    board.push_back(row);
  } 
}


bool check(Board& board, int flag){
  //row
  for (int i = 0; i < 4; ++i) {
    bool res = true;
    for (int j = 0; j < 4; ++j) {
      if (board[i][j] != flag && board[i][j] != -1) {
        res = false; 
        break;
      }
    }
    if (res) return res;
  }
  //col
  for (int i = 0; i < 4; ++i) {
    bool res = true;
    for (int j = 0; j < 4; ++j) {
      if (board[j][i] != flag && board[j][i] != -1) {
        res = false; 
        break;
      }
    }
    if (res) return res;
  }
  //
  bool res = true;
  for (int i = 0; i < 4; ++i) {
    if (board[i][i] != flag && board[i][i] != -1) {
      res = false; 
      break;
    }
  }
  if (res) return res;
  //
  res = true;
  for (int i = 0; i < 4; ++i) {
    if (board[i][3-i] != flag && board[i][3-i] != -1) {
      res = false; 
      break;
    }
  }   
  return res;
}
int check(Board& board, bool completed){
  if (check(board, 0)) return 0;
  if (check(board, 1)) return 1;
  return completed ? 2 : 3;
}

void output(int t, int res) {
  cout << "Case #"<< t << ": ";
  switch (res) {
    case 0: cout << "X won" << endl; break;
    case 1: cout << "O won" << endl; break;
    case 2: cout << "Draw" << endl;  break;
    case 3: cout << "Game has not completed" << endl; break;
    default:; 
  }
}


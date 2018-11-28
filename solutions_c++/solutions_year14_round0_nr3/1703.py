#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <list>
 
using namespace std;

class board {
 public:
  char pos[50*50];
  board() {
    for (int m=0; m<50*50; m++) {
      pos[m] = ' ';
    }
  }
};
 
class qc {
 public:
  qc() {
  }

  ostringstream convert;

  int count_neighbor_mines(board b, int loc) {
    int row = get_row(loc);
    int col = get_col(loc);
    int count = 0;

    if (row!=0   && col!=0   && b.pos[loc-C-1] == '*') count++;
    if (row!=0               && b.pos[loc-C] == '*') count++;
    if (row!=0   && col!=C-1 && b.pos[loc-C+1] == '*') count++;
    if (            col!=0   && b.pos[loc-1] == '*') count++;
    if (            col!=C-1 && b.pos[loc+1] == '*') count++;
    if (row!=R-1 && col!=0   && b.pos[loc+C-1] == '*') count++;
    if (row!=R-1             && b.pos[loc+C] == '*') count++;
    if (row!=R-1 && col!=C-1 && b.pos[loc+C+1] == '*') count++;

    return count;
  }

  board reveal(board b, int loc) {
    b.pos[loc] = '.';
    if (count_neighbor_mines(b, loc) != 0) {
      // stop it now
      return b;
    }
    else {
      int row = get_row(loc);
      int col = get_col(loc);

      if (row!=0   && col!=0   && b.pos[loc-C-1] == ' ') b = reveal(b, loc-C-1);
      if (row!=0               && b.pos[loc-C] == ' ') b = reveal(b, loc-C);
      if (row!=0   && col!=C-1 && b.pos[loc-C+1] == ' ') b = reveal(b, loc-C+1);
      if (            col!=0   && b.pos[loc-1] == ' ') b = reveal(b, loc-1);
      if (            col!=C-1 && b.pos[loc+1] == ' ') b = reveal(b, loc+1);
      if (row!=R-1 && col!=0   && b.pos[loc+C-1] == ' ') b = reveal(b, loc+C-1);
      if (row!=R-1             && b.pos[loc+C] == ' ') b = reveal(b, loc+C);
      if (row!=R-1 && col!=C-1 && b.pos[loc+C+1] == ' ') b = reveal(b, loc+C+1);

      return b;
    }
  }

  bool is_all_not_mines_revealed(board b) {
    for (int m=0; m<R*C; m++) {
      if (b.pos[m] == ' ') {
        return false;
      }
    }
    return true;
  }

  bool is_one_click_win(board b) {

    for (int m=0; m<R*C; m++) {
      board b_analyze = b;

      if (b_analyze.pos[m] == '*') return false;
      b_analyze = reveal(b_analyze,m);
      b_analyze.pos[m] = 'c';

      if (is_all_not_mines_revealed(b_analyze)) {

        for (int j=0; j<R; j++) {
          for (int n=0; n<C; n++) {
            convert << b_analyze.pos[get_index(j, n)];
          }
          convert << endl;
        }
        convert << endl;

        return true;

      }
    }
    return false;
  }

  int get_row(int pos) { return pos/C; }
  int get_col(int pos) { return pos%C; }
  int get_index(int row, int col) { return (row*C)+col; }

  bool build(board b, int cur, bool is_mines, int mines_left) {

    if (mines_left == 0 && is_mines == true) {
      return false;
    }

    b.pos[cur] = is_mines ? '*' : ' ';
    if (is_mines) mines_left--;

    if (mines_left == 0 || cur == (C*R)-1) {
      if (mines_left > 0)
        return false;
      else
        return is_one_click_win(b);
    }
    else {
      cur++;
      if (build(b, cur, true, mines_left))
        return true;
      else if (build(b, cur, false, mines_left))
        return true;
      else
        return false;
    }
  }

  string solve() {
    board b;
    int cur = 0;
    int mines_left = M;

    if (build(b, cur, true, M))
      return convert.str();
    else if (build(b, cur, false, M))
      return "\n" + convert.str();
    else
      return "\nImpossible";
  }

  int R, C, M;

};
 
int main (void) {
  int n, T;

  cin >> T;

  for (n=1; n<=T; n++) {  
    qc *solver = new qc();
    cin >> solver->R >> solver->C >> solver->M;
    cout << "Case #" << n << ": " << solver->solve() << endl;
  }

  return 0;
}

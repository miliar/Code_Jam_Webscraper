#include <iostream>
#include <vector>
#include <string>

using namespace std;

#define for0(i, n) for(int (i) = 0; (i) < (n); (i)++)
#define sz size()
#define CHECKING -1
#define X_WON 0
#define Y_WON 1
#define DRAW 2
#define INCOMPLETE 3

bool check_row(string row, char c) {
  for0(i, row.sz) {
    if (row[i] == 'T') {
      continue;
    }
    if (row[i] != c) {
      return false;
    }
  }
  return true;
}

bool check_column(vector<string> &table, int col, char c) {
  for0(i, table.sz) {
    if (table[i][col] == 'T') {
      continue;
    }
    if (table[i][col] != c) {
      return false;
    }
  }
  return true;
}

bool check_diags(vector<string> &table, char c) {
  bool forwards = true;
  for0(i, table.sz) {
    if (table[i][i] == 'T') {
      continue;
    }
    if (table[i][i] != c) {
      forwards = false;
    }
  }
  
  bool backwards = true;
  for0(i, table.sz) {
    if (table[table.sz - i - 1][i] == 'T') {
      continue;
    }
    if (table[table.sz - i - 1][i] != c) {
      backwards = false;
    }
  }
  
  return forwards || backwards;
}

void do_output(int t, int status) {
  cout << "Case #" << t << ": ";
  switch(status) {
    case X_WON:
      cout << "X won" << endl;
      break;
    case Y_WON:
      cout << "O won" << endl;
      break;
    case DRAW:
      cout << "Draw" << endl;
      break;
    case INCOMPLETE:
      cout << "Game has not completed" << endl;
      break;
    default:
      break;
  }
}

int main() {
  int T = 0;
  cin >> T >> ws;
  for0(t, T) {
    vector< string > table(4);
    for0(i, 4) {
      getline(cin, table[i]);
      cin >> ws;
    }
    
    int status = CHECKING;
    // check rows
    for0(i, table.sz) {
      if (check_row(table[i], 'X')) {        
        status = X_WON;
        break;
      }
      if (check_row(table[i], 'O')) {
        status = Y_WON;
        break;
      }
    }
    
    if (status == X_WON) {
      do_output(t + 1, status);
      continue;
    } else if (status == Y_WON) {
      do_output(t + 1, status);
      continue;
    }
    
    // check columns
    for0(j, 4) {
      if (check_column(table, j, 'X')) {
        status = X_WON;
        break;
      }
      if (check_column(table, j, 'O')) {
        status = Y_WON;
        break;
      }
    }

    if (status == X_WON) {
      do_output(t + 1, status);
      continue;
    } else if (status == Y_WON) {
      do_output(t + 1, status);
      continue;
    }
    
    // check diagonals
    if (check_diags(table, 'X')) {
      do_output(t + 1, X_WON);
      continue;
    } else if (check_diags(table, 'O')) {
      do_output(t + 1, Y_WON);
      continue;
    }
    
    for0(i, table.sz) {
      for0(j, table[i].sz) {
        if (table[i][j] == '.') {
          status = INCOMPLETE;
          break;
        }
      }
      if (status == INCOMPLETE)
        break;
    }
    
    if (status == INCOMPLETE) {
      do_output(t + 1, status);
      continue;
    } else {
      do_output(t + 1, DRAW);
      continue;
    }
  }
  return 0;
}
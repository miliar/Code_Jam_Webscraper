#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

class TicTacToe {
 public:
   vector<vector<char> > board_;
   bool has_dot_;
   TicTacToe() {
     vector<char> row;
     for (int i = 0; i < 4; ++i)
       row.push_back('.');
     for (int i = 0; i < 4; ++i)
       board_.push_back(row);
     has_dot_ = false;
   }
   void Dump() {
     for (int i = 0; i < 4; ++i) {
       for (int j = 0; j < 4; ++j) {
         cout << board_[i][j] << " ";
       }
       cout << endl;
     }
   }
   void Read() {
     string line;
     for (int i = 0; i < 4; ++i) {
       getline(cin, line);
       // cout << "Line: " << line << endl;
       for (int j = 0; j < 4; ++j) {
         board_[i][j] = line[j];
         if (board_[i][j] == '.')
           has_dot_ = true;
       }
     }
     getline(cin, line);
   }

   string WinColumnRow(int c, int row) {
     // cout << "Row is " << row << endl;
     char seen = ' ';
     for (int i = 0; i < 4; ++i) {
       char cur = ' ';
       if (row == 1)
         cur = board_[c][i];
       else if (row == 0)
         cur = board_[i][c];
       else if (row == 2)
         cur = board_[i][i];
       else 
         cur = board_[i][3 - i];

       // cout << "Cur is " << i << ":" << cur << endl;
       if (cur == 'T')
         continue;
       if (cur == '.')
         return "";
       if (seen == ' ')
         seen = cur;
       if (cur != seen)
         return "";
     }
     // cout << "===\n";
     char blah[2] = " ";
     blah[0] = seen;
     string r = blah;
     return r;
   }

   string Result() {
     string r;
     for (int c = 0; c < 4; ++c) {
       // cout << "Col " << c << endl;
       if ((r=WinColumnRow(c, 0)) != "")
         return r + " won";
       if ((r=WinColumnRow(c, 1)) != "")
         return r + " won";
     }
     if ((r=WinColumnRow(0, 2)) != "")
       return r + " won";
     if ((r=WinColumnRow(0, 3)) != "")
       return r + " won";

     if (has_dot_)
       return "Game has not completed";
     else
       return "Draw";
   }


};

int main() {
  int ncases = 0;
  string line;
  getline(cin, line);
  istringstream iss(line);
  iss >> ncases;
  char c;
  for (int i = 0; i < ncases; ++i) {
    TicTacToe t;
    t.Read();
  //  t.Dump();
    cout << "Case #" << (i+1) << ": " << t.Result() << endl;
  }

  return 0;
}

#include <iostream>
#include <sstream>
using namespace std;

char t[4][4];

void read() {
  char nl;
  for (int i=0; i<4; i++) {
    for (int j=0; j<4; j++) {
      cin >> t[i][j];
    }
  }
}

void print() {
  for (int i=0; i<4; i++) {
    for (int j=0; j<4; j++) {
      cout << t[i][j];
    }
    cout << endl;
  }
  cout << endl;
}

string solve() {
  bool finish = true;
  string winner;
  for (int i=0; i<4; i++) {
    char target = 0;
    for (int j=0; j<4; j++) {
      if (t[i][j] == '.') {
        finish = false;
        break;
      }
      if (t[i][j] == 'T') {
        if (j == 3) {
          stringstream ss;
          ss << target << " won";
          return ss.str();
        }
        continue;
      }
      if (t[i][j] == 'X' || t[i][j] == 'O') {
        if (target == 0) {
          target = t[i][j];
        }
        else if (target != t[i][j])
          break;
        else if (target == t[i][j]) {
          if (j == 3) {
            stringstream ss;
            ss << target << " won";
            return ss.str();
          }
        }
      }
    }
  }

  for (int i=0; i<4; i++) {
    char target = 0;
    for (int j=0; j<4; j++) {
      if (t[j][i] == '.') {
        finish = false;
        break;
      }
      if (t[j][i] == 'T') {
        if (j == 3) {
          stringstream ss;
          ss << target << " won";
          return ss.str();
        }
        continue;
      }
      if (t[j][i] == 'X' || t[j][i] == 'O') {
        if (target == 0) {
          target = t[j][i];
        }
        else if (target != t[j][i])
          break;
        else if (target == t[j][i]) {
          if (j == 3) {
            stringstream ss;
            ss << target << " won";
            return ss.str();
          }
        }
      }
    }
  }

  char target = 0;
  for (int i=0; i<4; i++) {
    if (t[i][i] == '.') {
      finish = false;
      break;
    }
    if (t[i][i] == 'T') {
      if (i == 3) {
        stringstream ss;
        ss << target << " won";
        return ss.str();
      }
      continue;
    }
    if (t[i][i] == 'X' || t[i][i] == 'O') {
      if (target == 0) {
        target = t[i][i];
      }
      else if (target != t[i][i])
        break;
      else if (target == t[i][i]) {
        if (i == 3) {
          stringstream ss;
          ss << target << " won";
          return ss.str();
        }
      }
    }
  }

  target = 0;
  for (int i=0; i<4; i++) {
    if (t[i][3-i] == '.') {
      finish = false;
      break;
    }
    if (t[i][3-i] == 'T') {
      if (i == 3) {
        stringstream ss;
        ss << target << " won";
        return ss.str();
      }
      continue;
    }
    if (t[i][3-i] == 'X' || t[i][3-i] == 'O') {
      if (target == 0) {
        target = t[i][3-i];
      }
      else if (target != t[i][3-i])
        break;
      else if (target == t[i][3-i]) {
        if (i == 3) {
          stringstream ss;
          ss << target << " won";
          return ss.str();
        }
      }
    }
  }

  if (finish)
    return "Draw";
  else
    return "Game has not completed";
}

int main()
{
  int T;
  cin >> T;
  for (int i=0; i<T; i++) {
    read();
    string ret = solve();
    cout << "Case #" << i+1 << ": " << ret << endl;
  }
  return 0;
}

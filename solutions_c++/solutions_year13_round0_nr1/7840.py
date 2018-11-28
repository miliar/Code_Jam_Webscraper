#include <cstdio>
#include <algorithm>
#include <iostream>
#include <vector>
#define dbg true
#define numRows 4
#define ok(x, y) (x>=0 && y>=0 && x < numRows && y < numRows)
using namespace std;

int main() {
  int T;
  cin >> T;
  string input[numRows];
  for (int testCase = 1; testCase <= T; testCase++) {
    for (int i = 0; i < numRows; i++) {
      cin >> input[i];
    }
    if (dbg) cout << "Case #" << testCase << endl;
    for (int j = 0; j < numRows; j++) {
      if (dbg) cout << input[j] << endl;
    }
    int xs = 0, os = 0, dots = 0;
    int ti = -1, tj = -1;
    // X starts first
    for (int i = 0; i < numRows; i++) {
      for (int j = 0; j < numRows; j++) {
        char c = input[i][j];
        switch (c) {
          case 'X' :
            xs++;
            break;
          case 'O' :
            os++;
            break;
          case 'T' :
            ti = i;
            tj = j;
            break;
          case '.' :
            dots++;
            break;
        }
      }
    }
    // sweeps => {L->R, T->B, Diag-L-R, Diag-R-L}
    int di[] = {0, 1, 1, 1};
    int dj[] = {1, 0, 1, -1};
    string tmpStuff[] = {"L-R", "T-B", "Diag-L-R", "Diag-R-L"};

    vector<int> si[numRows];
    vector<int> sj[numRows];
    for (int i = 0; i < numRows; i++) {
      si[0].push_back(i);
      sj[0].push_back(0);
      if (i > 0) {
        si[2].push_back(i);
        sj[2].push_back(0);
      }
      si[1].push_back(0);
      sj[1].push_back(i);
      if (i < (numRows - 1)) {
        si[3].push_back(i);
        sj[3].push_back(numRows - 1);
      }
      si[2].push_back(0);
      sj[2].push_back(i);
      si[3].push_back(numRows - 1);
      sj[3].push_back(i);

    }
    int maxCnt = 0;
    char winner = '.';
    bool done = false;
    for (int i = 0; i < numRows && !done; i++) {
      if (dbg) cout << tmpStuff[i] << endl;
      for (int j = 0; j < si[i].size() && !done; j++) {
        int tsi = si[i][j];
        int tsj = sj[i][j];
        char prev = '.';
        int cnt = 0;
        while (ok(tsi, tsj)) {
          char cur = input[tsi][tsj];

          switch (prev) {
            case '.' :
              cnt = cur == '.' ? 0 : 1;
              prev = cur;
              break;
            case 'X' :
            case 'O' :
              cnt = cnt + (cur == prev ? 1 : (cur == 'T'));
              cnt = ((cur == 'T' || cur == prev) ? cnt : cur != '.');
              prev = (cur == 'T' ? prev : cur);
              break;
            case 'T' :
              cnt = cnt + (cur != '.');
              cnt = cur == '.' ? 0 : cnt;
              prev = cur;
              break;
          }
          if (cnt > maxCnt) {
            maxCnt = cnt;
            winner = prev;
            if (maxCnt == 4) {
              done = true;
            }
          }
          if (dbg) cout << "(" << tsi << "," << tsj << "," << cur << "," << cnt << "," << winner << ")";
          tsi = tsi + di[i];
          tsj = tsj + dj[i];
        }
        if (dbg) cout << endl;
      }
    }
    cout << "Case #" << testCase << ": ";
    if (winner == '.') {
      cout << "Game has not completed";
    } else {
      if (!done) {
        if (dots > 0) {
          cout << "Game has not completed";
        } else {
          cout << "Draw";
        }
      } else {
        cout << winner << " won";
      }
    }
    cout << endl;
    if (dbg) cout << "xs : " << xs << " os : " << os << " ti : " << ti << " tj : " << tj << endl;
  }

  return 0;
}

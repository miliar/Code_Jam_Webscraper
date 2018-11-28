#include <iostream>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int i = 0; i < T; ++i) {
    int R, C;
    cin >> R >> C;
    char **cells = new char*[R];
    for (int j = 0; j < R; ++j) {
      cells[j] = new char[C];
      for (int k = 0; k < C; ++k) {
        char read;
        cin >> read;
        // cout << "Got: " << read << endl;
        cells[j][k] = read;
      }
    }

    int total = 0;
    bool imp = false;

    // Left-side
    for (int j = 0; j < R; ++j) {
      for (int k = 0; k < C; ++k) {
        char cur = cells[j][k];
        if (cur == '<') {
          bool top = false, bot = false, left = false, right = false;
          // Top
          for (int l = j-1; l >= 0; --l) {
            if (cells[l][k] != '.') {
              top = true;
              break;
            }
          }
          // Bot
          for (int l = j+1; l < R; ++l) {
            if (cells[l][k] != '.') {
              bot = true;
              break;
            }
          }
          // Left
          for (int l = k-1; l >= 0; --l) {
            if (cells[j][l] != '.') {
              left = true;
              break;
            }
          }
          // Left
          for (int l = k+1; l < C; ++l) {
            if (cells[j][l] != '.') {
              right = true;
              break;
            }
          }

          if ((cur == '<' && left) ||
              (cur == '>' && right) ||
              (cur == '^' && top) ||
              (cur == 'v' && bot)) {
            continue;
          }
          else if (top) {
            cells[j][k] = '^';
            total++;
            continue;
          }
          else if (bot) {
            cells[j][k] = 'v';
            total++;
            continue;
          }
          else if (right) {
            cells[j][k] = '>';
            total++;
            continue;
          }
          else if (left) {
            cells[j][k] = '<';
            total++;
            continue;
          }
          else {
            imp = true;
            break;
          }
        }
      }
      if (imp) break;
    }
    if (imp) {
      cout << "Case #" << i+1 << ": ";
      cout << "IMPOSSIBLE" << endl;
      continue;
    }
    // Right-side
    for (int j = 0; j < R; ++j) {
      for (int k = C-1; k >= 0; --k) {
        char cur = cells[j][k];
        if (cur == '>') {
          bool top = false, bot = false, left = false, right = false;
          // Top
          for (int l = j-1; l >= 0; --l) {
            if (cells[l][k] != '.') {
              top = true;
              break;
            }
          }
          // Bot
          for (int l = j+1; l < R; ++l) {
            if (cells[l][k] != '.') {
              bot = true;
              break;
            }
          }
          // Left
          for (int l = k-1; l >= 0; --l) {
            if (cells[j][l] != '.') {
              left = true;
              break;
            }
          }
          // Left
          for (int l = k+1; l < C; ++l) {
            if (cells[j][l] != '.') {
              right = true;
              break;
            }
          }

          if ((cur == '<' && left) ||
              (cur == '>' && right) ||
              (cur == '^' && top) ||
              (cur == 'v' && bot)) {
            continue;
          }
          else if (top) {
            cells[j][k] = '^';
            total++;
            continue;
          }
          else if (bot) {
            cells[j][k] = 'v';
            total++;
            continue;
          }
          else if (right) {
            cells[j][k] = '>';
            total++;
            continue;
          }
          else if (left) {
            cells[j][k] = '<';
            total++;
            continue;
          }
          else {
            imp = true;
            break;
          }
        }
      }
      if (imp) break;
    }
    if (imp) {
      cout << "Case #" << i+1 << ": ";
      cout << "IMPOSSIBLE" << endl;
      continue;
    }
    // Top-side
    for (int k = 0; k < C; ++k) {
      for (int j = 0; j < R; ++j) {
        char cur = cells[j][k];
        if (cur == '^') {
          bool top = false, bot = false, left = false, right = false;
          // Top
          for (int l = j-1; l >= 0; --l) {
            if (cells[l][k] != '.') {
              top = true;
              break;
            }
          }
          // Bot
          for (int l = j+1; l < R; ++l) {
            if (cells[l][k] != '.') {
              bot = true;
              break;
            }
          }
          // Left
          for (int l = k-1; l >= 0; --l) {
            if (cells[j][l] != '.') {
              left = true;
              break;
            }
          }
          // Left
          for (int l = k+1; l < C; ++l) {
            if (cells[j][l] != '.') {
              right = true;
              break;
            }
          }

          if ((cur == '<' && left) ||
              (cur == '>' && right) ||
              (cur == '^' && top) ||
              (cur == 'v' && bot)) {
            continue;
          }
          else if (top) {
            cells[j][k] = '^';
            total++;
            continue;
          }
          else if (bot) {
            cells[j][k] = 'v';
            total++;
            continue;
          }
          else if (right) {
            cells[j][k] = '>';
            total++;
            continue;
          }
          else if (left) {
            cells[j][k] = '<';
            total++;
            continue;
          }
          else {
            imp = true;
            break;
          }
        }
      }
      if (imp) break;
    }
    if (imp) {
      cout << "Case #" << i+1 << ": ";
      cout << "IMPOSSIBLE" << endl;
      continue;
    }
    // Bot-side
    for (int k = C-1; k >= 0; --k) {
      for (int j = 0; j < R; ++j) {
        char cur = cells[j][k];
        if (cur == 'v') {
          bool top = false, bot = false, left = false, right = false;
          // Top
          for (int l = j-1; l >= 0; --l) {
            if (cells[l][k] != '.') {
              top = true;
              break;
            }
          }
          // Bot
          for (int l = j+1; l < R; ++l) {
            if (cells[l][k] != '.') {
              bot = true;
              break;
            }
          }
          // Left
          for (int l = k-1; l >= 0; --l) {
            if (cells[j][l] != '.') {
              left = true;
              break;
            }
          }
          // Left
          for (int l = k+1; l < C; ++l) {
            if (cells[j][l] != '.') {
              right = true;
              break;
            }
          }

          if ((cur == '<' && left) ||
              (cur == '>' && right) ||
              (cur == '^' && top) ||
              (cur == 'v' && bot)) {
            continue;
          }
          else if (top) {
            cells[j][k] = '^';
            total++;
            continue;
          }
          else if (bot) {
            cells[j][k] = 'v';
            total++;
            continue;
          }
          else if (right) {
            cells[j][k] = '>';
            total++;
            continue;
          }
          else if (left) {
            cells[j][k] = '<';
            total++;
            continue;
          }
          else {
            imp = true;
            break;
          }
        }
      }
      if (imp) break;
    }
    if (imp) {
      cout << "Case #" << i+1 << ": ";
      cout << "IMPOSSIBLE" << endl;
      continue;
    }
    cout << "Case #" << i+1 << ": ";
    cout << total << endl;
  }
}

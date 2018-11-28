#include <iostream>
#include <vector>

using namespace std;

void eval(char board[][4], int test);

int main(int argc, char** argv) {
  int N;
  char board[4][4] = { {0,0,0,0},{0,0,0,0}, {0,0,0,0}, {0,0,0,0} };
  // newline vector<vector<char> > board = vector(vector<int>(4));
  // string newline;
  cin >> N;
  for (int i = 0; i < N; ++i) {
    for (int r = 0; r < 4; ++r)
      for (int c = 0; c < 4; ++c) {
        cin >> board[r][c];
      }
    eval(board, i + 1);
    // cin.readLine();
  }
}

bool find(char board[][4], char& ch, int r, int c, bool& empty) {
  if (ch == 'T')
    ch = board[r][c];
  // cout << "(" << ch << "); " << r << ", " << c << ": " << board[r][c] << endl;
  if (board[r][c] == '.') {
    empty = true;
    return false;
  }
  if (board[r][c] != ch && board[r][c] != 'T')  {
    return false;
  }
  return true;
}

void eval(char board[][4], int test) {
  // for (int r = 0; r < 4; ++r) {
  //   for (int c = 0; c < 4; ++c)
  //     cout << board[r][c];
  //   cout << "\n";
  // }
  
  bool empty = false;
  char result[30] = "";
  for (int r = 0; r < 4; ++r) {
    char ch = board[r][0];
    bool found = true;
    for (int c = 1; c < 4; ++c) {
      found = find(board, ch, r, c, empty);
      if (!found) break;
    }
    if (found) sprintf(result, "%c won", ch);
  }
  for (int c = 0; c < 4; ++c) {
    char ch = board[0][c];
    bool found = true;
    for (int r = 1; r < 4; ++r) {
      found = find(board, ch, r, c, empty);
      if (!found) break;
    }
    if (found) sprintf(result, "%c won", ch);
  }
  char ch = board[0][0];
  bool found = true;
  for (int r = 1, c = 1; r < 4; ++r,++c) {
    found = find(board, ch, r, c, empty);
    if (!found) break;
  }
  if (found) sprintf(result, "%c won", ch);
  ch = board[0][3];
  found = true;
  for (int r = 1, c = 2; r < 4; ++r,--c) {
    found = find(board, ch, r, c, empty);
    if (!found) break;
  }
  if (found) sprintf(result, "%c won", ch);

  if (strlen(result) == 0) {
    if (empty)
      sprintf(result, "Game has not completed");
    else
      sprintf(result, "Draw");
  }
  cout << "Case #" << test << ": " << result << "\n";

}

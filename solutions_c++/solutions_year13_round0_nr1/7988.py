#include <iostream>
#include <string>
using namespace std;

int judge(char b[][4], char c);

int main() {
  int T = 0;
  cin >> T;
  cin.ignore();
  for (auto i=0; i<T; ++i) {
    cout << "Case #" << i+1 << ": ";
    char b[4][4];
    for (auto y=0; y<4; ++y) {
      string G;
      getline(cin, G);
      for (auto x=0;x<4;++x) {
	b[y][x] = G[x];
      }
    }
    cin.ignore();
    //    cout << endl;
    // for (auto y=0; y<4; ++y) {
    //   for (auto x=0; x<4; ++x) { cout << b[y][x]; }
    //   cout << endl;
    // } cout << endl;
    int ret = 0;
    ret = judge(b, 'X');
    if (ret==1) {
      cout << "X won" << endl;
    } else if (ret==2) {
      cout << "Draw" << endl;
    } else {
      ret = judge(b, 'O');
      if (ret==1) {
	cout << "O won" << endl;
      } else if (ret == 2) {
	cout << "Draw" << endl;
      } else {
	cout << "Game has not completed" << endl;
      }
    }
  } // T loop
}

int judge(char b[][4], char c)
{
  int count = 0;
  for (auto i=0;i<4;++i) {
    if (b[i][i] == c || b[i][i] == 'T') {
      ++count;
    } else {
      break;
    }
  }
  if (count == 4) return 1;
  count = 0;
  for (auto i=0;i<4;++i) {
    if (b[i][3-i] == c || b[i][3-i] == 'T') {
      ++count;
    } else { break; }
  }
  if (count == 4) return 1;
  count = 0;
  for (auto y=0;y<4;++y) {
    for (auto x=0;x<4;++x) {
      if (b[y][x]==c || b[y][x]=='T') {
	++count;
      } else { break; }
    }
    if (count == 4) { return 1; }
    else { count = 0; }
  }
  count=0;
  for (auto y=0;y<4;++y) {
    for (auto x=0;x<4;++x) {
      if (b[x][y]==c || b[x][y]=='T') {
	++count;
      } else { break; }
    }
    if (count == 4) { return 1; }
    else { count = 0; }
  }
  // draw
  count=0;
  for (auto y=0;y<4;++y) {
    for (auto x=0;x<4;++x) {
      if (b[y][x]=='.') {
	++count;
      }
    }
  }
  if(count==0) return 2;
  return 0;
}

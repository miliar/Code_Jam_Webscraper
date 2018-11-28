#include <iostream>
#include <string>
#include <vector>
using namespace std;

bool won(vector<string>& b, char ch) {

  for(int i = 0; i < 4; ++i) {
    int j = 0;
    while(j < 4 && (b[i][j] == ch || b[i][j] == 'T')) j++;
    if (j == 4) return true;
    j = 0;
    while(j < 4 && (b[j][i] == ch || b[j][i] == 'T')) j++;
    if (j == 4) return true;
    j = 0;
    while(j < 4 && (b[j][j] == ch || b[j][j] == 'T')) j++;
    if (j == 4) return true;
    j = 0;
    while(j < 4 && (b[j][3-j] == ch || b[j][3-j] == 'T')) j++;
    if (j == 4) return true;
  }
  return false;
}

bool draw(vector<string>& b) {
  for(int i = 0; i < 4; ++i)
    for(int j = 0; j < 4; ++j)
      if (b[i][j] == '.') return false;
  return true;
}

int main() {
  int T;
  cin >> T;
  int ctr = 0;
  while(T--) {
    vector<string> b(4);
    for(int i = 0; i < 4; ++i)
      cin >> b[i];
    if (won(b,'X'))
      std::cout << "Case #" << ++ctr << ": X won\n";
    else if(won(b,'O'))
      std::cout << "Case #" << ++ctr << ": O won\n";
    else if(draw(b))
      std::cout << "Case #" << ++ctr << ": Draw\n";
    else
      std::cout << "Case #" << ++ctr << ": Game has not completed\n";
  }
}

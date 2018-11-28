#include <iostream>
#include <fstream>
#include <string.h>

using namespace std;

int func(int maxShyness, const char *str) {
  int total = 0, needed = 0;
  for (int i = 0; i < maxShyness + 1; i++) {
    int levelNum = ((int) *(str + i)) - 48;
    if ((i > total) && (levelNum != 0)) {
      needed += (i - total);
      total += needed;
    }
    total += levelNum;
  }
  return needed;
}

int main(int argc, char *argv[]) {
  int numTestCases;
  ifstream ifs(argv[1]);
  ofstream ofs("small.out");
  ifs >> numTestCases;
  for (int i = 0; i < numTestCases; i++) {
    int maxShy;
    ifs >> maxShy;
    string str;
    ifs >> ws;
    getline(ifs, str);
    ofs << "Case #" << (i + 1) << ": " << func(maxShy, str.c_str()) << '\n';
  }
  ifs.close();
  ofs.close();
}

#include <iostream>
#include <cstdio>
#include <string>
#include <cassert>

#define NDEBUG

int max(int a , int b) {
  return (a > b) ? a : b;
}

int min(int a , int b) {
  return (a < b) ? a : b;
}

using namespace std;

const char INPUT[] = "HelloWorld.inp";
const char OUTPUT[] = "HelloWorld.out";

int main() {
  freopen(INPUT, "r", stdin);
  freopen(OUTPUT, "w", stdout);

  int numTest;
  cin >> numTest;

  for (int idTest = 0; idTest < numTest; ++ idTest) {
    string inputLine;
    cin >> inputLine;

    //cerr << "\"" << inputLine << "\"" << endl;

    int maxFlipForHappy = 0;
    int maxFlipForBlank = 0;

    for (int id = 0; id < inputLine.size(); ++ id) {
      assert(inputLine[id] == '+' || inputLine[id] == '-');
      if (id == 0) {
        if (inputLine[id] == '+') {
          maxFlipForHappy = 0;
          maxFlipForBlank = 1;
        } else { // '-'
          maxFlipForHappy = 1;
          maxFlipForBlank = 0;
        }
      } else {
        int tmpMaxFlipForHappy = maxFlipForHappy;
        int tmpMaxFlipForBlank = maxFlipForBlank;
        if (inputLine[id] == '+') {
          maxFlipForHappy = tmpMaxFlipForHappy;
          maxFlipForBlank = tmpMaxFlipForHappy + 1;
        } else {
          maxFlipForHappy = tmpMaxFlipForBlank + 1;
          maxFlipForBlank = tmpMaxFlipForBlank;
        }
      }
    }

    cout << "Case #" << idTest + 1 << ": " << maxFlipForHappy << endl;
  }

  return 0;
}

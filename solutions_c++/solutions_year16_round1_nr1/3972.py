#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <climits>
#include <map>
#include <sstream>
#include <string>
// www.boost.org
#include <boost/multiprecision/cpp_int.hpp>
#include <boost/utility/binary.hpp>
using namespace std;
using namespace boost::multiprecision;

void findWinningWord(string s) {
  stringstream winningWordStream;
  string winningWord;
  winningWordStream << s[0];
  winningWordStream >> winningWord;

  for (int i = 1; i < s.size(); i++) {
    char topChar = winningWord[0];
    char toAdd = s[i];

    if (toAdd >= topChar) {
      winningWord = toAdd + winningWord;
    } else {
      winningWord += toAdd;
    }
  }

  cout << winningWord;
}

int main() {
  int t;
  scanf("%d\n", &t);

  for (int i = 1; i <= t; i++) {
    string s;
    cin >> s;

    cout << "Case #" << i << ": ";

    findWinningWord(s);

    cout << endl;
  }
}

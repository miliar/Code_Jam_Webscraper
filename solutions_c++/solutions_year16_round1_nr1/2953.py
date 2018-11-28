#include <cstdio>
#include <string>
#include <iostream>
#include <algorithm>

using namespace std;

bool compare (char a, char b) { return a > b; }

main()
{
  int T;
  string str;

  // INPUT
  cin >> T;

  for (int i = 1; i <= T; ++i) {
    string lastWord;
    cin >> str;
    for (string::iterator it = str.begin(); it != str.end(); ++it) {
      if (lastWord.length() == 0)
        lastWord = *it;
      else {
        if (*it >= *(lastWord.begin())) {
          string tmp = *it + lastWord;
          lastWord = tmp;
        }
        else
          lastWord += *it;
      }
    }
    cout << "Case #" << i << ": " << lastWord << endl;
  }
}

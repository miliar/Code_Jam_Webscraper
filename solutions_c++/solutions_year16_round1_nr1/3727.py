#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
  int t;
  string s;
  cin >> t;
  for (int caseN = 1; caseN <= t; caseN++) {
    cin >> s;
    string lastWord;
    lastWord += s[0];
    for (int i = 1; i < s.length(); i++) {
      string front, back;
      front = s[i] + lastWord;
      back = lastWord + s[i];
      lastWord = (front > back) ? front : back;
    }
    cout << "Case #" << caseN << ": " << lastWord << endl;
  }
  return 0;
}

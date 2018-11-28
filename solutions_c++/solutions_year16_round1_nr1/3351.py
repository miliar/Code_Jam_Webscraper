#include <iostream>
#include <list>
using namespace std;


void getTheLastWord(string& origin) {
  list<char> result;
  char maxLetter;
  for (char i : origin) {
    if (i >= result.front()) {
      result.push_front(i);
    } else {
      result.push_back(i);
    };
  }
  for (auto i : result) {
    cout << i;
  }
  cout << endl;
}

int main() {
  int caseNum;
  cin >> caseNum;
  for (int i = 1; i <= caseNum; ++i) {
    string origin;
    cin >> origin;
    cout << "Case #" << i << ": ";
    getTheLastWord(origin);
  }
  return 0;
}
#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cstring>

using namespace std;

int main() {
  int nrCases;
  cin >> nrCases;
  int i = 1;
  while(nrCases --> 0) {
    string str;
    cin >> str;
    int res = -1;
    char last = 'a';
    for(auto &ch : str) {
      res += ch != last;
      last = ch;
    }
    res += last != '+';
    cout << "Case #" << i++ << ": " << res << endl;
  }
  return 0;
}
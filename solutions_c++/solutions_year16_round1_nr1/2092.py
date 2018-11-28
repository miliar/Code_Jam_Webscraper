#include <iostream>
#include <vector>
#include <string>

using std::cin;  using std::cout;  using std::endl;
using std::vector; using std::string;

int main() {

  int T;
  cin >> T;

  // get rid of \n after T
  string s;
  getline(cin,s);

  long N, currentN, cN;

  for (int i=1; i<=T; ++i) {

    string letters, sorted;
    getline(cin, letters);

    // int begin, end;
    // if (letters.size() % 0) {
    //   begin = end = letters.size() / 2;
    // }
    // else {
    //   begin = end = letters.size()
    // }
    // int count = 0;
    sorted = sorted + letters[0];
    for (int j = 1; j< letters.length();  ++j) {
      if (letters[j] >= sorted[0])
	sorted = letters[j] + sorted;
      else
	sorted = sorted + letters[j];
    }
    cout << "case #" << i << ": " << sorted << endl;

  }

  return 0;
}

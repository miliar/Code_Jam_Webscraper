#include <iostream>
#include <vector>
#include <string>

using std::cin;  using std::cout;  using std::endl;
using std::vector; using std::string;

int main() {

  int T;
  cin >> T;

  string s;
  getline(cin,s);

  long N, currentN, cN;

  for (int i=1; i<=T; ++i) {

    string pancakes;
    getline(cin, pancakes);

    int count = 0;
    for (int j = 1; j< pancakes.length();  ++j) {
      if (pancakes[j-1] != pancakes[j])
	++count;
    }
    if (pancakes[pancakes.length()-1] == '-')
      ++count;
    
    cout << "case #" << i << ": " << count << endl;

  }

  return 0;
}

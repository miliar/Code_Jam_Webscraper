#include <iostream>
#include <string>

using namespace std;

int flips = 0;

int Solve(string str) {
  if (str.size() == 1) {
    if (str[0] == '+')
      return 0;
    else
      return 1;
  } else if (str.size() == 2) {
    if (str == "++") {
      return 0;
    } else if (str == "+-") {
      return 2;
    } else if (str == "-+") {
      return 1;
    } else {
      return 1;
    }
  }

  if (str[str.size()-1] == '+') {
    return Solve(str.substr(0, str.size()-1));
  } else {
    if (str[str.size()-2] == '-') {
      return Solve(str.substr(0, str.size()-1));
    } else {
      return 2 + Solve(str.substr(0, str.size()-1));
    }
  }
}

int main()
{
  int T;
  string S;

  cin >> T;

  for (int i = 0; i < T; ++i) {
    cout << "Case #" << i+1 << ": ";
    cin >> S;
    flips = Solve(S);
    cout << flips << endl;
  }

  return 0;
}

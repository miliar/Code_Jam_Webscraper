#include <iostream>
#include <sstream>

using namespace std;

int main() {
  int n;
  cin >> n;
  cin.ignore();

  for (int i = 1; i <= n; i++) {
    string str;
    getline(cin, str);
    istringstream iss(str);

    char c,
         c_curr;
    iss >> c_curr;
    int flips = 0;
    while (iss >> c) {
      if (c == c_curr) ;
      else {
        c_curr = c;
        flips++;
      }
    }
    if (c_curr == '-') flips++;

    cout << "Case #" << i << ": " << flips << endl;
  }

  return 0;
}

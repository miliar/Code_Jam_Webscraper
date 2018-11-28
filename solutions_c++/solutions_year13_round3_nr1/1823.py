#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

bool Con(char c) {
  return !(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u');
}

int Solve(const string& s, int n) {
  int ret = 0;
  for (int i = 0; i < s.size(); ++i) {
    for (int j = 0; j <= i; ++j) {
      //cout << j << "\t" << i << "\t" << s.substr(j, i - j + 1) << endl;
      int c = 0;
      for (int k = j; k <= i; ++k) {
        if (Con(s[k])) ++c;
        else {
          if (c >= n) {
            ++ret;
            c = 0;
            break;
          }
          c = 0;
        }

      }
      if (c >= n) ++ret;
    }
  }

  return ret;
}

int main() {
  ifstream in("A-small-attempt0.in");
  ofstream out("out.txt");

  string s;
  int n;
  int t;
  in >> t;
  for (int i = 1; i <= t; ++i) {
    in >> s >> n;
    out << "Case #" << i << ": " << Solve(s, n) << endl;
  }

  in.close();
  out.close();
  return 0;
}
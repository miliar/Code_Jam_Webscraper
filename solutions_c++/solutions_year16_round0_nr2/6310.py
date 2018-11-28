#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <set>
#include <unordered_set>
#include <stack>
#include <queue>

using namespace std;

char get(bool flip, char c) {
  if (flip) {
    return (c == '-') ? '+' : '-';
  } 
  return c;
}

int go(string &s) {
  const int n = (int) s.size();
  int cnt = 0;
  bool f = false;
  for (int i = n - 1; i >= 0; --i) {
    if (get(f, s[i]) == '-') {
      cnt++;
      f = !f;
    }
  }
  return cnt;
}

void inout_revenge_of_the_pancakes(istream &in, ostream &out) {
 	int t; 
  in >> t;  
  string s;
  for (int c = 1; c <= t; ++c) {
    in >> s;
    out << "Case #" << c << ": ";
    out << go(s) << endl;
  }
}

int main() {
  ifstream in("in.txt");
  ofstream out("out.txt");
  inout_revenge_of_the_pancakes(in, out);
  return 0;
}





#include <iostream>
#include <cstring>
#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <set>
#include <cmath>
#include <map>
#include <cassert>
//#include "windows.h"
using namespace std;

int compute_result(unsigned int n, string t)
{
  int res = 0;
  char c = t.at(0);
  int d = c - 48;
  for (int i = 1; i <= n; i++) {
    char e = t[i];
    int f = e - 48;
    if (f == 0) continue;
    if (d < (i)) {
      unsigned int diff = i - d;
      res += diff;
      d += diff;
      // cout << res << " when i = " << i << endl;
    }
    d += f;
  }
  return res;
}

int main(int argc, char* argv[])
{
  if (argc < 2) exit(1);
  string s;
  ifstream inFile(argv[1], ios::in);
  getline(inFile, s);
  istringstream ss(s);
  size_t count;
  ss >> count;
  for (size_t i = 0; i < count; ++i) {
    getline(inFile, s);
    //unsigned long long a, b;
    string t;
    size_t n;
    ss.clear();
    ss.str(s);
    ss >> n >> t;
    int res = compute_result(n, t);
    cout << "Case #" << (i+1) << ": " << res << '\n';
  }
  return 0;
}

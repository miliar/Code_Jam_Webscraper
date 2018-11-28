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

inline bool is_fair(size_t t)
{
  ostringstream ost;
  ost << t;
  string ss = ost.str();
  const char* s = ost.str().c_str();
  size_t len = ost.str().length();
  size_t lenm1 = len - 1;
  if (len == 1) return true;
  if (len == 2) return (t % 11) == 0;
  size_t max = (len % 2) == 1? (len-3)/2: (len-2)/2;

  for (size_t i = 0; i <= max; ++i)
    if (ss[i] != ss[lenm1-i])
      return false;
  return true;
}

size_t compute_result(size_t a, size_t b)
{
  double db = (double)b;
  size_t max_sq = (size_t)sqrt(db);
  size_t count = 0;
  for (size_t i = max_sq; i >= 1; i--) {
    size_t t = i * i;
    if (t < a) break;
    if (is_fair(i) && is_fair(t)) {
      ++count;
    }
  }
  return count;
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
    size_t a, b;
    ss.clear();
    ss.str(s);
    ss >> a >> b;
    size_t res = compute_result(a, b);
    cout << "Case #" << (i+1) << ": " << res << '\n';
  }
  return 0;
}

#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <cmath>
#include <map>
#include <cassert>

using namespace std;

long double get_result(long double c, long double f, long double x)
{
  long double result = x / 2;
  long double same_term = c / 2;
  //size_t max = (int)x / 2;
  for (size_t i = 1; i <= (int)x; ++i) {
    long double cur= same_term + x / (2.0 + f * i);
    //if (cur > result) return result;
    //else result = cur;
    if (cur < result) result = cur;
    same_term += (c / (2.0 + i*f));
  }
  return result;
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
    long double c, f, x;
    getline(inFile, s);
    ss.clear();
    ss.str(s);
    ss >> c >> f >> x;
    long double res = get_result(c, f, x);
    size_t cnt = (size_t)log10(res);
    cout << "Case #" << (i+1) << ": " << setprecision(8+cnt) << res << '\n';
  }
  return 0;
}



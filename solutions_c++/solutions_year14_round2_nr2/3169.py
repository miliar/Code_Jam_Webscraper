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

size_t A, B,K;

size_t get_result(void)
{
  size_t count = 0;
  for( size_t i = 0; i < A; ++i)
    for (size_t j = 0; j < B; ++j) {
      if ((i & j) < K )
        ++count;
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
    ss.clear();
    ss.str(s);
    ss >> A >> B >> K;
    size_t res = get_result();
    cout << "Case #" << (i+1) << ": " << res << '\n';
  }
  return 0;
}






#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <math.h>
#include <assert.h>
#include <queue>
#include <sstream>
#include <iomanip>
#include <algorithm>

using namespace std;

bool debug=false;

#define DEBUG if (debug) cout

//ostream& operator<<(ostream& o, const Omino& oo) {
//  for (int y=0; y<oo[0].size(); ++y) {
//    for (int x=0; x<oo.size(); ++x) {
//      o << oo[x][y] << " ";
//    }
//    o << endl;
//  }
//
//  return o;
//}

long int N;

string int2string(long int i) 
{
  stringstream s;
  s << i;

  return s.str();
}

long int string2int(const string& s)
{
  assert(s.find("@") == string::npos);

  long int i;
  stringstream ss(s);
  ss >> i;

  assert(int2string(i) == s);

  return i;
}



long int solve()
{
  set<char> nums;

  for (int i=1; nums.size() < 10; ++i) {
    long int NN = i*N;

    string str = int2string(NN);
    for (size_t c=0; c<str.size(); ++c) {
      char cc = str[c];

      nums.insert(cc);
    }

    assert(nums.size() <= 10);

    if (nums.size() == 10) return NN;
  }
  
  assert(false);
  return -1;
}


bool readFile(ifstream& i)
{
  int numCases;
  i >> numCases;

  DEBUG << "  numCases: " << numCases << endl;
  
  for (int c=0; c<numCases; ++c) {
    string NSTR;
    i >> NSTR;
    N = string2int(NSTR);

    assert(int2string(N) == NSTR);

    if (N == 0)
      cout << "Case #" << c+1 << ": INSOMNIA" << endl;
    else {
      long int a = solve();
      cout << "Case #" << c+1 << ": " << a << endl;
    }
  }

  return true;
}



int main(int argv, char* argc[])
{
  if (argv < 2) {
    cout << "Usage " << argc[0] << " <inputFile>" << endl;
    exit(1);
  }

  ifstream filei(argc[1]);

  readFile(filei);

  return 0;
}

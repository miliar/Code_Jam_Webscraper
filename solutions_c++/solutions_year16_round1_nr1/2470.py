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


string solve_(string s)
{
  if (s.empty()) return "";
  
  size_t best = 0;

  for (size_t i=0; i<s.size(); ++i) {
    if (s[i] >= s[best]) {
      best = i;
    }
  }

  string tmp = s.substr(best+1);

  char bla[2]; bla[0] = s[best]; bla[1] = 0;

  return string(bla) + solve_(s.substr(0, best)) + tmp;
}


string solve(string s)
{
  return solve_(s);
}


bool readFile(ifstream& i)
{
  int numCases;
  i >> numCases;

  DEBUG << "  numCases: " << numCases << endl;
  
  for (int c=0; c<numCases; ++c) {
    string NSTR;
    i >> NSTR;

    string a = solve(NSTR);
    cout << "Case #" << c+1 << ": " << a << endl;
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

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
#include <bitset>

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


string int2string(long int i) 
{
  stringstream s;
  s << i;

  return s.str();
}


long int string2int(const string& s, int base=10)
{
  if (base == 10) {
    long int i;
    stringstream ss(s);
    ss >> i;
    
    assert(int2string(i) == s);

    return i;
  }

  return strtol(s.c_str(), NULL, base);
}

int K,C,S;


bool readFile(ifstream& i)
{
  int numCases;
  i >> numCases;

  DEBUG << "  numCases: " << numCases << endl;
  
  for (int c=0; c<numCases; ++c) {
    i >> K;
    i >> C;
    i >> S;

    if (K==S) {
      cout << "Case #" << c+1 << ":";
      long int p = pow(K, C-1);
      for (int n=0; n<K; ++n)
        cout << " " << (long int)(n)*p + 1;
      cout << endl;
    } else {
      cout << "Case #" << c+1 << ": IMPOSSIBLE" << endl;
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

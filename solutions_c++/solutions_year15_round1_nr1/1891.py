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

int numTurns;
vector<int> v;

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

int X, Y;

void solve()
{
  X = Y = 0;
  if (v.empty()) return;

  int minMush = 0;

  for (int i=1; i<v.size(); ++i) {
    if (v[i] < v[i-1])
      minMush += v[i-1] - v[i];
  }
  
  X = minMush;

  int largestDiff=0;

  for (int i=1; i<v.size(); ++i) {
    if (v[i] < v[i-1])
      largestDiff = std::max(v[i-1] - v[i], largestDiff);
  }

  DEBUG << "largestDiff: " << largestDiff << endl;

  int method2=0;

  int totalMushNow = v.front();

  for (int i=1; i<v.size(); ++i) {
    int eat = std::min(largestDiff, totalMushNow);

    method2 += eat;
    
    totalMushNow = v[i];
  }

  Y = method2;
}



bool readFile(ifstream& i)
{
  int numCases;
  i >> numCases;

  DEBUG << "  numCases: " << numCases << endl;
  
  for (int c=0; c<numCases; ++c) {
    i >> numTurns;

    v.clear();

    for (int r=0; r<numTurns; ++r) {
      int b;
      i >> b;
      v.push_back(b);
    }

    DEBUG << "vector: ";
    if (debug) {
      for (int b: v) {
        cout << b << " ";
      }
      cout << endl;
    }

    solve();
    cout << "Case #" << c+1 << ": " << X << " " << Y << endl;
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

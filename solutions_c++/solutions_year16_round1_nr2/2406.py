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

ostream& operator<<(ostream& o, const vector<size_t>& ve)
{
  o << "{";

  for (size_t i: ve) {
    o << " " << i;
  }

  return o << " }";
}

ostream& operator<<(ostream& o, const set<size_t>& ve)
{
  o << "{";

  for (size_t i: ve) {
    o << " " << i;
  }

  return o << " }";
}


ostream& operator<<(ostream& o, const vector<int>& ve)
{
  o << "{";

  for (size_t i: ve) {
    o << " " << i;
  }

  return o << " }";
}


vector<vector<int>> lists;


vector<int> checkFit(const vector<size_t>& rows)
{
  assert(rows.size() == N);

  DEBUG << "checkFit " << rows << endl;

  vector<vector<int>> matrix;
  for (size_t r: rows) {
    matrix.push_back(lists[r]);
  }

  set<size_t> cols;

  for (size_t c = 0; c < lists.size(); ++c) {
    bool isRow=false;
    for (size_t r: rows) {
      if (c==r) { isRow = true; break; }
      if (r > c) break;
    }

    if (isRow) continue;

    assert(c < lists.size());

    for (int cc=0; cc<N; ++cc) {
      if (cols.find(cc) != cols.end()) continue;

      bool match = true;
      for (int r=0; r<N && match; ++r)
        if (matrix[r][cc] != lists[c][r]) 
          match = false;

      if (match) {
        cols.insert(cc);
        break;
      }

      if (lists[c].front() < matrix[0][cc]) return vector<int>();
    }
  }

  if (cols.size() != N-1) return vector<int>();

  DEBUG << "cols: " << cols << endl;

  assert(cols.size() == N-1);

  vector<int> rv;
  int col = -1;
  for (int c=0; c<N; ++c)
    if (cols.find(c) == cols.end()) {
      col = c;
      break;
    }

  assert(col != -1);
  
  for (int r=0; r<N; ++r)
    rv.push_back(matrix[r][col]);
    
  return rv;
}


vector<int> solve_(const vector<size_t>& rows, size_t last)
{
  if (rows.size() == N) {
    return checkFit(rows);
  }

  for (size_t r=last+1; r<lists.size(); ++r) {
    vector<size_t> rows2 = rows;
    rows2.push_back(r);

    vector<int> bla = solve_(rows2, r);
    if (!bla.empty()) return bla;
  }

  return vector<int>();
}


vector<int> solve()
{
  return solve_(vector<size_t>(), -1);
}


bool readFile(ifstream& i)
{
  int numCases;
  i >> numCases;

  DEBUG << "  numCases: " << numCases << endl;
  
  for (int c=0; c<numCases; ++c) {
    i >> N;

    lists.clear();

    for (int q=0; q<2*N-1; ++q) {
      vector<int> l;
      for (int n=0; n<N; ++n) {
        int bla;
        i >> bla;
        l.push_back(bla);
      }
      lists.push_back(l);
    }

    sort(lists.begin(), lists.end());
    
    for (const vector<int>& l: lists) {
      DEBUG << l << endl;
    }


    vector<int> missingList = solve();
    cout << "Case #" << c+1 << ":";
    for (int a: missingList)
      cout << " " << a;
    cout << endl;
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

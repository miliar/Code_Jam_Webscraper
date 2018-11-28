// #include <assert.h>

#include <algorithm>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>
//#include <unordered_map>
#include <vector>

using namespace std;

#define FOR(i, n) for (int i = 0; i < n; ++i)
#define FOR_(i, n) for (int i = n - 1; i >= 0; --i)

string IsPossible(const vector<vector<int> > & lawn, int N, int M) {
  int min_ = 100000;
  int max_ = -100;
  for (int i = 0; i < N; ++i)
    for (int j = 0; j < M; ++j) {
      if (lawn[i][j] < min_)
        min_ = lawn[i][j] ;
      if (lawn[i][j] > max_)
        max_ = lawn[i][j] ;
    }

  string yes = "YES";
  string no = "NO";
  if (min_ < 1)
    return no;
  if (max_ > 100)
    return no;
  vector<int> vertical_height;
  for (int i = 0; i < N; ++i) {
    int mn = -100;
    for (int j = 0; j < M; ++j)
      if (lawn[i][j] > mn)
        mn = lawn[i][j];
    vertical_height.push_back(mn);
  }

  vector<int> horizontal_height;
  for (int i = 0; i < M; ++i) {
    int mn = -100;
    for (int j = 0; j < N; ++j)
      if (lawn[j][i] > mn)
        mn = lawn[j][i];
    horizontal_height.push_back(mn);
  }

  // Apply the smallest heights;
  vector<int> row(M, 100);
  vector<vector<int> > mowed_lawn(N, row);
  for (int i = 0; i < N; ++i)
    for (int j = 0; j < M; ++j)
      mowed_lawn[i][j] = vertical_height[i];
  for (int i = 0; i < N; ++i)
    for (int j = 0; j < M; ++j)
      mowed_lawn[i][j] = min(mowed_lawn[i][j], horizontal_height[j]);

  // Check if we satisfied the pattern.
  bool b = true;
  for (int i = 0; i < N; ++i)
    for (int j = 0; j < M; ++j)
      if (lawn[i][j] != mowed_lawn[i][j])
        b = false;

  if (b == true)
    return yes;
  return no;
}

int main () {
  ifstream in_("B-large.in");
  ofstream out_("out");
  int T;
  in_ >> T;
  vector<vector<vector<int> > > lawns;
  vector<pair<int, int> > sizes;
  in_.ignore();
  vector<vector<int> > dummy;
  lawns.push_back(dummy);
  sizes.push_back(make_pair(-1, -1));
  int temp;
  for (int count = 1; count <= T; ++count) {
    int N, M;
    in_ >> N >> M;
    sizes.push_back(make_pair(N, M));
    vector<vector<int> > v;
    for (int i = 0; i < N; ++i) {
      vector<int> w;
      for (int j = 0; j < M; ++j) {
        in_ >> temp;
        w.push_back(temp);
      }
      v.push_back(w);
    }
    lawns.push_back(v);
  } // End of input.



  vector<string> output;
  output.push_back("");
  for (int count = 1; count <= T; ++count) {
    int N, M;
    N = sizes[count].first;
    M = sizes[count].second;
    output.push_back(IsPossible(lawns[count], N, M));
  }

  for (int i = 1; i <= T; ++i) {
    stringstream ss;
    ss << i;
    string s1("Case #");
    string s2;
    ss >> s2;
    string s3(": ");

    output[i] = s1 + s2 + s3 + output[i];
  }

  for (int i = 1; i <= T; ++i) {
    out_ << output[i] << endl;
  }
  in_.close();
  out_.close();

  return 0;
}

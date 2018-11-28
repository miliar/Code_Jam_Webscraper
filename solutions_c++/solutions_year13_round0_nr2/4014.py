#include <iostream>
#include <map>
#include <vector>
#include <list>
#include <algorithm>
#include <numeric>
#include <string>
using namespace std;

void printMap(const vector<vector<int> >& m) {
  for (unsigned i = 0; i < m.size(); i++) {
    for (unsigned j = 0; j < m[0].size(); j++) 
      cout << m[i][j] << " ";
    cout << endl;
  }
}

bool checkHeight(const vector<int>& vec, int height) {
  for (unsigned i = 0; i < vec.size(); i++)
    if (vec[i] > height) return false;
  return true;
}

void cutMap(const vector<vector<int> >& target,
	    vector<vector<int> >& current, int height) {
  // check row
  for (unsigned i = 0; i < target.size(); i++)
    if (checkHeight(target[i], height))
      fill(current[i].begin(), current[i].end(), height);
  // check col
  for (unsigned i = 0; i < target[0].size(); i++) {
    vector<int> tmp(target.size(), -1);
    for (unsigned j = 0; j < target.size(); j++)
      tmp[j] = target[j][i];
    if (checkHeight(tmp, height))
      for (unsigned j = 0; j < target.size(); j++)
	current[j][i] = height;
  }
}


bool checkMap(const vector<vector<int> > &l) {
  vector<vector<int> > ll;
  ll.reserve(l.size());
  for (unsigned i = 0; i < l.size(); i++) {
    vector<int> tmp(l[0].size(), 101);
    ll.push_back(tmp);
  }
  for (int h = 100; h > 0; h--) {
    cutMap(l, ll, h);
  }
  for (unsigned i = 0; i < l.size(); i++)
    for (unsigned j = 0; j < l[0].size(); j++)
      if (ll[i][j] != l[i][j]) return false;
  return true;
}

int main() 
{
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
      int n, m;
      cin >> n >> m;
      vector<vector<int> > lawn;
      lawn.reserve(n);
      for (int i = 0; i < n; i++) {
	vector<int> tmp(m, 0);
	for (int j = 0; j < m; j++)
	  cin >> tmp[j];
	lawn.push_back(tmp);
      }
      cout << "Case #" << t << ": ";
      if (checkMap(lawn)) cout << "YES" << endl;
      else cout << "NO" << endl;
    }
    return 0;    
}

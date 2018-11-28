#include <cmath>
#include <iostream>
#include <map>
#include <set>
#include <stdexcept>
#include <vector>

using namespace std;

struct Fragment {
  char ch;
  int len;
};

void compute(const string& str, vector<Fragment> * const res) {
  int currsize = 0;
  int i;
  for (i = 0; i + 1 < str.size(); ++i) {
    ++currsize;
    if (str[i] != str[i + 1]) {
      res->push_back(Fragment());
      res->back().ch = str[i];
      res->back().len = currsize;
      currsize = 0;
    }
  }
  ++currsize;
      res->push_back(Fragment());
      res->back().ch = str[i];
      res->back().len = currsize;
}

bool consistent(const vector<Fragment>& left, const vector<Fragment>& right) {
  if (left.size() != right.size()) {return false;}
  
  for (int i = 0; i < left.size(); ++i) {
    if (left.at(i).ch != right.at(i).ch) {
      return false;
    }
  }
  return true;
}

int main() {
  int ncases;
  cin >> ncases;
  
  for (int c = 0; c < ncases; ++c) {
    cout << "Case #" << c + 1 << ": ";
    
    int nstr;
    cin >> nstr;
    
    string str[nstr];
    vector<vector<Fragment> > frags;
    for (int i = 0; i < nstr; ++i) {
      cin >> str[i];
      frags.push_back(vector<Fragment>());
      compute(str[i], &frags[i]);
    }
    bool fail = false;
    for (int i = 1; i < nstr; ++i) {
      if (!consistent(frags.at(i), frags.at(0))) {
        fail = true;
        break;
      }
    }
    if (fail) {
      cout << "Fegla Won" << endl;
      continue;
    }
    double minops = 0.0;
    for (int i = 0; i < frags.at(0).size(); ++i) {
      double meanlen = 0.0;
      for (int j = 0; j < nstr; ++j) {
        meanlen += frags.at(j).at(i).len;
        //cout << str[j] << " " << frags.at(j).at(i).ch << " " << frags.at(j).at(i).len << endl;
      }
      meanlen /= nstr;
      meanlen = round(meanlen);
      //cout << "meanlen " << meanlen << endl;
      
      for (int j = 0; j < nstr; ++j) {
        minops += fabs( frags.at(j).at(i).len - meanlen );
      }
    }
    minops = round(minops);
    cout << minops << endl;
  }
  return 0;
}


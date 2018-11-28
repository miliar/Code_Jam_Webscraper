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

bool traverse (string str, int n) {
  int count = 0;
  set<char> vowels = {'a', 'e', 'i', 'o', 'u'};
  for (int i = 0; i < str.size(); ++i) {
    if (vowels.find(str[i]) == vowels.end())
      ++count;
    else
      count = 0;
    if (count == n)
        return true;
  }
  return false;

}


int main () {
  ifstream in_("A-small-attempt0.in");
  ofstream out_("out");
  int T;
  in_ >> T;
  string s;
  int n;
  vector<string> output;
  output.push_back("dsfd");
  for (int i = 1; i <= T; ++i) {
    in_ >> s;
    in_ >> n;
    vector<string> substr;
    for (int j = 0; j < s.size(); ++j)
      for (int k = j; k < s.size(); ++k)
        if (k - j >= n - 1)
          substr.push_back(s.substr(j, k - j + 1));
    int count = 0;
    for (int j = 0; j < substr.size(); ++j)
      if (traverse(substr[j], n) == true)
        ++count;
    output.push_back(to_string(count));
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

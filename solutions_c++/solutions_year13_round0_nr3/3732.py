#include <assert.h>

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

#define FOR(i, n) for (long long i = 0; i < n; ++i)
#define FOR_(i, n) for (long long i = n - 1; i >= 0; --i)

long long Palindroms(long long A, long long B) {
  double d = sqrt(B);
  long long upper = (long long)d + 1;
  d = sqrt(A);
  long long lower = max((long long)1, (long long)d - 1);
  long long count = 0;
  string s;
  for (long long i = lower; i <= upper; ++i) {
    s = to_string(i);
    string s2(s.rbegin(), s.rend());
    if (s == s2) {
      if (i*i >= A && i*i <= B) {
        s = to_string(i*i);
        s2 = string(s.rbegin(), s.rend());
        if (s == s2)
          ++count;
      }
    }
  }
  return count;
}


int main () {
  ifstream in_("C-small-attempt1.in");
  ofstream out_("out");
  long long T;
  in_ >> T;
  vector<pair<long long, long long> > range;
  long long A, B;
  range.push_back(make_pair(-1, -1));
  for (long long i = 1; i <= T; ++i) {
    in_ >> A >> B;
    range.push_back(make_pair(A, B));
  }
  // End of input.

  vector<string> v;
  v.push_back("");
  for (long long i = 1; i <= T; ++i)
    v.push_back(to_string(Palindroms(range[i].first, range[i].second)));

  // output
  for (long long i = 1; i <=T; ++i) {
    stringstream ss;
    ss << i;
    string s1("Case #");
    string s2;
    ss >> s2;
    string s3(": ");

    v[i] = s1 + s2 + s3 + v[i];
  }

  for (int i = 1; i <= T; ++i) {
    out_ << v[i] << endl;
  }
  in_.close();
  out_.close();

  return 0;
}

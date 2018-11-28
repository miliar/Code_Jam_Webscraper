
#include <iostream>
#include <cstring>
#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <set>
#include <cmath>
#include <map>
#include <cassert>
//#include "windows.h"
using namespace std;

bool is_vowel(char c)
{
  return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

set<pair<size_t, size_t> > all_pairs;

size_t can_contain(size_t index, size_t total_len, size_t sub_len)
{
  size_t a = index + 1;
  size_t b = total_len - 1 - (index + sub_len - 1) + 1;
  size_t count = 0;
  for (size_t i = 0; i < a; ++i) {
    for (size_t j = index + sub_len - 1; j < total_len; ++j) {
      pair<size_t, size_t> p(i, j);
      if (all_pairs.find(p) == all_pairs.end()) {
        ++count;
        all_pairs.insert(p);
      }
    }
  }
  //cout << "a*b=" << a*b << '\n';
  return count;
  //return a * b;
}

int compute_result(size_t n, string s)
{
  int count = 0;
  size_t len = s.length();

  vector<size_t> all_match;

  for (size_t i = 0; i <= len - n; ++i) {
    string t = s.substr(i, n);
    //cout << "testing t = " << t << '\n';
    bool not_meet = false;
    for (size_t j = 0; j < n; ++j) {
      if (is_vowel(t[j])) {
        not_meet = true;
        break;
      }
    }
    if (!not_meet) {
      size_t addend = can_contain(i, len, n);
      //cout << "substring t " << t << " match! i = " << i << " addend="
        //<< addend << "\n";
      count += addend;
#if 0
      for (size_t k = 0; k < all_match.size(); ++k) {
        // pair: i, all_match[k]
        size_t tmp_start = i < all_match[k]? i: all_match[k];
        size_t tmp_end = i > all_match[k]? i: all_match[k];
        tmp_end += (n-1);
        size_t tmp_len = tmp_end - tmp_start + 1;
        /*
        cout << "tmp_start = " << tmp_start << '\n';
        cout << "tmp_end = " << tmp_end << '\n';
        cout << "tmp_len = " << tmp_len << '\n';
        cout << "len = " << len << '\n';
        */
        size_t substract = can_contain(tmp_start, len, tmp_len);
        cout << "substract = " << substract << '\n';
        count -= substract;
      }
#endif
      all_match.push_back(i);
    }
  }

  return count;
}

int main(int argc, char* argv[])
{
  if (argc < 2) exit(1);
  string s;
  ifstream inFile(argv[1], ios::in);
  getline(inFile, s);
  istringstream ss(s);
  size_t count;
  ss >> count;
  for (size_t i = 0; i < count; ++i) {
    all_pairs.clear();
    getline(inFile, s);
    //unsigned long long a, b;
    string t;
    size_t n;
    ss.clear();
    ss.str(s);
    ss >> t >> n;
    int res = compute_result(n, t);
    cout << "Case #" << (i+1) << ": " << res << '\n';
  }
  return 0;
}

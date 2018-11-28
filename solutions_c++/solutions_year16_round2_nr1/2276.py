#include <cassert>
#include <cstdio>
#include <cstdlib>

#include <algorithm>
#include <array>
#include <bitset>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <regex>
#include <set>
#include <string>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;

string Solve(string s) {
  unordered_map<char, int> let;
  for (char c : s) {
    ++let[c];
  }

  string ret = "";

  auto uniq = [&](char ch, char dig, string word) {
    auto n = let[ch];
    ret += string(n, dig);
    for (char c : word)
      let[c] -= n;
  };

  uniq('Z', '0', "ZERO");
  uniq('W', '2', "TWO");
  uniq('U', '4', "FOUR");
  uniq('X', '6', "SIX");

  uniq('S', '7', "SEVEN");
  uniq('O', '1', "ONE");
  uniq('R', '3', "THREE");
  uniq('H', '8', "EIGHT");
  uniq('V', '5', "FIVE");
  uniq('I', '9', "NINE");

  sort(ret.begin(), ret.end());
  return ret;
}

int main() {
  int t;
  scanf("%d", &t);
  for (int tc = 0; tc < t; ++tc) {
    char s[2005];
    scanf("%s", s);
    printf("Case #%d: %s\n", tc + 1, Solve(s).c_str());
  }
  return 0;
}

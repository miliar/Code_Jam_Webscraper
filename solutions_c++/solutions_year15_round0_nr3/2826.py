#include <algorithm>
#include <cassert>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <sstream>
#include <unordered_map>
#include <vector>


#define INF 1000000000
#define MOD 1000000007
#define ALL(x) std::begin(x), std::end(x)


std::map<std::string, std::string> fexp = {
  {"11",  "1"},
  {"1i",  "i"},
  {"1j",  "j"},
  {"1k",  "k"},

  {"i1",  "i"},
  {"ii", "-1"},
  {"ij",  "k"},
  {"ik", "-j"},

  {"j1",  "j"},
  {"ji", "-k"},
  {"jj", "-1"},
  {"jk",  "i"},

  {"k1",  "k"},
  {"ki",  "j"},
  {"kj", "-i"},
  {"kk", "-1"}
};

std::map<std::string, std::string> rexp = {
  {"11",  "1"},
  {"1i",  "i"},
  {"1j",  "j"},
  {"1k",  "k"},

  {"ii",  "1"},
  {"i1", "-i"},
  {"ik",  "j"},
  {"ij", "-k"},

  {"jj",  "1"},
  {"jk", "-i"},
  {"j1", "-j"},
  {"ji",  "k"},

  {"kk",  "1"},
  {"kj",  "i"},
  {"ki", "-j"},
  {"k1", "-k"}
};


std::string mul(const std::string& a, const std::string& b)
{
  if (a[0] != '-' && b[0] != '-') {
    return a + b;
  }
  else if (a[0] == '-' && b[0] != '-') {
    return a + b;
  }
  else if (a[0] != '-' && b[0] == '-') {
    return "-" + a + b.substr(1);
  }
  else {
    return a.substr(1) + b.substr(1);
  }
}


bool solve()
{
  long long X, L, n;

  std::string s;

  std::cin >> L >> X >> s;

  std::map<char, long long> map;
  
  for (const auto& c : s)
    map[c] ++;

  if (map.size() == 1)
    return false;

  std::cerr << "L=" << L << " X=" << X << " s=" << s << std::endl;

  std::string S;

  for (int i = 0; i < X; i ++)
    S += s;

  int size = S.size();

  if (size < 3)
    return false;

  std::vector<std::string> table1(size), table2(size);

  std::set<int> ii, kk;

  if ((table1[0] = S[0]) == "i")
    ii.insert(0);

  for (int i = 1; i < size; i ++)
    if ((table1[i] = fexp[mul(table1[i - 1], std::string(1, S[i]))]).back() == 'i')
      ii.insert(i);

  if ((table2[size - 1] = S[size - 1]) == "k")
    kk.insert(size - 1);

  for (int i = size - 1; i > 0; i --)
    if ((table2[i - 1] = fexp[mul(std::string(1, S[i - 1]), table2[i])]).back() == 'k')
      kk.insert(i - 1);
  
  for (const auto& i : ii)
    for (const auto& k : kk)
      if (i < k) {
        std::string target("j");

        if (table1[i][0] == '-' && table2[k][0] == '-') {
          ;
        }
        else if (table1[i][0] == '-') {
          target = "-j";
        }
        else if (table2[k][0] == '-') {
          target = "-j";
        }
        else {
          ;
        }

        if (rexp[mul(table1[i], table1[k - 1])] == target)
          return true;
      }
  
  return false;
}


int main(int argc, char** argv)
{
  std::cin.tie(0);
  std::ios_base::sync_with_stdio(0);

  std::vector<std::string> keys;

  for (const auto& key : fexp)
    keys.push_back(key.first);

  for (const auto& key : keys)
    if (fexp[key][0] == '-') {
      fexp["-" + key] = fexp[key].substr(1);
    }
    else {
      fexp["-" + key] = "-" + fexp[key];
    }

  keys.clear();

  for (const auto& key : rexp)
    keys.push_back(key.first);

  for (const auto& key : keys)
    if (rexp[key][0] == '-') {
      rexp["-" + key] = rexp[key].substr(1);
    }
    else {
      rexp["-" + key] = "-" + rexp[key];
    }


  int T;

  std::string s;

  std::cin >> T;

  for (int t = 1; t <= T; t ++) {
    bool r = solve();

    std::cout << "Case #" << t << ": " << (r ? "YES" : "NO") << std::endl;
  }

  return 0;
}

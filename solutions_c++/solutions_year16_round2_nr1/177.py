#include <iostream>
#include <cassert>
#include <string>
#include <map>
#include <vector>

using namespace std;

void solve(int test) {
  string str;
  cin >> str;
  vector<int> res;
  map<char, int> cnt;
  for (auto x : str) {
    cnt[x]++;
  }
  //1345789
  while (cnt['Z'] > 0) {
    res.push_back(0);
    cnt['Z']--;
    cnt['E']--;
    cnt['R']--;
    cnt['O']--;
  }
  //SIX
  while (cnt['X'] > 0) {
    res.push_back(6);
    cnt['S']--;
    cnt['I']--;
    cnt['X']--;
  }       
  //TWO
  while (cnt['W'] > 0) {
    res.push_back(2);
    cnt['T']--;
    cnt['W']--;
    cnt['O']--;
  }
  //FOUR
  while (cnt['U'] > 0) {
    res.push_back(4);
    cnt['F']--;
    cnt['O']--;
    cnt['U']--;
    cnt['R']--;
  }

  while (cnt['F'] > 0) {
    res.push_back(5);
    cnt['F']--;
    cnt['I']--;
    cnt['V']--;
    cnt['E']--;
  }
  while (cnt['G'] > 0) {
    res.push_back(8);
    cnt['E']--;
    cnt['I']--;
    cnt['G']--;
    cnt['H']--;
    cnt['T']--;
  }
  while (cnt['T'] > 0) {
    res.push_back(3);
    cnt['T']--;
    cnt['H']--;
    cnt['R']--;
    cnt['E']--;
    cnt['E']--;
  }
  while (cnt['O'] > 0) {
    res.push_back(1);
    cnt['O']--;
    cnt['N']--;
    cnt['E']--;
  }
  while (cnt['S'] > 0) {
    res.push_back(7);
    cnt['S']--;
    cnt['E']--;
    cnt['V']--;
    cnt['E']--;
    cnt['N']--;
  }
  while (cnt['N'] > 0) {
    res.push_back(9);
    cnt['N']--;
    cnt['I']--;
    cnt['N']--;
    cnt['E']--;
  }
  for (auto x : cnt) {
    assert(x.second == 0);
  }
  sort(begin(res), end(res));
  printf("Case #%d: ", test);
  for (auto x : res) {
    printf("%d", x);
  }
  printf("\n");
}

int main() {
  int T;
  cin >> T;
  for (int test = 1; test <= T; test++) {
    solve(test);
  }
}

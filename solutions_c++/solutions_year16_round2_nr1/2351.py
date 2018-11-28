#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

void solve() {
  string S;
  cin >> S;
  int table[32] = {0};
  vector<int> ans;
  for (int i = 0; i < S.size(); ++i) {
    ++table[S[i] - 'A'];
  }
  for (int i = S.size() - 1; 0 <= i; --i) {
    if (S[i] == 'Z') {
      --table['Z' - 'A'];
      --table['E' - 'A'];
      --table['R' - 'A'];
      --table['O' - 'A'];
      S.replace(i, 1, "");
      ans.push_back(0);
    } else if(S[i] == 'W') {
      --table['T' - 'A'];
      --table['W' - 'A'];
      --table['O' - 'A'];
      S.replace(i, 1, "");
      ans.push_back(2);
    } else if(S[i] == 'U') {
      --table['F' - 'A'];
      --table['O' - 'A'];
      --table['U' - 'A'];
      --table['R' - 'A'];
      S.replace(i, 1, "");
      ans.push_back(4);
    } else if(S[i] == 'X') {
      --table['S' - 'A'];
      --table['I' - 'A'];
      --table['X' - 'A'];
      S.replace(i, 1, "");
      ans.push_back(6);
    } else if(S[i] == 'G') {
      --table['E' - 'A'];
      --table['I' - 'A'];
      --table['G' - 'A'];
      --table['H' - 'A'];
      --table['T' - 'A'];
      S.replace(i, 1, "");
      ans.push_back(8);
    }
  }
  for (int i = S.size() - 1; 0 <= i; --i) {
    if (S[i] == 'O' && table['O' - 'A'] > 0) {
      --table['O' - 'A'];
      --table['N' - 'A'];
      --table['E' - 'A'];
      S.replace(i, 1, "");
      ans.push_back(1);
    } else if(S[i] == 'T' && table['T' - 'A'] > 0){
      --table['T' - 'A'];
      --table['H' - 'A'];
      --table['R' - 'A'];
      --table['E' - 'A'];
      --table['E' - 'A'];
      S.replace(i, 1, "");
      ans.push_back(3);
    } else if(S[i] == 'F' && table['F' - 'A'] > 0){
      --table['F' - 'A'];
      --table['I' - 'A'];
      --table['V' - 'A'];
      --table['E' - 'A'];
      S.replace(i, 1, "");
      ans.push_back(5);
    } else if(S[i] == 'S' && table['S' - 'A'] > 0){
      --table['S' - 'A'];
      --table['E' - 'A'];
      --table['V' - 'A'];
      --table['E' - 'A'];
      --table['N' - 'A'];
      S.replace(i, 1, "");
      ans.push_back(7);
    } 
  }
  for (int i = S.size() - 1; 0 <= i; --i) {
    if (S[i] == 'I' && table['I' - 'A'] > 0) {
      --table['N' - 'A'];
      --table['I' - 'A'];
      --table['N' - 'A'];
      --table['E' - 'A'];
      S.replace(i, 1, "");
      ans.push_back(9);
    }
  }
  sort(ans.begin(), ans.end());
  for (int i = 0; i < ans.size(); ++i) {
    cout << ans[i];
  }
  cout << endl;
}

int main() {
  int T;
  cin >> T;
  for (int i = 0; i < T; ++i) {
    printf("Case #%d: ", i + 1);
    solve();  
  }
  return 0;
}

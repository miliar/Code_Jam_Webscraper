#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <math.h>
using namespace std;

vector<int> memo;

bool palindrome(char *ch, int i) {
  string s, s2;
  sprintf(ch, "%d", i); // int i を char ch に変換
  s = ch; // char ch を string s に変換
  s2 = ch;
  reverse(s2.begin(), s2.end());
  if (s == s2) return true;
  else return false;
}

int search(int a, int b) { // memoの中のaからbまでの要素数を求める
  int c = 0; // counter
  int len = memo.size();
  int i = 0;
  while(i <= len - 1 && memo.at(i) <= b) {
    if (a <= memo.at(i)) c++;
    i++;
  }
  return c;
}

int solve(int a, int b) {
  int ans = 0;
  char ch[1000];
  if (memo.empty()) { // memoを作る
    for (int i = 1; i <= 1000; i++) {
      if (palindrome(ch, i) && palindrome(ch, i*i)) memo.push_back(i*i);
    }
  }
  return search(a, b);

}

int main () {
  int t;
  cin >> t;
  for (int i = 1; i <= t; i++) {
    int a, b, ans;
    cin >> a >> b;
    ans = solve(a, b);
    printf("Case #%d: %d\n", i, ans);
  }
  return 0;
}

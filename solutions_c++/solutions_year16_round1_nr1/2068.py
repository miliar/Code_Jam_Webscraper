#include <stdio.h>
#include <string.h>
#include <iostream>
#include <vector>
using namespace std;

string Work(int from, int to, string &s, vector< vector<string> >& temp) {
  if (temp[from][to].length() != 0) {
     return temp[from][to];
  }
  if (from == to) {
    temp[from][to] += s[from];
    return temp[from][to];
  }
  char max_char = s[from];
  for (int i = from; i <= to; i++) {
    if (max_char < s[i]) { max_char = s[i]; }
  }
  for (int i = from; i <= to; i++)
  if (s[i] == max_char) {
    string ans = "";
    ans += s[i];
    if (i > from) { ans += Work(from, i - 1, s, temp); }
    if (i < to) { ans += s.substr(i + 1, to - i); }
    if (temp[from][to] < ans) {
        temp[from][to] = ans;
    }
  }
   return temp[from][to];
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int test;
    scanf("%d", &test);
    for (int t = 1; t <= test; t++) {
        string s;
        cin >> s;
        int n = s.length();
        vector< vector<string> > temp(n, vector<string>(n, ""));
        printf("Case #%d: ", t);
        cout << Work(0, n - 1, s, temp) << endl;
    }
    return 0;
}

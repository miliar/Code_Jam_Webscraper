#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

string a[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

int ct[10][26], tot[26], t;
string s;
int ans[10];

void del(int x) {
  ans[x]++;
  for (int i = 0; i < 26; ++i)
    tot[i] -= ct[x][i];
}

void work(string s, int q) {
  memset(ans, 0, sizeof(ans));
  memset(tot, 0, sizeof(tot));
  
  for (int i = 0; i < s.length(); ++i)
    tot[s[i] - 'A']++;

  while (tot[25] > 0)
    del(0);
  while (tot['W'-'A'] > 0)
    del(2);
  while(tot['X'-'A'] > 0)
    del(6);
  while(tot['G'-'A'] > 0)
    del(8);
  while(tot['U'-'A'] > 0)
    del(4);
  while(tot['F'-'A'] > 0)
    del(5);
  while(tot['V'-'A'] > 0)
    del(7);
  while(tot['O'-'A'] > 0)
    del(1);
  while(tot['T'-'A'] > 0)
    del(3);
  while(tot['N'-'A'] > 0)
    del(9);
  
  cout << "Case #" << q << ": ";
  for (int i = 0; i < 10; ++i)
    for (int j = 0; j < ans[i]; ++j)
      cout << i;
  cout << "\n";
}

int main() {
  ifstream cin("input.in");
  cin >> t;
  
  for (int i = 0; i < 10; ++i)
    for (int j = 0; j < a[i].length(); ++j)
      ct[i][a[i][j] - 'A']++;

  for (int i = 0; i < t; ++i) {
    cin >> s; work(s, i+1);
  }
}

#include <iostream>
#include <cstring>
using namespace std;

int freq[26];
int cnt[10];

string nums[] = {"ZERO", "ONE", "WTO",
		 "THREE", "RFOU", "FIVE",
		 "XSI", "SEVEN", "GEIHT", "INNE"};
int ord[] = {0, 2, 6, 8, 3, 4, 1, 5, 7, 9};

char ret[2001];

void find(int i) {
  cnt[i] = freq[nums[i][0] - 'A'];
  for (char& ch: nums[i]) freq[ch - 'A'] -= cnt[i];
}
string s;
void solve() {
  memset(freq, 0, sizeof(freq));
  memset(cnt, 0, sizeof(cnt));
  for (char& ch: s) freq[ch - 'A']++;

  for (int i = 0; i < 10; i++) find(ord[i]);
  int l = 0;
  for (int i = 0; i < 10; i++) {
    while (cnt[i]--) ret[l++] = '0' + i;
  }
  ret[l] = 0;
}

void verify() {
  bool corr = 1;
  memset(freq, 0, sizeof(freq));
  for (char& ch: s) freq[ch -'A']++;
  for (int i = 0; ret[i]; i++) {
    int j = ret[i] - '0';
    for (char& ch: nums[j]) freq[ch - 'A']--;
  }
  for (int i = 0; i < 26; i++) if (freq[i] != 0) corr = 0;
  if (!corr) cerr << "Failed: " << s << ": " << ret << endl;
}

int main() {
  int t; cin >> t;
  for (int i = 1; i <= t; i++) {
    cin >> s;
    solve();
    verify();
    cout << "Case #" << i << ": " << ret << '\n';
  }
  return 0;
}

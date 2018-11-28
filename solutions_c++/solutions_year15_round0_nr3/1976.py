#include<bits/stdc++.h>
using namespace std;
#define S second
#define C first

typedef long long ll;
typedef pair<char, int> pp;

pp mul(pp a, pp b) {
  char c = 0;
  int s = 0;
  if(a.C == '1') {c = b.C; s = +1;}
  else if(b.C == '1') {c = a.C; s = +1;}
  else if(a.C == b.C) {c = '1'; s = -1;}
  if(a.C == 'i' && b.C == 'j') {c = 'k'; s = +1;}
  if(a.C == 'j' && b.C == 'k') {c = 'i'; s = +1;}
  if(a.C == 'k' && b.C == 'i') {c = 'j'; s = +1;}
  if(a.C == 'j' && b.C == 'i') {c = 'k'; s = -1;}
  if(a.C == 'k' && b.C == 'j') {c = 'i'; s = -1;}
  if(a.C == 'i' && b.C == 'k') {c = 'j'; s = -1;}
  if(s == 0 || c == 0) {
    cout << a.C << " " << b.C << "\n";
    throw;
  }
  s *= (a.S * b.S);
  return pp(c, s);
}

bool go() {
  const pp ONE = pp('1', +1);

  ll l, x;
  cin >> l >> x;
  string s;
  cin >> s;
  pp subSum = ONE;
  for(char c : s) {
    subSum = mul(subSum, pp(c, +1)); 
  }
  pp totSum = ONE;
  for(int i = 0; i < x; ++i) {
    totSum = mul(totSum, subSum);
  }
  if(totSum != pp('1', -1)) return false;

  string sOrig = s;
  for(int i = 1; i < max(x, 10ll); ++i) {
    s += sOrig;
  }

  pp lSum = ONE;
  int lIdx = 0;
  while(true) {
    if(lIdx >= s.size()) return false;
    lSum = mul(lSum, pp(s[lIdx], +1));
    if(lSum == pp('i', +1)) break;
    ++lIdx;
  }

  pp rSum = ONE;
  int rIdx = s.size() - 1;
  while(true) {
    if(rIdx < 0) return false;
    rSum = mul(pp(s[rIdx], +1), rSum);
    if(rSum == pp('k', +1)) break;
    --rIdx;
  } 
  rIdx = (s.size() - rIdx);
  lIdx = (lIdx + 1);
  return (lIdx + rIdx <= l * x);
}

int main() {
  int t;
  cin >> t;
  for(int i = 0; i < t; ++i) {
    printf("Case #%d: %s\n", i + 1, go() ? "YES" : "NO");
  }
}

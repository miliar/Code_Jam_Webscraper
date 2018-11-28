#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<ll, pair<string, string> > pii;

#define A first
#define B second

int t;
string s1, s2;
pii ans;

ll conv(string g) {
  ll ans = 0;
  for (int i = 0; i < g.length(); ++i)
    ans = 10*ans+g[i]-'0';
  return ans;
}

ll chk(string a, string b) {
  // cout << a << ' ' << b << endl;
  int ind = -1;
  bool y = 0;
  for (int i = 0; i < a.length(); ++i) {
    if (a[i] > b[i]) {
      ind = i+1, y = 0; break;
    }
    if (a[i] < b[i]) {
      ind = i+1, y = 1; break;
    }
  }

  if (ind != -1) {
    for (int i = ind; i < a.length(); ++i) {
      if (y == 0) {
	if (a[i] == '?')
	  a[i] = '0';
	if (b[i] == '?')
	  b[i] = '9';
      } else {
	if (a[i] == '?')
	  a[i] = '9';
	if (b[i] == '?')
	  b[i] = '0';
      }
    }
  }
  
  //  cout << a << ' ' << b << ' ' << ind << endl;
  ll a1 = conv(a), b1 = conv(b);
  ans = min(ans, pii(labs(a1-b1), make_pair(a, b)));
}

ll work(int q) {
  cout << "Case #" << q << ": ";
  ans = pii(1000000000000000000LL, make_pair("", ""));
  string g1 = s1, g2 = s2;
  for (int i = 0; i < s1.length(); ++i) {
     for (int j = 0; j < 10; ++j)
       for (int k = 0; k < 10; ++k) {
	   if (s1[i] != '?' && s1[i] != j+'0')
	     continue;
	   if (s2[i] != '?' && s2[i] != k+'0')
	     continue;
	   if (j == k)
	     continue;
	   g1[i] = j+'0', g2[i] = k+'0';
	   chk(g1, g2);
	  }

     if (s1[i] != '?' && s2[i] != '?') {
       if (s1[i] != s2[i])
	 break;
       continue;
     }
     
     if (s1[i] == '?' && s2[i] == '?') {
       g1[i] = '0', g2[i] = '0'; continue;
     }

     if (s1[i] != '?') {
       g2[i] = g1[i]; continue;
     }

     if (s2[i] != '?') {
       g1[i] = g2[i]; continue;
     }
  }

  chk(g1, g2);

  cout << ans.B.A << ' ' << ans.B.B << "\n";
}

int main() {
  ifstream cin("input.in");
  cin >> t;
  
  for (int i = 0; i < t; ++i) {
    cin >> s1 >> s2;
    work(i+1);
  }
}

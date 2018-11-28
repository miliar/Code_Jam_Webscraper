#include <bits/stdc++.h>

#define DEBUG

#ifdef DEBUG
#define DBG(...) printf(__VA_ARGS__)
#else
#define DBG(...)
#endif

using namespace std;

typedef long long ll;


int main() {
  ll T;
  cin >> T;

  for (ll t=1; t<=T; t++)
  {
    string s;
    cin >> s;
    ll C = 0;

    if (s[0] == '-') C++;
    for (ll i=1; i<s.length(); i++) 
      if (s[i] == '-' && s[i-1] == '+')
        C += 2;

    cout << "Case #" << t << ": " << C << endl;    
  }
  return 0;
}


#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define REP(i, a, b) for (int i = int(a); i <= int(b); i++)

ll t, n;

int main() {
  ios_base::sync_with_stdio(false); 
  cin.tie(NULL);
  cin >> t;
   
  REP(tt, 1, t) {
    set<char> s;
    cin >> n;

    stringstream ss;
    string num;
    ss << n;
    ss >> num;

    cout << "Case #" << tt << ": ";

    if (!n) {
      cout << "INSOMNIA" << endl;
      continue;
    }

    ll it = 1, n2;
    while (true) {
      for (ll i = 0; i < num.size(); ++i) { 
        if (s.find(num[i]) == s.end()) {
          s.insert(num[i]);
        }
      }
      if (s.size() == 10) break;

      n2 = n * ++it;

      ss.clear();
      ss << n2;
      ss >> num;
    }

    cout << n2 << endl;
  }
  return 0;
}


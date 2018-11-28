#include <iostream>
#include <string>
#include <vector>

using namespace std;

int TC;
string s;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cin >> TC;
  for(int tc = 1; tc <= TC; ++tc) {
    cout << "Case #" << tc << ": ";
    cin >> s;
    // cout << s << "\n";
    int sz = s.size();
    vector<bool> v(sz);
    int p = 0, n = 0;
    for (int i = 0; i < sz; ++i)
      if (s[i] == '-')
	v[i] = false, ++n;
      else
	v[i] = true, ++p;
    // cout << p << " " << n << "\n";
    int sol = 0;
    while (p != sz) {
     if (v[0]) {
       for (int i = 0; i < sz; ++i)
	 if (!v[i]) break;
	 else 
	   v[i] = false, ++n, --p;
     } else {
       for (int i = 0; i < sz; ++i)
	 if (v[i]) break;
	 else
	   v[i] = true, --n, ++p;
     }
     ++sol;
    }
    cout << sol << "\n"; 
   }
}

#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

string flip(string s) {
  reverse(s.begin(), s.end());
  for(string::iterator it = s.begin(); it != s.end(); ++it) *it = "+-"[*it == '+'];
  return s;
}

int findpc(string s) {
  size_t loc = s.rfind('-');
  if(string::npos == loc) return 0;

  s = s.substr(0, loc + 1);
  loc = s.find('+');
  if(loc == string::npos) return 1;
  if(0 != loc) {
	return 1 + findpc( flip(s) );
  } else {
   loc = s.find('-');
   if(0 == loc) return 1;
   return 2 + findpc( flip( s.substr(loc) ) );
  }
}

int main() {
  int T;
  std::ios_base::sync_with_stdio(false);
  cin.tie(0);
  cin >> T;
  for(int cn = 1; cn <= T; ++cn) {
cerr << cn << " of " << T << '\n';
    string pc;
	cin >> pc;


	cout << "Case #" << cn << ": ";
	cout << findpc(pc) << "\n";
  }
}

#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
#include <string>
#include <set>
#include <sstream>

using namespace std;

#define lli long long int

int main() {
  int totalTc;
  cin >> totalTc;
  for(int tc = 1; tc <= totalTc; tc++) {
    string str; cin >> str;
    int splitIdx = str.find_first_of("/");
    string ps = str.substr(0, splitIdx);
    string qs = str.substr(splitIdx+1);
    lli p,q;
    stringstream ss; 
    ss << ps + " " + qs;
    ss >> p >> q;

    for (lli i = 2; i*i <= q; i++) {
      while ((q % i == 0) && (p % i == 0)) {
	q /= i;
	p /= i;
      }
    }
    cout << "Case #" << tc << ": ";
    if ((q-1) & q) {
      cout << "impossible" << endl;
      continue;
    }
    int ans = 1;
    while (p < q/2) {
      ans++;
      q /= 2;
    }
    if ( ans > 40 ) {
      cerr << "oops ans over 40" << ans << endl;
      cout << "impossible" << endl;
      continue;
    }
    cout << ans << endl;
  }
  return 0;
}

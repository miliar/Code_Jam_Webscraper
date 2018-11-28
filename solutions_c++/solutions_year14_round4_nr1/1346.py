#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int n, x;
vector<int> s;

int main() {
  int T;
  cin >> T;
  for(int tcase=1;tcase<=T;++tcase) {
    cin >> n >> x;
    s.resize(n);
    for(int i=0;i<n;++i)
      cin >> s[i];
    sort(s.rbegin(), s.rend());
    vector<bool> done(n);
    int cur = 0;
    for(int i=0;i<n;++i) {
      for(int j=0;j<i;++j)
	if(!done[j] && s[i] + s[j] <= x) {
	  done[i] = done[j] = true;
	  break;
	}
      if(!done[i]) ++cur;
    }
    cout << "Case #" << tcase << ": " << cur << '\n';
  }
}

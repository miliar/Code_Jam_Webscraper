#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int n;
vector<int> a;
vector<int> p;

int main() {
  int T;
  cin >> T;
  for(int tcase=1;tcase<=T;++tcase) {
    cin >> n;
    a.resize(n);
    p.resize(n);
    for(int i=0;i<n;i++)
      cin >> a[i];
    const int maxi = max_element(a.begin(), a.end()) - a.begin();
    int sol = n * n;
    for(int signs=0;signs<(1LL << n);signs++) {
      for(int j=0;j<n;j++)
	p[j] = ((signs >> j) & 1) * 2;
      p[maxi] = 1;
      int cur = 0;
      for(int i=0;i<n;i++)
	for(int j=0;j<i;j++)
	  if(p[j] != p[i]) cur += (p[j] > p[i]);
	  else
	    if(p[i])
	      cur += (a[i] > a[j]);
	    else
	      cur += (a[i] < a[j]);
      //cerr << signs << ' ' << cur << '\n';
      sol = min(sol, cur);
    }
    cout << "Case #" << tcase << ": " << sol << '\n';
  }
}

#include <bits/stdc++.h>

using namespace std;

typedef long long          ll;
typedef vector<int>        vi;
typedef pair<int, int>     ii;
typedef vector<ii>         vii;
typedef set<int>           si;
typedef map<string, int>   msi;

int main() {
  int t, tc = 0; scanf("%d", &t);

  while(t--) {
    ll n; scanf("%lld", &n);
    ll m = n;
    n = 0;

    int c = 0;
    vector<bool> D(10, false);

    if(m == 0) c = 11;

    while(c < 10) {
      n += m;
      
      ll x = n;
      
      while(x > 0) {
	if(!D[x%10]) {
	  D[x%10] = true;
	  c++;
	}
	x /= 10;
      }
    }

    if(c == 11) printf("Case #%d: INSOMNIA\n", ++tc, n);
    else printf("Case #%d: %lld\n", ++tc, n);
  }

  return 0;
}

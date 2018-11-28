#include <bits/stdc++.h>

using namespace std;

typedef long long          ll;
typedef vector<int>        vi;
typedef pair<int, int>     ii;
typedef vector<ii>         vii;
typedef set<int>           si;
typedef map<string, int>   msi;

int main() {
  int t, tc=0; scanf("%d", &t);

  while(t--) {
    int n; scanf("%d", &n);
    string s; cin >> s;

    int c = 0, a = 0;
    for(int i=0; i<s.length(); i++) {
      if(c >= i) {
	c += (s[i] - '0');
      } else {
	a += (i - c);
	c = i;
	c += (s[i] - '0');
      }
    }

    printf("Case #%d: %d\n", ++tc, a);
  }

  return 0;
}

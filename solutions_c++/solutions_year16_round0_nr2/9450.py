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
    string s;
    cin >> s;
    int c = 1;

    for(int i=1; i<s.length(); i++) {
      if(s[i-1] != s[i]) c++;
    }

    if(s[s.length()-1] == '-') printf("Case #%d: %d\n", ++tc, c);
    else printf("Case #%d: %d\n", ++tc, c - 1);

  }

  return 0;
}

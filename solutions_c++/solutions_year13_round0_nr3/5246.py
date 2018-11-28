#include <iostream>
#include <string>
#include <sstream>
#include <cstring>
#include <algorithm>
using namespace std;

int sq[1001];
bool ok[1001];

bool paren(string x) {
  string p = x;
  reverse(p.begin(), p.end());
  return p == x;
}

bool check(int x) {
  if (sq[x] == -1) return false;
  stringstream ss;
  ss<<x;
  string xs = ss.str();
  ss.str("");
  ss<<sq[x];
  string xxs = ss.str();
  ss.str("");
  return paren(xs) && paren(xxs);
}

int main() {
  int T,A,B;
  cin>>T;
  memset(sq, -1, sizeof(sq));
  memset(ok, false, sizeof(ok));
  for (int i=0; i<=1000; ++i)
    if (i*i <= 1000) sq[i*i] = i;
  for (int x = 1; x <= 1000; ++x)
    ok[x] = check(x);

  for (int tc=1; tc<=T; ++tc) {
    cin>>A>>B;
    int ans = 0;
    for (int p=A; p<=B; ++p)
      if (ok[p]) ans++;
    cout<<"Case #"<<tc<<": "<<ans<<endl;
  }
}

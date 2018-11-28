#include <iostream>
#include <stdlib.h>
#include <string>
#define ll unsigned long long int
using namespace std;

bool needMove(char c, int dir) {
  int r = false;
  if (c == '-')
    r = true;

  if (!dir)
    r = !r;

  return r;
}

int main() {
  ll T;
  cin>>T;

  for (int k = 0; k < T; k++) {
    string s;

    cin>>s;
    int sz = s.size();
    int dir = 1;
    int ans = 0;
    for (int i = sz - 1; i >= 0; i--) {
      if (needMove(s[i], dir)) {
        ans++;
        dir = !dir;
      }
    }

    cout<<"Case #"<<(k +1)<<": "<<ans<<endl;
  }
}
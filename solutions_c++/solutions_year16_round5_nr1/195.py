#include <cstdio>
#include <vector>
#include <cassert>
#include <string>
#include <algorithm>
#include <utility>
#include <stack>

using namespace std;

typedef long long ll;

int main() {
  ll T;
  scanf("%lld", &T);
  for(ll cas=1; cas<=T; cas++) {
    char S[20002];
    scanf("%s", S);
    ll n = strlen(S);
    char p = 'X';

    stack<char> ST;
    for(ll i=0; i<n; i++) {
      if(!ST.empty() && ST.top() == S[i]) {
        ST.pop();
      } else {
        ST.push(S[i]);
      }
    }
    assert(ST.size()%2 == 0);
    ll score = (n - ST.size()/2)*5;
    printf("Case #%lld: %lld\n", cas, score);
  }
}

#include <iostream>
#include <string>
#include <algorithm>
#include <cctype>
#include <numeric>
#include <vector>
#include <cstdio>
#include <set>

using namespace std;

using ll = long long;
using l = long;


void digs(ll n, bool *ar) {
  while (n) {
    ar[n%10] = true;
    n = n/10;
  }
}

bool check(bool *ar) {
  bool flag = true;

  for (int i = 0; i < 10; ++i)
    if (ar[i] == false) {
      flag = false;
      break;
    }
  return flag;
}

int main() {

  freopen("A-large.in","r",stdin);
  freopen("output.out","w",stdout);
  
  int tc;
  scanf("%d", &tc);

  for (int t = 1; t <= tc; ++t) {
    ll n;
    scanf("%lld",&n);
    ll ori = n;
    set<ll> vec;
    bool ar[10];
    for (int i = 0; i < 10; ++i)
      ar[i] = false;

    ll add = 2;
    while (true) {

      if (!vec.empty()) {
	auto it = vec.find(n);
	if (it != vec.end()) {
	  printf("Case #%d: INSOMNIA\n",t);
	  break;
	}
      }

      vec.insert(n);

      digs(n,ar);
      bool flag = check(ar);

      if (flag) {
	printf("Case #%d: %lld\n",t,n);
	break;
      }

      n = ori*add;
      ++add;
    }
  }
  
  return 0;
}

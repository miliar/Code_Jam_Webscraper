//Esteban Foronda Sierra
using namespace std;
#include <algorithm>
#include <iostream>
#include <iterator>
#include <numeric>
#include <sstream>
#include <fstream>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <unordered_map>

template <class T> string toStr(const T &x)
{ stringstream s; s << x; return s.str(); }
template <class T> int toInt(const T &x)
{ stringstream s; s << x; int r; s >> r; return r;}

#define ll long long
#define D(x) cout << #x << " " << x << endl

ll getSleep(ll x) {
  if(x == 0LL) return -1;
  int rest = 10;
  int f[10];
  for(int i = 0; i < 10; ++i) f[i] = 0;
  ll curr = x;
  while(rest > 0) {
    string xs = toStr(curr);
    for(int i = 0; i < xs.size(); ++i) {
      int digit = xs[i] - '0';
      if(f[digit] == 0) {
        f[digit] = 1;
        rest--;
        if(rest == 0) break;
      }
    }
    curr += x;
  }
  return curr -= x;
}

int main(){
  int n;
  cin >> n;
  for(int i = 0; i < n; ++i) {
    ll starting;
    cin >> starting;
    ll result = getSleep(starting);
    if(result == -1) printf("Case #%d: INSOMNIA\n", i + 1);
    else printf("Case #%d: %lld\n", i + 1, result);
  }
	return 0;
}

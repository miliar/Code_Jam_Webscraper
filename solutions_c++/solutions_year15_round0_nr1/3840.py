#include <algorithm>
#include <bitset>
#include <cassert>
#include <climits>
#include <cmath>
#include <complex> 
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <fstream>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <vector>

using namespace std;

#define sf(n)         scanf("%lf",&n)
#define fill(a,v)     memset(a, v, sizeof a)
#define bitcount      __builtin_popcount
#define all(x)        x.begin(), x.end()
#define pb(z)       push_back( z )
#define gcd           __gcd

bool isNum(char c) { return ('0' <= c && c <= '9'); }
template<typename T>
T read(T &res) {
  res = 0; char c, neg = 0;
  do { c=getchar(); } while (!isNum(c) && c != '-');
  if (c == '-') { neg = 1; c = getchar(); }
  while (isNum(c)) { res = res * 10 + c-'0'; c = getchar(); }
  return neg ? -res : res;
}

typedef unsigned long long ull;
typedef long long ll;
typedef long double ld;

#define readInt read<int>
#define readLL read<ll>

//37ae83cb1254dc6d8f3f075ebd91cb

int main() {
  int cases; cin >> cases;
  for (int cs=1; cs <= cases; cs++) {
    int len; 
    cin>>len; 
    
    string a;
    cin>>a;
    
    ll extras = 0;
    ll res = 0;
    
    for (int i=0; i <= len; i++) {
      int need = i;
      if (extras < need) {
        res += need - extras;
        extras += need - extras;
      }
      int existing = a[i] - '0';
      extras += existing;
    }
    printf("Case #%d: %lld\n", cs, res);
  }
}

//#include<bits/stdc++.h>
#include<cmath>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
#define IOS ios_base::sync_with_stdio(0); cin.tie(0);
#define clean(n,val) memset((n),(val),sizeof(n))
#define MP make_pair
#define PB push_back
#define ll long long
#define debug(x) x
typedef pair<int, int> PI;
const int INF = 0xFFFFFFF;
const int MOD = 1e9+7;
const int MAXN = 100005;

int t, x;
char s[1005];

bool check(int p) {

  int now = p;
  for ( int i = 0 ; i <= x ; i++ ) {
    int a = s[i] - '0';
    if ( a && i > now ) return false;
    now += a;
  }
  return true;
}

int main() {
    #ifdef LOCAL
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif

    cin >> t;
    int kase = 0;
    while ( t-- ) {
      cin >> x >> s;

      int lo = 0, hi = 10000, mid;
      while ( lo != hi ) {
        mid = lo + (hi - lo) / 2;
        if ( check(mid) ) {
          hi = mid;
        } else {
          lo = mid + 1;
        }
      }

      cout << "Case #" << ++kase << ": " << lo << endl;
    }



    return 0;
}

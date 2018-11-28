#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cctype>
#include <algorithm>
#include <string>
#include <vector>
#include <deque>
#include <stack>
#include <queue>
#include <list>
#include <map>
#include <set>

using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int> > vvi;
typedef vector<string> vs;
typedef vector<long long> vll;
#define sz(a)  int((a).size())
#define pb  push_back
#define all(c)  (c).begin(),(c).end()
#define mset(arr,val)  memset(arr,val,sizeof(arr))
#define tr(c,i)  for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)
#define rep(var,n)  for(int var=0;var<(n);var++)
#define forr(var,from,to) for(int var=(from);var<=(to);var++) 
#define found(s,e)  ((s).find(e)!=(s).end())
#define remove_(c,val) (c).erase(remove((c).begin(),(c).end(),(val)),(c).end())
#define lastc(str) (*((str).end()-1))

// #include "cout.h"

main(){
  int _T;
  scanf("%d", &_T);
  rep(_t,_T){
    char buf[1000001]; ll n;
    scanf("%s%lld", buf, &n);
    ll L = strlen(buf);
    // printf("%d: %d(%s) %d\n", 1+_t, L, buf, n);
    vector<ll> cnt(L, 0LL);
    vector<bool> bnt(L, false);
    ll c = 0;
    for(int i=L-1; i>=0; --i) {
      char ch = buf[i];
      if (ch=='a' || ch=='e' || ch=='i' || ch=='o' || ch=='u') {
        c = 0; cnt[i] = 0;
      } else {
        cnt[i] = ++c;
        if (c >= n) bnt[i] = true;
      }
    }
    // cout << cnt << endl;
    // cout << bnt << endl;

    ll u = n-1;
    ll ans = 0LL;
    ll pre = 0LL;
    rep(i,L-u) {
      // printf("+ (%d-%d)-%d * (1+%d)\n", L,i,u,pre);
      if (bnt[i]) {
        ans += ((L-i)-u) * (1+pre);
        pre = 0LL;
      } else {
        ++pre;
      }
    }

    printf("Case #%d: %lld\n", 1+_t, ans);
  }
}

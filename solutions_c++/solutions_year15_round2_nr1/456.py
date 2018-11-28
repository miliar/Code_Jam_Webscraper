#include <algorithm>
#include <assert.h>
#include <climits> 
#include <cmath>
#include <cstdio>
#include <fstream>
#include <iostream>
#include <map>
#include <memory.h>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>

using namespace std;

#define pb push_back
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++) 
#define REP(i,n) FOR(i,0,n)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define CL(a,v) memset((a),(v),sizeof(a))
#define mp make_pair
#define X first
#define Y second 
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c)) 

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> VI;

ll reverse(ll n) {
    ll c = 0;
    ll res =0;
    while(n>0){
        res = res*10 + (n%10);
        n/=10;
    }
    return res;
}

ll mid(ll x) {
    VI d;
    while (x > 0) {
        d.push_back(x % 10);
        x /= 10;
    }
    int n = (int)d.size();
    n = (n + 1) / 2;
    ll m = 1;
    ll val = 0;
    REP(i, n) {
        val = m * d[i] + val;
        m *= 10;
    }
    return val;
}

ll solve(ll n) {
  ll steps = 0;
  while (n > 0) {
    if (n % 10 == 0) {
      --n;
      ++steps;
      continue;
    }
    ll m = mid(n);
    if (m > 1) {
      n -= m - 1;
      steps += m - 1;
      continue;
    }
    m = reverse(n);
    if (m < n) {
      steps++;
      n = m;
      continue;
    }
    --n;
    ++steps;
  }
  return steps;
}

int main(int argc, char const *argv[]) {

    freopen("input.txt","r", stdin);
    freopen("a_small.txt","w",stdout);

    int T; cin>>T;

    REP(t,T) {
        ll n; cin>>n;
        ll res = solve(n);
        cout<<"Case #"<<t+1<<": "<<res<<endl;
    }

    return 0;
}
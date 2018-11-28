#include <iostream>
typedef long long ll;

#include <queue>
#define REP(i,n) for(int i=0; i<(int)(n); i++)

#include <cstdio>
inline int getInt(){ int s; scanf("%d", &s); return s; }

#include <set>

using namespace std;

ll check(ll tm, const vector<int> &m){
  ll ret = 0;
  REP(i,m.size())
    ret += 1 + tm / m[i];
  return ret;
}

int main(){
  const int T = getInt();

  REP(t, T){
    const int b = getInt();
    const int n = getInt();

    vector<int> m(b);
    REP(i,b) m[i] = getInt();

    ll low = 0;
    ll high = (ll)n * 100000;

    while(low <= high){
      const ll med = (low + high) / 2;
      if(check(med, m) < n) low = med + 1;
      else high = med - 1;
    }

    int prev = 0;
    if(low > 0) prev = check(low - 1, m);

    int rest = n - prev;
    REP(i,b) if(low % m[i] == 0){
      if(--rest == 0){
	printf("Case #%d: %d\n", t + 1, i + 1);
	break;
      }
    }

  }

  return 0;
}

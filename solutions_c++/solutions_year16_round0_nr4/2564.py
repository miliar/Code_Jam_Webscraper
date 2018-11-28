typedef long long ll;

#define REP(i,n) for(int i=0; i<(int)(n); i++)

#include <cstdio>
inline int getInt(){ int s; scanf("%d", &s); return s; }

#include <set>

using namespace std;

ll pos(ll p, ll k, ll c) {
  if(c == 1) return p;
  return pos((p - 1) * k + p, k, c - 1);
}

int main(){
  const int t = getInt();
  REP(tt, t) {
    const int k = getInt();
    const int c = getInt();
    const int s = getInt();

    printf("Case #%d:", tt + 1);
    REP(i,s){
      printf(" %d", i + 1);
    }
    puts("");
  }
  return 0;
}

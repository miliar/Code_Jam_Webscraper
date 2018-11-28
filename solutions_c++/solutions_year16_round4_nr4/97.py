#define print(x) printf("%d\n",x)

#include <algorithm>
#include <queue>
#include <iostream>
#include <cstdio>
#include <set>
#define REP(i,n) for(int i=0; i<(int)(n); i++)

using namespace std;

inline int getInt(){ int s; scanf("%d", &s); return s; }
inline string getStr() { char s[32]; scanf("%s", s); return s; }

bool ok(const vector<int> &a, int pos, int f) {
  const int n = a.size();
  if(pos == n) return true;
  if((a[pos] & f) == 0) return false;

  REP(i,n) if((a[pos] & f & (1 << i)) != 0)
    if(!ok(a, pos + 1, f ^ (1 << i))) return false;
  return true;
}

bool check(const vector<int> &a) {
  const int n = a.size();
  vector<int> v(n); REP(i,n) v[i] = i;

  do {
    vector<int> b(n);
    REP(i,n) b[i] = a[v[i]];
    if(!ok(b, 0, (1 << n) - 1)) return false;
  }while(next_permutation(v.begin(), v.end()));

  return true;
}

void printa(const vector<int> &a) {
  const int n = a.size();
  REP(i,n){ REP(j,n) printf("%d", (a[i] & (1 << (n - 1 - j))) != 0); puts(""); }
}

int main(){
  const int T = getInt();
  REP(t, T) {
    const int n = getInt();
    vector<int> a(n);
    REP(i,n) {
      const string s = getStr();
      REP(j,n) a[i] |= ((s[j] - '0') << j);
    }

    int ans = n * n;
    REP(i,1<<(n*n)) {
      vector<int> b(n);
      int t = i;
      REP(i,n) {
	b[i] = t & ((1 << n) - 1);
	t >>= n;
      }

      int cost = 0;
      bool ok = true;
      REP(i,n) REP(j,n) {
	if((a[i] & (1 << j)) != 0 && (b[i] & (1 << j)) == 0)
	  ok = false;
	if((a[i] & (1 << j)) == 0 && (b[i] & (1 << j)) != 0)
	  cost++;
      }

      if(!ok) continue;
      if(check(b)){
	// printa(a);
	// printa(b); printf("=> %d\n", cost); puts("");
	ans = min(ans, cost);
      }
    }

    printf("Case #%d: %d\n", t + 1, ans);
  }
  return 0;
}














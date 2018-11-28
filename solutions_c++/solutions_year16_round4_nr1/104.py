#include <algorithm>
#define REP(i,n) for(int i=0; i<(int)(n); i++)

#include <cstdio>
inline int getInt(){ int s; scanf("%d", &s); return s; }

#include <iostream>
#include <queue>
#include <set>

using namespace std;

char loser(char c) {
  if(c == 'R') return 'S';
  if(c == 'S') return 'P';
  return 'R';
}

pair<bool, vector<char> > solve(const vector<char> &c, int R, int S, int P) {
  if(R + S + P == 0) return make_pair(true, c);

  const int n = c.size();
  vector<char> ret; ret.reserve(n + n);

  for(const char cc : c) {
    if(cc == 'R') {
      if(S == 0) {
	return make_pair(false, ret);
      } else {
	--S; ret.push_back('S');
	ret.push_back(cc);
      }
    } else if(cc == 'S') {
      if(P == 0) {
	return make_pair(false, ret);
      } else {
	--P; ret.push_back('P');
	ret.push_back(cc);
      }
    } else {
      if(R == 0) {
	return make_pair(false, ret);
      } else {
	--R; ret.push_back('R');
	ret.push_back(cc);
      }
    }
  }

  return solve(ret, R, S, P);
}

vector<char> vsort(vector<char> v) {
  const int n = v.size();
  if(n == 1) return v;
  vector<char> a(n / 2);
  vector<char> b(n / 2);
  REP(i,n/2) a[i] = v[i]; a = vsort(a);
  REP(i,n/2) b[i] = v[n/2 + i]; b = vsort(b);
  if(a > b) swap(a, b);
  REP(i,n/2) v[i] = a[i];
  REP(i,n/2) v[n/2 + i] = b[i];
  return v;
}

int main(){
  const int T = getInt();
  REP(t,T) {
    const int n = getInt();
    const int R = getInt();
    const int P = getInt();
    const int S = getInt();

    vector<char> ans(1 << n, 'Z');

    if(S > 0) {
      const auto a = solve(vector<char>(1, 'S'), R, S - 1, P);
      if(a.first) ans = min(ans, vsort(a.second));
    }

    if(R > 0) {
      const auto a = solve(vector<char>(1, 'R'), R - 1, S, P);
      if(a.first) ans = min(ans, vsort(a.second));
    }

    if(P > 0) {
      const auto a = solve(vector<char>(1, 'P'), R, S, P - 1);
      if(a.first) ans = min(ans, vsort(a.second));
    }

    printf("Case #%d: ", t + 1);
    if(ans[0] != 'Z') {
      for(char c : ans) putchar(c);
      puts("");
    } else {
      puts("IMPOSSIBLE");
    }
  }
}

















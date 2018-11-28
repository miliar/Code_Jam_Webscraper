#include <cstdio>
#include <vector>
#include <cassert>
#include <string>
#include <algorithm>
#include <utility>
#include <stack>
#include <set>
#include <iostream>

using namespace std;

typedef long long ll;

vector<vector<vector<int>>> SEEN;
vector<vector<vector<int>>> ANS;
bool can(string& S, string& A, string& B, ll si, ll ai, ll bi, char reg) {
  if(si == S.size()) { return true; }
  if(SEEN[si][ai][bi]) {
    return ANS[si][ai][bi];
  }
  bool ans = false;
  if(ai < A.size()) {
    if(A[ai]=='?') {
      if(reg==S[si] && can(S, A, B, si+1, ai+1, bi, reg)) {
        ans = true;
      }
    } else {
      if(can(S, A, B, si, ai+1, bi, A[ai])) {
        ans = true;
      }
    }
  }
  if(bi < B.size()) {
    if(B[bi]=='?') {
      if(reg == S[si] && can(S, A, B, si+1, ai, bi+1, reg)) {
        ans = true;
      }
    } else {
      if(can(S, A, B, si, ai, bi+1, B[bi])) {
        ans = true;
      }
    }
  }
  SEEN[si][ai][bi] = true;
  ANS[si][ai][bi] = ans;
  return ans;
}

int main() {
  ll T;
  cin >> T;
  for(ll cas=1; cas<=T; cas++) {
    ll n, L;
    cin >> n >> L;
    set<string> GOOD;
    string BAD;
    for(ll i=0; i<n; i++) {
      string s;
      cin >> s;
      GOOD.insert(s);
    }
    cin >> BAD;

    if(GOOD.count(BAD) == 1) {
      printf("Case #%lld: IMPOSSIBLE\n", cas);
    } else if(L==1) {
      printf("Case #%lld: 0 ?\n", cas);
    } else {
      string A;
      for(ll i=0; i<L; i++) {
        A += "10";
      }
      A += "?1";
      string B;
      for(ll i=0; i<L-1; i++) {
        B += "?";
      }
      ll qs = 0;
      for(char c : A) {
        if(c=='?') { qs++; }
      }
      for(char c : B) {
        if(c=='?') { qs++; }
      }
      assert(qs == L);
      assert(A.size() > 0);
      assert(B.size() > 0);
      assert(A.size() + B.size() <= 200);
      SEEN = vector<vector<vector<int>>>(L+1, vector<vector<int>>(A.size()+1, vector<int>(B.size()+1, false)));
      ANS = vector<vector<vector<int>>>(L+1, vector<vector<int>>(A.size()+1, vector<int>(B.size()+1, false)));
      assert(!can(BAD, A, B, 0, 0, 0, '0'));
      for(string g : GOOD) {
        SEEN = vector<vector<vector<int>>>(L+1, vector<vector<int>>(A.size()+1, vector<int>(B.size()+1, false)));
        ANS = vector<vector<vector<int>>>(L+1, vector<vector<int>>(A.size()+1, vector<int>(B.size()+1, false)));
        assert(can(g, A, B, 0, 0, 0, '0'));
      }
      printf("Case #%lld: %s %s\n", cas, A.c_str(), B.c_str());
    }
  }
}

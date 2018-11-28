#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>

#define REP(i,n) for(int i = 0; i < (n); i++)
#define FOR(i,a,b) for(int i = (a); i <= (b); i++)
#define FORD(i,a,b) for(int i = (a); i >= (b); i--)

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;

int solve() {
  string s;
  cin >> s;
  int res = 0;
  FOR(i, 1, s.size() - 1) {
    if (s[i] != s[i-1]) res++;
  }
  if (s[s.size() - 1] == '-') res++;
  return res;
}

int main() {
  int t;
  cin >> t;
  REP(i, t) {
    cout << "Case #" << (i+1) << ": " << solve() << endl;
  }
}
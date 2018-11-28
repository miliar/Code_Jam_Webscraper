#pragma comment(linker, "/stack:32000000")
#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <map>
#include <set>
#include <cmath>
#include <sstream>
#include <stack>
#include <cassert>
#include <string.h>
#include <ctime>

#define pb push_back
#define mp make_pair
#define PI 3.1415926535897932384626433832795
#define sqr(x) (x)*(x)
#define forn(i, n) for(int i = 0; i < n; ++i)
#define ALL(x) x.begin(), x.end()
#define sz(x) int((x).size())
#define X first
#define Y second
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
using namespace std;
typedef pair<int,int> pii;
const int INF = 2147483647;
const ll LLINF = 9223372036854775807LL;

map<pair<int, char>, string > mm;

string chars = "RPS";

string getans(int n, char c) {
  if (n == 0) {
    string res = "";
    res += c;
    return res;
  }
  if (mm.count(mp(n, c))) return mm[mp(n,c)];
  vector<string> tans;
  if (c == 'R') tans.pb(getans(n-1,'R')), tans.pb(getans(n-1,'S'));
  else if (c == 'P') tans.pb(getans(n-1,'P')), tans.pb(getans(n-1,'R'));
  else if (c == 'S') tans.pb(getans(n-1,'S')), tans.pb(getans(n-1,'P'));
  sort(ALL(tans));
  return mm[mp(n,c)] = tans[0] + tans[1];
}

vector<int> getcounts(const string& s) {
  vector<int> res(3);
  forn(i, sz(s)) forn(j, 3) if (s[i] == chars[j]) res[j]++;
  return res;
}

int main()
{
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
  int T; scanf("%d", &T);
  for (int tn = 1; tn <= T; ++tn) {
    int n; scanf("%d", &n);
    vector<int> cc(3);
    forn(i, 3) scanf("%d", &cc[i]);
    vector<string> cands;
    forn(j, 3) {
      string cur = getans(n, chars[j]);
      vector<int> curres = getcounts(cur);
      if (curres == cc) cands.pb(cur);
    }
    sort(ALL(cands));
    printf("Case #%d: ", tn);
    if (sz(cands)) printf("%s\n", cands[0].c_str());
    else printf("IMPOSSIBLE\n");
  }
  return 0;
}
#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define ull unsigned long long
#define ld long double
#define pb push_back
#define popb pop_back

#define pii pair<int,int>
#define mp make_pair
#define X first
#define Y second

#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)

#define maxN 205

int T;
int N;
map<ll, int> lang[2];
set<ll> newlang;
set<ll> bigenglish;
vector<ll> sentence[maxN];

ll string_to_ll(string k) {
  ll ans = 1;
  REP(i, (int)k.length()) {
    ans = ans * 27 + k[i] - 'a';
  }
  return ans;
}

int main() {
  scanf("%d ", &T);
  FOR(t, 1, T) {
    scanf("%d ", &N);
    lang[0].clear(); lang[1].clear();
    bigenglish.clear();
    REP(i, N - 2) sentence[i].clear();
    int in_both = 0;
    REP(i, N) {
      string w;
      char c;
      while (scanf("%c", &c) == 1) {
        ll ww = string_to_ll(w);
        if (c == ' ' || c == '\n') {
          if (i < 2) {
            if (i == 0) bigenglish.insert(ww);
            if (i == 1 && lang[0].count(ww)) {
//              printf("ok\n");
              ++in_both;
              lang[0].erase(ww);
            } else {
              lang[i][ww] = 0;
            }
          } else {
            sentence[i - 2].push_back(ww);
          }
          w = "";
        } else {
          w.push_back(c);
        }
        if (c == '\n') break;
      }
    }
    int mincnt = maxN * 10 + 2000 + 5;
    REP(i, (1 << (N - 2))) {
      int cnt = in_both;
      newlang.clear();
      REP(j, N - 2) {
        if ((1 << j) & i) {
          REP(k, (int)sentence[j].size()) {
            if (!bigenglish.count(sentence[j][k]) && !lang[1].count(sentence[j][k]))
              newlang.insert(sentence[j][k]);
            if (lang[1].count(sentence[j][k]) && lang[1][sentence[j][k]] != i + 1) {
              lang[1][sentence[j][k]] = i + 1;
              ++cnt;
//              printf("now english, before french: %s\n", sentence[j][k].c_str());
            }
          }
        }
      }
      REP(j, N - 2) {
        if (!((1 << j) & i)) {
          REP(k, (int)sentence[j].size()) {
            if (newlang.count(sentence[j][k])) {
              ++cnt;
              newlang.erase(sentence[j][k]);
//              printf("now french, before english(newlang): %s\n", sentence[j][k].c_str());
            }
            else if (lang[0].count(sentence[j][k]) && lang[0][sentence[j][k]] != i + 1) {
              lang[0][sentence[j][k]] = i + 1;
              ++cnt;
//              printf("now french, before english: %s\n", sentence[j][k].c_str());
            }
          }
        }
      }
      mincnt = min(cnt, mincnt);
//      printf("subset %d: cnt %d\n", i, cnt);
    }
    printf("Case #%d: %d\n", t, mincnt);
  }

  return 0;
}

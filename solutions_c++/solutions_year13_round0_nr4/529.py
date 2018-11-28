#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>

using namespace std;
typedef long long ll;
typedef vector<int> vi;
#define all(c)  (c).begin(),(c).end()
#define tr(i,c)  for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)
#define rep(var,n)  for(int var=0;var<(n);var++)
#define found(s,e)  ((s).find(e)!=(s).end())
#define sz(a)  int((a).size())

typedef pair<int,vector<int> > Chest;

vector<Chest> chests;
vector<vector<int> > chg;

vector<int> keys, way;
int N;

map<pair<int,ll>, int> mm;

int solve(int ix, ll vf) {
  if (ix == N) return 1;

  pair<int,ll> y(ix,vf);
  if (found(mm,y)) return mm[y];

  set<int> ab;
  rep(k, 201){
    if (!keys[k]) continue;
    tr(jt, chg[k]) {
      ll c = *jt;
      if (vf & (1 << c)) continue;
      ab.insert(c);
    }
  }

  tr(it, ab) {
    int c = *it;
    int rq = chests[c].first;

    way[ix] = c;

    --keys[rq];
    rep(j,201) keys[j] += chests[c].second[j];

    int r = solve(ix+1, vf | (1LL << c));
    if (r) return mm[y] = r;

    rep(j,201) keys[j] -= chests[c].second[j];
    ++keys[rq];
  }

  return mm[y] = 0;
}

main(){
  int _T; cin>>_T; // 25
  rep(_t,_T){
    mm.clear();

    printf("Case #%d:", 1+_t);

    int K; cin >> K; // 40 (or 400) keys altogether
    cin >> N; // 1-20, 1-200

    chg.assign(201, vector<int>());

    // types of the keys
    keys.assign(201, 0);
    rep(i,K){
      int k; cin >> k;
      ++keys[k];
    }
    // chests
    chests.resize(N);
    rep(i,N){
      int ti; cin >> ti;
      chests[i].first = ti;
      chests[i].second.assign(201, 0);

      int ki; cin >> ki;
      rep(j,ki) {
        int k; cin >> k;
        ++chests[i].second[k];
      }

      chg[ti].push_back(i);
    }

    way.assign(N, -1);

    int r = solve(0, 0LL);
    if (r) {
      tr(it, way) printf(" %d", 1 + *it);
    } else {
      printf(" IMPOSSIBLE");
    }
    printf("\n");
  }
}

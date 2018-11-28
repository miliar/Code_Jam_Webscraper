#include <iostream>
#include <ctime>
#include <fstream>
#include <cmath>
#include <cstring>
#include <cassert>
#include <cstdio>
#include <algorithm>
#include <iomanip>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <complex>
#include <utility>
#include <cctype>
#include <list>
#include <bitset>

using namespace std;

#define FORALL(i,a,b) for(int i=(a);i<=(b);++i)
#define FOR(i,n) for(int i=0;i<(n);++i)
#define FORB(i,a,b) for(int i=(a);i>=(b);--i)

typedef long long ll;
typedef long double ld;
typedef complex<ld> vec;

typedef pair<int,int> pii;
typedef map<int,int> mii;

#define pb push_back
#define mp make_pair

#define MAXN 52
char S[MAXN];
bool adj[MAXN][MAXN];
bool tmp[MAXN][MAXN];

int L[MAXN];
int R[MAXN];

bool is_valid(int N) {
  memset(L,0,sizeof(L));
  memset(R,0,sizeof(R));

  FOR(i,N) FOR(j,N) {
    if (adj[i][j]) {
      L[i] |= (1<<j);
      R[j] |= (1<<i);
    }
  }

  FOR(i,N) {
    //cout << i << endl;
    bool found = false;
    int s = L[i];
    for(int t = s; t; t = (t-1)&s) {
      int neighbors = 0;
      FOR(j,N) if (t & (1<<j)) neighbors |= R[j];
      neighbors = neighbors & (~(1<<i));
      if (__builtin_popcount(neighbors) < __builtin_popcount(t)) {
        found = true;
        break;
      }
    }
    if (!found) return false;
  }

  return true;
}

void clear() {
  memset(adj,0,sizeof(adj));
}

void add_edge(int i, int j) {
  adj[i][j] = true;
  L[i] |= (1<<j);
  R[j] |= (1<<i);
}

vector<pii> all_edges;

int main() {

  int TEST,N;
  scanf("%d",&TEST);
  FOR(test,TEST) {
    clear();
    all_edges.clear();
    scanf("%d",&N);
    FOR(i,N) FOR(j,N) all_edges.pb(mp(i,j));
    FOR(i,N) {
      scanf("%s",&S[0]);
      FOR(j,N) if (S[j] == '1') add_edge(i,j);
    }

    int ans = 100000000;
    int K = all_edges.size();
    int S = (1<<K);
    FOR(s,S) {
      int cost = __builtin_popcount(s);
      memcpy(tmp,adj,sizeof(tmp));
        FOR(k,K) if (s & (1<<k)) {
          int i = all_edges[k].first;
          int j = all_edges[k].second;
          adj[i][j] = true;
        }
        if (is_valid(N)) ans = min(ans,cost);
      memcpy(adj,tmp,sizeof(adj));
    }

    printf("Case #%d: %d\n",test+1,ans);
  }
}
















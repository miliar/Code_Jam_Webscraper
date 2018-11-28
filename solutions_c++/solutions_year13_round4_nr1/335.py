#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <cstring>

#define FOR(i,k,n) for (int i=(k); i<(int)(n); ++i)
#define REP(i,n) FOR(i,0,n)
#define FORIT(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define sz size()
#define pb push_back
#define mp make_pair
#define ALL(X) (X).begin(),(X).end()

using namespace std;

typedef long long ll;
typedef vector<int> vi;

void output(int c, int n) { printf ("Case #%d: %d\n", c, n); }

int main(void)
{
  int t, n, m;
  cin>>t;
  FOR(cas,1,t+1){
    long long x=0, y=0;
    cin >> n >> m;
    vector<pair<int,int> > v;
    REP(i,m){
      int o,e,p;
      cin>>o>>e>>p;
      long long dist = e-o;
      long long hoge = (n*dist-(dist-1)*dist/2) % 1000002013;
      x += hoge*p;
      v.pb(mp(o,-p));
      v.pb(mp(e,p));
      x %= 1000002013;
    }
    sort(ALL(v));
    vector<pair<int,int> > w;
    REP(i,v.sz){
      if(v[i].second<0){
	w.pb(mp(v[i].first,-v[i].second));
      }
      else {
	long long nin=v[i].second;
	while(nin>0){
	  long long deru=min(nin,(long long)w[w.sz-1].second);
	  long long dist=v[i].first-w[w.sz-1].first;
	  w[w.sz-1].second-=deru;
	  long long hoge = (n*dist-(dist-1)*dist/2)%1000002013;
	  y+=(hoge*deru)%1000002013;
	  if(w[w.sz-1].second==0)w.pop_back();
	  nin-=deru;
	}
      }
      y%=1000002013;
    }
    output(cas,(x-y+1000002013)%1000002013);
  }
  return 0;
}

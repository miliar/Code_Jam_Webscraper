#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;

#define MOD 1000002013

void go(int t) {
  long long N, M, st, en, i, n, j;
  long long tot = 0, cst, tot2 = 0;
  
  vector< pair<int, int> > Events, add;
  
  scanf("%lld %lld",&N,&M);
  for(i=0;i<M;i++) {
    scanf("%lld %lld %lld",&st,&en,&n);
    cst = (en-st)*N - (long long)(en-st)*(en-st-1)/2;
    //printf("## %lld\n",cst);
    cst %= MOD;
    tot += cst * n;
    tot %= MOD;
    Events.push_back( make_pair(st,-n) );
    Events.push_back( make_pair(en,n) );
  }
  //printf("%lld\n",tot);
  tot2 = 0;
  sort(Events.begin(), Events.end());
  for(i=0;i<Events.size();i++){
    if(Events[i].second < 0) {
      add.push_back( Events[i] );
      continue;
    }
    en = Events[i].first;
    n = Events[i].second;
    while(n > 0) {
      j = add.size()-1;
      st = add[j].first;
      if( -add[j].second > n ) {
        //printf("# %d %d %d\n",st,en,n);
        cst = (en-st)*N - (long long)(en-st)*(en-st-1)/2;
        cst %= MOD;
        tot2 += cst * n;
        tot2 %= MOD;
        add[j].second += n;
        n = 0;

      } else {
        //printf("# %d %d %d\n",st,en,-add[j].second);
        cst = (en-st)*N - (long long)(en-st)*(en-st-1)/2;
        cst %= MOD;
        tot2 += cst * (-add[j].second);
        tot2 %= MOD;
        n += add[j].second;
        add.pop_back();
      }
    }
  }
  tot -= tot2;
  if(tot < 0) tot+=MOD;
  tot %= MOD;
  printf("Case #%d: %lld\n",t,tot);
}

int main() {
  int t,T;
  scanf("%d",&T);
  for(t=1;t<=T;t++) go(t);
  return 0;
}

#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

long long int MOD = 1000002013;

long long int mod(long long int k) {
  return ((k%MOD) + MOD) % MOD;
}
long long int min(long long int a, long long int b) {
  if(a<b) {
    return a;
  }
  return b;
}
long long int pyr(long long int n) {
  return mod(n*(n+1)/2);
}
long long int cost(long long int n, long long int st) {
  return mod(pyr(n)-pyr(n-st));
}

long long int solve() {
  int N, M;
  long long int realfare = 0;
  long long int fare = 0;
  cin>>N>>M;

  map<int, long long int> enter;
  map<int, long long int> leave;
  map<int, long long int> tickets;
  set<int> stations;

  for(int m=0;m<M;++m) {
    int o, e;
    long long int p;
    cin>>o>>e>>p;
    enter[o] += p;
    leave[e] += p;
    realfare = mod(realfare + cost(N, e-o)*p);
    stations.insert(o);
    stations.insert(e);
  }

  for(set<int>::iterator i = stations.begin();i!=stations.end();++i) {
    int s = *i;
    // People enter
    tickets[s] += enter[s];
    // People leave
    long long int needed = leave[s];
    set<int>::iterator f = i;
    int from;
    while(needed > 0) {
      from = *f;
      long long int get = min(needed, tickets[from]);
      fare = mod(fare + cost(N, s-from)*get);
      tickets[from] -= get;
      needed -= get;
      f--;
    }
  }

  return mod(realfare-fare);

}

int main(int argc, char** argv) {
  int T;
  cin>>T;

  for(int t=0;t<T;++t) {
    long long int sol = mod(solve());
    cout<<"Case #"<<(t+1)<<": "<<sol<<endl;
  }

  return 0;
}

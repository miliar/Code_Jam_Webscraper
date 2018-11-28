#include <cstdio>
#include <cassert>
#include <vector>
#include <algorithm>

using namespace std;

void apply(vector<double>& s,double p) {
  vector<double> ns;
  for (int i=0;i<int(s.size());++i) ns.push_back(s[i]*(1-p));
  ns.push_back(0.0);
  for (int i=0;i<int(s.size());++i) ns[i+1]+=s[i]*p;
  swap(s,ns);
}

void run() {
  int N,K;
  scanf("%d%d",&N,&K);
  assert(K%2==0 && K<=N);
  vector<double> P(N);
  for (int i=0;i<N;++i) scanf("%lf",&P[i]);
  sort(P.begin(),P.end());
  double sl=0.0;
  for (int j=0;j<=K;++j) {
    vector<double> sol(1,1.0);
    for (int i=0;i<j;++i) apply(sol,P[i]);
    for (int i=0;i<K-j;++i) apply(sol,P[P.size()-1-i]);
    if (sol[K/2]>sl) sl=sol[K/2];
  }
  printf("%f\n",sl);
}

int main() {
  int T;
  scanf("%d",&T);
  for (int t=1;t<=T;++t) {
    printf("Case #%d: ",t);
    run();
  }
  return 0;
}

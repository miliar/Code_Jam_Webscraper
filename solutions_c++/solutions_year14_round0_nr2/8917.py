#include <iostream>
#include <queue>
#include <utility>
#include <iomanip>
#include <tuple>
#include <cstdlib>
#include <ctime>
#include <unistd.h>

using namespace std;

typedef tuple<double,double,int> state;

struct cmp {
  bool operator() (const state& s1, const state& s2) {
    return get<0>(s1) > get<0>(s2);
  }
};

void solve(int i, double c, double f, double x) {
  priority_queue<state,vector<state>,cmp> pq;
  pq.push(make_tuple(0,0,0));
  while(!pq.empty()) {
    state s = pq.top(); pq.pop();
    if(x == get<1>(s)) {
      cout<<"Case #"<<i<<": "<<get<0>(s)<<endl;
      break;
    }
    double income = 2 + get<2>(s) * f;
    double needed = x - get<1>(s);
    state ws = s;
    get<0>(ws) += needed / income;
    get<1>(ws) = x;
    pq.push(ws);

    double fneeded = c - get<1>(s);
    state fs = s;
    get<0>(fs) += fneeded / income;
    get<1>(fs) = 0;
    get<2>(fs)++;
    pq.push(fs);
  }
}

int main() {
  cout<<setprecision(10);
  int N;
  cin>>N;
  for(int i = 0; i < N; ++i) {
    double c,f,x;
    cin>>c>>f>>x;
    solve(i+1,c,f,x);
  }
  return 0;
}

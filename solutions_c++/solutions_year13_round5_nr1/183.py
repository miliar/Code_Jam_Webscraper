#include <cstdlib>
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <cmath>
using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<VI> VVI;
typedef long long LL;
typedef stringstream SS;


#define pb(x) push_back(x)
#define ins(x) insert(x)
#define sz size()
#define len length()

#define REP(i,n) for(int i=0; i<(n); i++)
#define FOR(i,a,b) for(int i=(a),_d=((a)<(b))?1:-1; _d*i<=_d*(b); i+=_d)
#define FOREACH(it,s) for (typeof((s).begin()) it = (s).begin(); it != (s).end(); ++it)
#define SORT(x) (sort((x).begin(),(x).end()))
#define UNIQ(x) ((x).erase(unique((x).begin(),(x).end()),(x).end()))

#define INF 2147450751



double profit(vector<long long> other, vector<long long> me) {
  long long m = 100000000000000LL; 
  for(int i = 0; i < 37; i++) if(other[i] + me[i] < m) m = other[i] + me[i];

  int n = 0;
  long long sum = 0;
  long long total  = 0;
  for(int i = 0; i < 37; i++) if(other[i] + me[i] == m) {
    n++;
    sum += me[i];
  } 
  for(int i = 0; i < 37; i++) total += me[i];
  if(n == 0) return 0;

//  for(int i = 0; i < 37; i++) cerr << other[i] << " " << me[i] << " | ";
  //cerr << double(36*sum)/double(n) - double(total) << endl;


  return double(36*sum)/double(n) - double(total);
}


double try_bid(long long B, vector<long long> V, long long min) {
  vector<long long> me(V.size());

  int nb = 0;
  for(int i = 0; i < V.size(); i++) if(V[i] <= min) {
    me[i] = min - V[i];
    B -= min - V[i];
    nb++;
  }

  double best = 0;
    double p;
  for(int i = V.size()-1; i >= 0; i--) if(V[i] <= min) {
    if(B >= 0) {
      p = profit(V, me);
      if(p > best) best = p;
//      cerr << i << " " << p << endl;
    }
    me[i]++;
    B--;
  }

//  cerr << B << " " << best << endl;
  if(B >= 0) {
      p = profit(V, me);
      if(p > best) best = p;
  }
 // cerr << B << " " << best << endl;

  if(B > 0 && nb > 0) {
    long long d = B/nb;
    for(int i = 0; i < me.size(); i++) if(V[i] <= min) {
      me[i] += d;
      B -= d;
    }

    for(int i = V.size()-1; i >= 0; i--) if(me[i] > 0) {
      double p;
      if(B >= 0) {
        p = profit(V, me);
        if(p > best) best = p;
      }
      me[i]++;
      B--;
    }
  }

//  cerr  << "bubu" << endl;


  return best;
}

double profit(long long B, vector<long long> V) {
  while(V.size() < 37) V.push_back(0);  
  sort(V.begin(), V.end());
  double best = 0.;

//  cerr << V.size() << endl;

  //  cerr << V.size() << endl;

  double p = try_bid(B, V, 0);
 // cerr << 0 << " " << p << endl;
  if(p > best) best = p;

  
  for(int k = 0; k < 1000; k++) {
      double p = try_bid(B, V, k);
      if(p > best) best = p;

  }


  for(int k = 0; k < V.size(); k++) {
//    cerr << k << " " << V[k] << endl;
    if(V[k] > 1) {
     // cerr << "A" << endl;
      double p = try_bid(B, V, V[k]-1);
   //   cerr << "B" << endl;
     // cerr << V[k]-1 << " " << p << endl;
      if(p > best) best = p;
     // cerr << "bibi" << best << endl;
    }
    if(V[k] > 0) {
      double p = try_bid(B, V, V[k]);
//      cerr << V[k] << " " << p << endl;
      if(p > best) best = p;
    }
  }


  return best;







}



int main() {
  cout.precision(16);
  int T;
  cin >> T;
  for(int i = 1; i <= T; i++) {
    long long B, N;
    cin >> B >> N;
    vector<long long> V(N);
    for(int j = 0; j < N; j++) cin >> V[j];
    cout << "Case #" << i << ": " << profit(B, V) << endl;
  }
}

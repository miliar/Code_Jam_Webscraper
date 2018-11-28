// -*- compile-command: "g++ -Wall -Wextra x.cpp -o x && ./x <test.in" -*-
#include <algorithm>
#include <cassert>
#include <cstdio>
#include <cstdio>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <utility>
#include <vector>
#include <iomanip>
using namespace std;
typedef long long in;
#define PB push_back
#define MP make_pair
#define sz(v) (in)(((v).size()))
#define forn(i,n) for(int i=0;i<(n);i++)
#define forv(i,v) forn(i,sz(v))
typedef vector<in> VI;
typedef long double D;
#define temp first
#define rate second
#define litr second
vector<pair<D,D> > A;
in N;
D V,X;
#define eps (D)1e-15
D abs(D x) {
  if(x<0) return -x;
  return x;
}
bool check(D t) {
  // cout << "check " << t <<endl;
  vector<pair<D,D> > B(N);
  D totV = 0;
  forn(i,N) {
    B[i].litr = t*A[i].rate;
    B[i].temp = A[i].temp;
    totV += B[i].litr;
  }
  if(totV+eps < V) return false;

  D mintemp = 0;
  D restV = V;
  for(in i=0; i<N; i++) {
    D l = min(restV, B[i].litr);
    mintemp += l*B[i].temp;
    restV -= l;
  }
  mintemp /= V;

  D maxtemp = 0;
  restV = V;
  for(in i=N-1; i>=0; i--) {
    D l = min(restV, B[i].litr);
    maxtemp += l*B[i].temp;
    restV -= l;
  }
  maxtemp /= V;
  // cout << "mintemp " << mintemp << " and maxtemp " << maxtemp << " for target " << X << endl;
  // if(mintemp <= X && X <= maxtemp) return true;
  if(mintemp-eps <= X && X <= maxtemp+eps) return true;
  return false;
}
void test() {
  cin >> N;
  cin >> V >> X;
  A = vector<pair<D,D> >(N);
  D tmin = 0;
  D tmax = 0;
  in anzeq = 0, anzlarger=0, anzsmaller = 0;
  forn(i,N) {
    cin >> A[i].rate >> A[i].temp;
    tmax = max(tmax,V/A[i].rate);
    if(A[i].temp > X) anzlarger++;
    if(A[i].temp == X) anzeq++;
    if(A[i].temp < X) anzsmaller++;
  }
  // cout << anzsmaller << anzeq << anzlarger << endl;
  vector<pair<D,D> >AA;
  forn(i,N) {
    if(A[i].temp==X) {
      AA.PB(A[i]);
    } else {
      if(A[i].temp < X && anzlarger!=0) {
        AA.PB(A[i]);
      } else if(A[i].temp > X && anzsmaller!=0) {
        AA.PB(A[i]);
      }
    }
  }
  A = AA;
  N = sz(A);
  // cout << N << " sources left" << endl;

  sort(A.begin(),A.end());
  if(N==0) {
    cout << "IMPOSSIBLE" << endl;
    return;    
  }
  if(!check(tmax)) {
    cout << "IMPOSSIBLE" << endl;
    return;
  }
  D tmid = tmin;
  while(abs(tmax-tmin) >= tmin*eps) {
    tmid = (tmin+tmax)/2.;
    // cout << "tmin " << tmin << " tmax " << tmax << " try tmid " << tmid << endl;
    if(check(tmid)) {
      tmax = tmid;
    } else {
      tmin = tmid;
    }
  }
  // if(!check(tmax)) {
  //   cout << "IMPOSSIBLE" << endl;
  //   return;
  // }
  cout << tmax << endl;
}
int main(){
  std::ios::sync_with_stdio(false); // remove this if you use printf/scanf
  std::cin.tie(0);
  std::cout << std::setprecision(20);

  in T; cin >> T;
  forn(t,T) {
    cout << "Case #" << t+1 << ": ";
    test();
  }

  return 0;  
}

#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cctype>
#include <algorithm>
#include <string>
#include <vector>
#include <deque>
#include <stack>
#include <queue>
#include <list>
#include <map>
#include <set>
using namespace std;

typedef long long ll;
#define sz(a)  int((a).size())
#define pb  push_back
#define all(c)  (c).begin(),(c).end()
#define tr(i,c)  for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)
#define rep(var,n)  for(int var=0;var<(n);var++)
#define found(s,e)  ((s).find(e)!=(s).end())

// #include "cout.h"

int N, K;
vector<double> P;

double prob(vector<int>& x) {
    vector<double> p, q;
    p.pb(1.0); // 0人 = 1.0
//    cout << "x:" << x << endl;
    rep(i, K) {
        q.assign(p.size()+1, 0.0);
        double pi = P[x[i]];
//        cout << i << " " << pi << " : " << p << endl;
        rep(j, p.size()) {
            q[j]   += p[j] * (1.0 - pi);
            q[j+1] += p[j] * pi;
        }
        swap(p, q);
    }
//    cout << K << " " << p << endl;
    return p[K/2];
}

int main(){
  int _T; cin>>_T; // 1-100
  rep(_t,_T){
//    int N,  // 2-16, 2-200
//        K; // 2 <= K <= N, even number
    cin >> N >> K;
    P.resize(N);
    rep(i,N) cin >> P[i]; // 0.0 <= Pi <= 1.0
//    cout << N << " " << K << " " << P << endl;

    int M = 1 << N;
    double xmax = 0;
    rep(p,M) {
        if (__builtin_popcount(p) != K) continue;
        vector<int> X;
        for (int i=0,m=1; i<N; ++i,m<<=1) {
            if (p & m) {
                X.push_back(i);
            }
        }
        double x = prob(X);
        xmax = max(xmax, x);
    }

 answer:
    printf("Case #%d: %.6f\n", 1+_t, xmax);
  }
}

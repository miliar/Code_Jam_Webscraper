#include <bits/stdc++.h>
// Print containers, pairs and tuples with ostream
#include "prettyprint.h"


using namespace std;

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    cin.tie(0);
    int T;
    cin >> T;
    for(int cas=1;cas<=T;++cas){
        cout << "Case #"<<cas<<": ";
      int N, K;
      cin >> N >> K;
      vector<double> p(N);
      for(int i=0;i<N;++i){
        cin >> p[i];
      }
      double out=0.0;
      for(int m=0;m<(1<<N);++m){
        if(__builtin_popcount(m) != K) continue;
        vector<double> P(K+1, 0.0);
        P[0] = 1;
        for(int i=0;i<N;++i){
          if(!(m&(1<<i)))continue;
          for(int j=K;j>=0;--j){
            if(j!=K)P[j+1]+=P[j] * p[i];
            P[j] = P[j] * (1-p[i]);
          }
        }
        out=max(out, P[K/2]);
      }
      cout <<fixed << setprecision(10) <<  out << "\n";
    }
    return 0;
}

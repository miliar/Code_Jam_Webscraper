#include<bits/stdc++.h>

#define REP(i,s,n) for(int i=s;i<n;i++)
#define rep(i,n) REP(i,0,n)
#define EPS (1e-8)
#define equals(a,b) (fabs((a)-(b)) < EPS)
#define MAX 1000000

using namespace std;

long double C,F,X;
long double precalc[MAX];

int main(){
  int T,CNT = 1;
  cin >> T;
  while(T--){
    cin >> C >> F >> X;
    long double ans = X / (long double)2.0;
    long double den = 2;
    REP(i,1,MAX){
      if( equals(C,X) || C > X ) break;
      precalc[i] = ((i-1>=1)?precalc[i-1]:0) + C / den;
      den += F;
      if( equals(precalc[i],ans) || precalc[i] > ans ) break;
      long double cost = precalc[i] + X/den;
      ans = min(ans,cost);
    }
    cout << "Case #" << CNT++ << ": " << setiosflags(ios::fixed) << setprecision(7) << ans << endl;
  }
  return 0;
}

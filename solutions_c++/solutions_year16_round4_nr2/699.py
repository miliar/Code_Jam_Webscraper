#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
const int MAX_N = 100030;    // Change as necessary
const ll  MODD = 1000000009; //

double A[MAX_N];

void do_case(){
  int N,K;
  cin >> N >> K;
  
  for(int i=0;i<N;i++) cin >> A[i];
  
  double best = 0;
  for(int i=0;i<(1 << N);i++){
    if(__builtin_popcount(i) != K) continue;
    double curr = 0;
    int num = 0;
    for(int x=i;x > 0; x = ((x-1) & i)){
      if(__builtin_popcount(x) != K/2) continue;
      num++;
      double P = 1;
      for(int k=0;k<N;k++){
        if(((i >> k) & 1) == 0) continue;
        if((x >> k) & 1) P *= A[k];
        else P *= (1 - A[k]);
      }
      curr += P;
    }
    if(best < curr) best = curr;
  }
  cout << best << endl;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  
  int T,C=1; cin >> T;
  
  cout << fixed << setprecision(10);
  
  while(T--){
    cout << "Case #" << C++ << ": ";
    do_case();
  }
  
  return 0;
}

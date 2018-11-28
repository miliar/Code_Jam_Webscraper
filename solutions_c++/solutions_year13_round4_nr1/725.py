#include <climits>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <queue>

using namespace std;
const int M=1000002013;

void run(int case_index) {
  long long res=0, cost1=0, cost2=0, n,m; cin>>n>>m;
  vector<long long> o(m),e(m),op(m),ep(m); for (int k = 0; k < m; k++) cin>>o[k]>>e[k]>>op[k], ep[k]=op[k];
  
  // before
  for (int k = 0; k < m; k++){
    long long d=e[k]-o[k],pay;
    pay = (d*(2*n-d+1)/2)%M;
    ( cost1 += (op[k]*pay)%M ) %= M;
  }
  
  // after
  vector<int> io(m), ie(m);  
  for (int k = 0; k < m; k++) io[k]=k, ie[k]=k;
  for (int i = 0; i < m; i++)
    for (int j = i; j < m; j++){
      if(o[io[i]]>o[io[j]]) swap(io[i],io[j]);
      if(e[ie[i]]>e[ie[j]]) swap(ie[i],ie[j]);
    }
  
  for (int k = 0; k < m; k++){
    long long s=0, pay, num, d;
    for (int j = m-1; j >= 0 ; j--){
      if (o[io[j]]<=e[ie[k]]){
        num = min(ep[ie[k]],op[io[j]]);
        op[io[j]] -= num;
        ep[ie[k]] -= num;
        d = e[ie[k]] - o[io[j]];
        pay = (d*(2*n-d+1)/2)%M;
        s += (num*pay)%M;
      }
    }
    (cost2 += s) %= M;
  }

  res = ((cost1-cost2+M)%M+M)%M;
  cout << "Case #" << case_index << ": " << res;
  cout << endl;
}

int main(int argc, char* argv[]) {
  int n; 
  cin >> n;
  for(int i = 1; i <= n; i++){
    cerr << i << " ";
    run(i);
  }
  cerr << endl;
  return 0;
}

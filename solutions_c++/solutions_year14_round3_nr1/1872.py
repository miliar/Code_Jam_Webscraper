#include <iostream>
#include <iomanip>
#include <cstdio>
#include <string>
#include <algorithm>
using namespace std;

using LL = long long;
using ULL = unsigned long long;

bool is_prime(const int n) {
  for(int i=2;i+1<=(int)sqrt(n);++i) {
    if(n%i==0) return false;
  }
  return true;
}

int main(){
  const string FW  = "Fegla Won";
  int T; cin >> T;
  for(int t=1;t<=T;++t) {
    int P,Q;
    scanf("%d/%d\n",&P,&Q);
    int res = -1;
    bool possible = true;

    for(int gen=0;gen<=40;++gen) {
      if(P>=Q) {
        if(res<0) res = gen;
        P -= Q;
      }
      P *= 2;
    }
    if(P>0 or res<0) possible = false;

    cout << "Case #" << t << ": ";
    if(possible) cout << res;
    else cout << "impossible";
    cout << endl;
  }
  return 0;
}

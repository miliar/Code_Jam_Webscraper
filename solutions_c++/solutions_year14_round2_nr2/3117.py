#include <iostream>
#include <iomanip>
#include <array>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <algorithm>
using namespace std;

using LL = long long;
using ULL = unsigned long long;

int main(){
  const string FW  = "Fegla Won";
  int T; cin >> T;
  for(int t=1;t<=T;++t) {
    ULL A,B,K; cin>>A>>B>>K;

    ULL cnt=0;
    for(ULL a=0;a<A;++a) {
      for(ULL b=0;b<B;++b) {
        ULL c = a&b;
        if(c<K) cnt++;
      }
    }

    cout << "Case #" << t << ": ";
    cout << cnt;
    cout << endl;
  }
  return 0;
}

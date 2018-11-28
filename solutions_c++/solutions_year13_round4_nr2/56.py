#include <iostream>
using namespace std;
#define int long long 
main(){
  int T;
  cin>>T;
  for(int tc=1;tc<=T;tc++){
    int N,P;
    cin>>N>>P;
    cout << "Case #" << tc << ": ";
    int y = 0;
    P --;
    int rr = 0;
    int now = 2;
    for(int i=N - 1;i>=0;i--){
      rr += 1LL << i;
      if(P<rr)break;
      y += now;
      now <<= 1;
    }
    y = min(y, (1LL << N) - 1);
    cout << y << " ";
    int z = 0;
    int add = 1LL << (N - 1);
    for(int i=1;i<=N;i++){
      int bit = (1LL << i) - 1;
      if(P < bit)break;
      z += add;
      add /= 2;
    }
    cout <<z <<  endl;
  }
  
}

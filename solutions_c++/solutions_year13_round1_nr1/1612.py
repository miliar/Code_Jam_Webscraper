#include<iostream>

using namespace std;

typedef long long ll;

int main(){
  int T;
  cin >> T;
  for(int x = 0; x < T; x++){
    ll r,t;
    cin >> r >> t;
    int req = 2*(r+1)+1;
    ll ans = 0;
    while(1){
      ll req = 2*(r+1)-1;
      if(t < req) break;
      ans++;
      t -= req;
      r += 2;
    }
    cout << "Case #" << x+1 << ": " << ans << endl;
  }
  return 0;
}

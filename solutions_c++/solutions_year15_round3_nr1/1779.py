#include <iostream>
#include <cmath>

using namespace std;

int main(){
  int t;
  cin >> t;
  for(int k=1;k<=t;k++){
    int r = 0,c = 0,w = 0;
    cin >> r >> c >> w;
    int ans = 0;
    if(w==c){
      ans = c;
    }
    else{
      ans =  (ceil( (c*1.0) / w ) + w-1) * r;
    }
    cout <<"Case #" << k << ": " << ans << endl;
  }
  return 0;
}

#include <iostream>
#include <algorithm>
#include <cstdio>
using namespace std;

double c,f,x;

void solve(){
  double nowf = 2.0, ans = 0.0;
  while(1){
    //double t = now / (nowf+f-nowf);
    double next = c / f * (nowf+f);
    //cout << next << endl;
    if(next < x){
      ans += c / nowf;
      nowf += f;
    } else{
      ans += x / nowf;
      break;
    }
  }

  printf("%.7f\n",ans);
}

int main(){
  int T;
  cin >> T;
  for(int t=1;t<=T;t++){
    cin >> c >> f >> x;
    cout << "Case #" << t << ": " << flush;
    solve();
  }
}

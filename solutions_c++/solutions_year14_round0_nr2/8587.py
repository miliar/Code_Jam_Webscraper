#include <iostream>
#include <iomanip>
using namespace std;

int main() {
  int t;
  cin>>t;
  for(int i=0;i<t;i++){
    double farm,target,newr,ntime,rate=2.0,time=0,timeo=0;
    cin>>farm>>newr>>target;
    while(1){
      timeo=time+target/rate;
      ntime=time+farm/rate+target/(rate+newr);
      if(timeo<ntime){
        cout<<setprecision(7)<<fixed<<"Case #"<<i+1<<": "<<timeo<<endl;
        break;
      }
      time+=farm/rate;
      rate+=newr;
    }
  }
  return 0;
}

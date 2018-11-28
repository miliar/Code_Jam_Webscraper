#include<iostream>
#include<iomanip>
using namespace std;

int main(){
  int T;
  cin>>T;
  int n=1;
  while(T--){
    double C,F,X;
    cin>>C>>F>>X;
    
    double currsum=0.0;
    double currspeed=2.0;
    double prev=1e10;
    while(true){
      double curr=X/currspeed+currsum;
      if(curr>prev)
         break;
      prev=curr;
      currsum+=C/currspeed;
      currspeed +=F;
    }
    cout<<"Case #"<<n++<<": "<<fixed<<setprecision(7)<<prev<<endl;
  }
}
